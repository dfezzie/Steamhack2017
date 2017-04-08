from flask import Flask, render_template

from modules.twitter import twitter_blueprint

app = Flask(__name__)
app.register_blueprint(twitter_blueprint)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api')
def api():
    return 'Hi'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
