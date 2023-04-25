from dataclasses import dataclass
import os
from environs import Env

from security import get_password_hash


@dataclass
class User:
    login: str
    password: str
    hashed_password: str


@dataclass
class Secret:
    key: str


@dataclass
class Server:
    port: int
    use_ngrok: bool
    ngrok_auth_token: str


@dataclass
class Config:
    user: User
    secret: Secret
    server: Server


def load_config():
    env = Env()
    env.read_env(f'{os.getcwd()}/.env')
    import secrets
    secret_key = secrets.token_hex(32)
    return Config(
        user=User(
            login=env.str('LOGIN'),
            password=env.str('PASSWORD'),
            hashed_password=get_password_hash(env.str('PASSWORD'))
        ),
        secret=Secret(key=secret_key),
        server=Server(port=env.int('LOCAL_PORT'),
                      use_ngrok=env.bool('USE_NGROK'),
                      ngrok_auth_token=env.str('NGROK_AUTH_TOKEN')
                      )
    )
