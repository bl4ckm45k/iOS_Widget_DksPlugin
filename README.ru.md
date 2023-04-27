### Простой веб-сервер для DksPlugin DarkBot и скрипт виджета для приложения Scriptable. 
#### Зачем?
Сам DksPlugin не имеет никакой аутентификации и передает данные игровой сессии (сервер и SID).

Таким образом любой человек имеющий ссылку сразу получает доступ ко всем данным аккаунта (id, ник, сервер, SID).

При получении данных от плагина сервер удаляет данные о сессии.

Доступ к остальным данным предоставляется только при наличии логина и пароля к веб-серверу.

### Зарегистрируйтесь на  [ngrok](https://www.ngrok.com/ "ngrok") и получите [ngrok auth token](https://dashboard.ngrok.com/get-started/your-authtoken "ngrok auth token")
В файле `.env` установите логин, пароль и локальный порт (Как в настроках DksPlugin) для веб-сервера, а также токен ngrok.

### Windows (Без установки Python)
- Скачайте и установите [Memurai (Redis) for Windows](https://www.memurai.com/get-memurai "Redis")

- Выполните перезагрузку
- Запустите DarkBot_iOS_Dks_Widget.exe
- Скопируйте ссылку тунеля ngrok из терминала. Замените ссылку, укажите логин и пароль от веб-сервера в файле `do_widget.js` (Строка 58).
- Создайте новый скрипт в приложении Scriptable и вставьте содержимое файла do_widget.js. Установите виджет. Готово

P.S. Вы можете самостоятельно скомилировать exe файл, установив python и выполнив команды:
```pycon
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip 
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --noconfirm --onefile --console --icon "C:/YOUR_PATH/db.ico" --name "DarkBot_iOS_Dks_Widget" --clean --log-level "DEBUG" --collect-binaries "passlib" --collect-all "passlib"  "C:/YOUR_PATH/web_server/main.py"
```



### Windows (С установкой python)
- Скачайте и установите [Python 3.11 (Windows installer (64-bit)](https://www.python.org/downloads/release/python-3113/ "Python")
- Скачайте и установите [Memurai (Redis) for Windows](https://www.memurai.com/get-memurai "Redis")
- Выполните перезагрузку
- Распакуйте папку web_server в папку назначения. В папке выполните команды:
    ```pycon
    python -m venv venv
    venv/Scripts/activate
    python -m pip install --upgrade pip 
    pip install -r requirements.txt
    python -m main
    ```
-  Скопируйте ссылку тунеля ngrok из терминала. Замените ссылку, укажите логин и пароль от веб-сервера в файле `do_widget.js` (Строка 58).
- Создайте новый скрипт в приложении Scriptable и вставьте содержимое файла do_widget.js. Установите виджет. Готово