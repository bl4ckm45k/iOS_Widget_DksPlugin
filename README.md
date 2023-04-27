### A simple web server for DksPlugin DarkBot and a widget script for the Scriptable application.
#### Why?
DksPlugin itself has no authentication and transmits game session data (server and SID).

Thus, anyone with a link immediately gets access to all account data (id, nickname, server, SID).

When receiving data from the plugin, the server deletes the session data.

Access to the rest of the data is provided only if you have a login and password to the web server.

### Sign Up [ngrok](https://www.ngrok.com/ "ngrok") and Get [ngrok auth token](https://dashboard.ngrok.com/get-started/your-authtoken "ngrok auth token")
- Setup web server login, password, ngrok auth token, and local port (The same as in the DksPlugin settings) in `.env` file

### Windows (Without python install)
- Download and Install [Memurai (Redis) for Windows](https://www.memurai.com/get-memurai "Redis")
- Perform a reboot
- Execute DarkBot_iOS_Dks_Widget.exe
- Copy you ngrok URL from terminal. Replace url, login and password in `do_widget.js` (Line 58).
- Create a new script in the Scriptable app and paste the contents do_widget.js . Place the widget. Done

P.S. You can compile the exe file yourself using the commands:
```pycon
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip 
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --noconfirm --onefile --console --icon "C:/YOUR_PATH/db.ico" --name "DarkBot_iOS_Dks_Widget" --clean --log-level "DEBUG" --collect-binaries "passlib" --collect-all "passlib"  "C:/YOUR_PATH/web_server/main.py"
```



### Windows (With python install)
- Download and Install [Python 3.11 (Windows installer (64-bit)](https://www.python.org/downloads/release/python-3113/ "Python")
- Download and Install [Memurai (Redis) for Windows](https://www.memurai.com/get-memurai "Redis")
- Perform a reboot
- Unpack the contents of the web_server to the destination folder. In folder run commands:
    ```pycon
    python -m venv venv
    venv/Scripts/activate
    pip install --upgrade pip 
    pip install -r requirements.txt
    python -m main
    ```
- Copy you ngrok URL from terminal. Replace url, login and password in `do_widget.js` (Line 58).
- Create a new script in the Scriptable app and paste the contents do_widget.js . Place the widget. Done