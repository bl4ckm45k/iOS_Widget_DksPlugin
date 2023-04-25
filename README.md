### Sign Up [ngrok](https://www.ngrok.com/ "ngrok") and Get [ngrok auth token](https://dashboard.ngrok.com/get-started/your-authtoken "ngrok auth token")
Setup web server login, password, ngrok auth token, and local port (The same as in the DksPlugin settings) in `.env` file

## Windows (Without python install)
#### Download and Install [Memurai (Redis) for Windows](https://www.memurai.com/get-memurai "Redis")

1. Perform a reboot

2. Execute DarkBot_iOS_Dks_Widget.exe

3. Copy you ngrok URL from terminal. Replace url, login and password in `do_widget.js` (Line 58).

4. Create a new script in the Scriptable app and paste the contents do_widget.js . Place the widget. Done

P.S. You can compile the exe file yourself using the command:
```pycon
pyinstaller --noconfirm --onefile --console --icon "C:/YOUR_PATH/db.ico" --name "DarkBot_iOS_Dks_Widget" --clean --log-level "DEBUG" --collect-binaries "passlib" --collect-all "passlib"  "C:/YOUR_PATH/web_server/main.py"
```



## Windows (With python install)
#### Download and Install [Python 3.11 (Windows installer (64-bit)](https://www.python.org/downloads/release/python-3113/ "Python")
#### Download and Install [Memurai (Redis) for Windows](https://www.memurai.com/get-memurai "Redis")
1. Perform a reboot

2. Unpack the contents of the web_server to the destination folder. In folder run commands
    ```pycon
    python -m venv venv
    python -m pip install --upgrade pip 
    pip install -r requirements.txt
    python -m main
    ```

3. Copy you ngrok URL from terminal. Replace url, login and password in `do_widget.js` (Line 58). Done
4. Create a new script in the Scriptable app and paste the contents do_widget.js . Place the widget. Done