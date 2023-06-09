import json
import logging
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseSettings
from pyngrok.conf import PyngrokConfig

from auth import router_auth, get_current_active_user
from loader import redis_cli, config
from models import User
from utils import process_data

logger = logging.getLogger('web_server')


class Settings(BaseSettings):
    # ... The rest of our FastAPI settings

    BASE_URL = f"http://localhost:{config.server.port}"
    USE_NGROK = config.server.use_ngrok


settings = Settings()

app = FastAPI(docs_url=None, redoc_url=None)

origins = [
    f"http://localhost:{config.server.port}"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

app.include_router(router_auth, tags=["auth"])


@app.post("/")
async def dks(request: Request):
    if request.headers['host'] != origins[0].split('//')[1]:
        raise HTTPException(status_code=401, detail="Feel too sexy to accept requestes")
    data = await request.json()
    del data['sesion'], data['deaths'], data['tick']
    if data["hero"]["id"] != 0:
        await redis_cli.set(f'darkbot:{data["hero"]["id"]}', json.dumps(await process_data(data)), ex=600)


@app.get("/do_widget")
async def widget(current_user: Annotated[User, Depends(get_current_active_user)]):
    return [json.loads(await redis_cli.get(key)) for key in await redis_cli.keys('darkbot:*')]


if __name__ == "__main__":
    if settings.USE_NGROK:
        import os
        from pyngrok import conf, ngrok
        from pyngrok.exception import PyngrokNgrokError

        conf.get_default().auth_token = config.server.ngrok_auth_token
        conf.set_default(PyngrokConfig(region="eu",
                                       ngrok_path=f"{os.getcwd()}/ngrok.exe",
                                       auth_token=config.server.ngrok_auth_token),
                         )

        # Open a ngrok tunnel to the dev server
        try:
            ng_connect = ngrok.connect(settings.BASE_URL)
            print(f'\n\nYOU NGROK TUNNEL:\n\n{ng_connect}\n\n')
            logger.info(f"ngrok tunnel {ng_connect.public_url} -> {settings.BASE_URL}")
        except PyngrokNgrokError:
            pass

    # If u don't use exe file u can switch reload to "True"
    uvicorn.run(f"{__name__}:app", host="127.0.0.1", port=config.server.port, log_level="info", workers=1, reload=False)
