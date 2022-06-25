from flask import Flask, redirect, render_template, session, request, url_for

app = Flask(__name__)
# app.secret_key = "mysecret"
# app.config["SESSION_PERMANENT"] = False
app.config['SECRET_KEY'] = "sdkdlkl3kjl"
app.config.SESSION_COOKIE_SAMESITE = 'None'
app.config.SESSION_COOKIE_SECURE = 'True'
# Session(app)
readme = 'README.md'


@app.route('/')
def index():
    appVer = getAppVersion()
    session["appVer"] = appVer
    return render_template('index.html', title='Home')


@app.route("/greet", defaults={'name': 'KingKong'}, methods=['GET', 'POST'])
@app.route("/greet/<string:name>")
def greet(name):
    if request.method == 'GET':
        return render_template('greet.html', title='Greet', name=name)
    if request.method == 'POST':
        name = request.form.get('inputValue')
        return redirect(url_for('greet', name=name))


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/update-version')
def updateAppVersion():
    appver = request.args.get('val')
    if appver:
        with open(readme, 'r') as f:
            data = f.readlines()
        for index, line in enumerate(data):
            if 'App Version' in line:
                content = line.rstrip("\n").split(" ")
                content[-1] = f"{appver}\n"
                line = " ".join(content)
                data[index] = line

        with open(readme, 'w') as f:
            print(data)
            f.writelines(data)

    return redirect(url_for('index'))


def getAppVersion() -> str:
    appVer = ""
    try:
        with open(readme, 'r') as f:
            data = f.readlines()
        appVer = [x.rstrip('\n').split(" ")[-1]
                  for x in data if 'Version' in x][0]
    except IndexError:
        print('README.md file is missing or with no "App Version" in the source code')

    return appVer


if __name__ == "__main__":
    app.run(debug=True)
