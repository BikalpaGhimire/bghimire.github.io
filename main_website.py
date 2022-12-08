from flask import Flask, render_template
myweb = Flask(__name__)


@myweb.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    myweb.run(debug=True)