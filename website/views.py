from flask import Blueprint, redirect, render_template, session, request, url_for
from website import logging
from .utils import server_info

views = Blueprint('views', __name__)
logger = logging.getLogger(__name__)
readme = 'README.md'


@views.route('/')
def index():
    appVer = getAppVersion()
    serv_info = server_info()
    session["appVer"] = appVer
    logger.info(f"App Version : {appVer}")
    return render_template('index.html', title='Home', serv_info=serv_info)


@views.route("/greet", defaults={'name': 'KingKong'}, methods=['GET', 'POST'])
@views.route("/greet/<string:name>")
def greet(name):
    if request.method == 'GET':
        return render_template('greet.html', title='Greet', name=name)
    if request.method == 'POST':
        name = request.form.get('inputValue')
        if not name:
            name = "KingKong"
        return redirect(url_for('views.greet', name=name))


@views.route('/about')
def about():
    return render_template('about.html', title='About')


@views.route('/update-version')
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
            f.writelines(data)
            logger.info(f"App Version is updated : {appver}")

    return redirect(url_for('views.index'))


def getAppVersion() -> str:
    appVer = ""
    try:
        with open(readme, 'r') as f:
            data = f.readlines()
        appVer = [x.rstrip('\n').split(" ")[-1]
                  for x in data if 'Version' in x][0]
    except IndexError:
        logger.error(
            'README.md file is missing or with no "App Version" in the source code')
    return appVer
