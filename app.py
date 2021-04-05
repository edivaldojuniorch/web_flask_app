from flask import Flask, redirect, render_template, request, session, abort


app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('template_hello.html',var_template_name = name,var_template_footer_message_1="Site lindão!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
