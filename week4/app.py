from flask import Flask
from flask import request
from flask import redirect
from flask import json
from flask import render_template
from flask import session
from flask import url_for
app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/") 

app.secret_key = "wrerw"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/signin',methods=["POST"])
def ver():
    name = request.form.get("account", "")
    password = request.form.get("password", "")

    if name!="test" or password!= "test":
        return redirect("/error?message=請輸入正確的帳號密碼")
    else:
        session["role"] = name
        return redirect(url_for('member'))
    

@app.route("/member")
def member():
    if "role" in session:
        name = session["role"]
        return render_template("member.html", user=name)
    else:
        return redirect(url_for('index'))


#表單和回傳
@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", message=message)

@app.route("/signout")
def out():
    session.clear()
    return redirect(url_for('index'))

@app.route('/square/<number>')
def square(number):
    square = int(number)*int(number);
    return render_template("square.html",square=square)

app.run()

