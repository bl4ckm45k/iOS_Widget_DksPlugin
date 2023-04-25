let data = await getData()
let widget = await createWidget()
if (config.runsInWidget) {
    // The script runs inside a widget, so we pass our instance of ListWidget to be shown inside the widget on the Home Screen.
    Script.setWidget(widget)
} else {
    // The script runs inside the app, so we preview the widget.
    widget.presentMedium()
}
// Calling Script.complete() signals to Scriptable that the script have finished running.
// This can speed up the execution, in particular when running the script from Shortcuts or using Siri.
Script.complete()

async function createWidget() {
    let widget = new ListWidget()
    widget.setPadding(0, 0, 0, 0)
    // Add background gradient
    let gradient = new LinearGradient()
    gradient.locations = [0, 1]
    gradient.colors = [
        new Color("141414"),
        new Color("13233F")
    ]
    widget.backgroundGradient = gradient
    let uri_indicator = SFSymbol.named("largecircle.fill.circle")
    //widget.addSpacer();
    for (j = 0; j < data.length; j++) {
        let user_name = widget.addStack()
        let userText = user_name.addText("Player: " + data[j].hero.username + " | Map: " + data[j].map + " ");
        let ind = user_name.addImage(uri_indicator.image);
        if (data[j].alert === true) {
            ind.tintColor = Color.red();
        } else {
            ind.tintColor = Color.green();
        }

        ind.imageSize = new Size(8, 8)
        userText.textColor = Color.white();
        userText.textOpacity = 0.8;
        userText.font = Font.boldMonospacedSystemFont(10);
        widget.addSpacer(1);

        let stats2 = widget.addStack()
        let statsText2 = stats2.addText("Running: " + data[j].stats.runningTime + " | URI/Hr: " + data[j].stats.uridiumPerHour + " | Total URI: " + data[j].stats.totalUridium);
        statsText2.textColor = Color.white();
        statsText2.textOpacity = 0.8;
        statsText2.font = Font.boldMonospacedSystemFont(10);
        widget.addSpacer(4);
    }

    return widget
}

async function getData() {
    // Your host's URL (ngrok tunnel or your domain with ssl)
    // URL вашего хоста (тунель ngrok или вашего домена с ssl)
    // https://1b84-79-139-999-127.ngrok-free.app
    let host = "NGROK URL";

    // username and password which you have installed in the ".env" file
    let username = 'some_name';
    let password = 'some_password';

    let token = await auth(host, username, password);
    let request = new Request(host + "/do_widget")
    request.headers = {'Authorization': 'Bearer ' + token};

    let response = await request.loadJSON()
    return await response

}

async function auth(host, username, password) {
    let request = new Request(host + "/token")
    request.method = "POST"
    request.addParameterToMultipart("username", username)
    request.addParameterToMultipart("password", password)
    let response = await request.loadJSON()
    let response_data = await response
    return response_data["access_token"]
}
