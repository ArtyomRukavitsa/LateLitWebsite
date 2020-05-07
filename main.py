from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная | LateLit')


@app.route('/support')
def support():
    return render_template('support.html', title='Поддержка | LateLit')


@app.route('/code')
def code():
    return render_template('code.html', title='Код доступа | LateLit')


if __name__ == '__main__':
    app.run()
