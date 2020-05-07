from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/code')
def code():
    return render_template('code.html')


if __name__ == '__main__':
    app.run()