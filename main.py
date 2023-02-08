from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def main():
    with open('static/html_/main.html') as main_html:
        return main_html.read()


@app.route('/index')
def index():
    with open('static/html_/index.html', encoding='UTF-8') as index_html:
        return index_html.read()


if __name__ == '__main__':
    app.run(port=12398, host='127.0.0.1')