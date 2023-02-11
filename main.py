from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/')
def main():
    with open('templates/html_/base.html') as main_html:
        return '<a href=http://127.0.0.1:12398/index>to go </a>'


@app.route('/index/<page_name>')
def index(page_name):
    if 'инженер' in page_name or 'строител' in page_name:
        return render_template('html_/base.html', page_name=page_name,
                               src='/static/Inkeda23bd91402c815b048859dca0c8cc266_LI.jpg')
    else:
        return render_template('html_/base.html', page_name=page_name,
                               src='/static/a23bd91402c815b048859dca0c8cc266.jpg')


if __name__ == '__main__':
    app.run(port=12398, host='127.0.0.1')