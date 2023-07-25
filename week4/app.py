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
def signin():
    name = request.form.get("account", "")
    password = request.form.get("password", "")
    agree = request.form.get("checked", "")
    if agree != "on":
        print(name,password,agree)
        return redirect("/")
    elif(name!="test" or password!= "test"):
        return redirect("/error?message=請輸入正確的帳號和密碼")
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

@app.route("/error")
def error():
    message = request.args.get("message", "")
    print(message)
    return render_template("error.html", message=message)

@app.route("/signout")
def out():
    session.clear()
    return redirect(url_for('index'))

@app.route('/cal',methods=["POST"])
def cal():
    number = request.form.get('number')
    try:
        number = int(number)
        print(type(number))
        if isinstance(number, int):
            return redirect(url_for('square', number=number))
        else:
            return redirect(url_for('index'))
    except ValueError:
        return redirect(url_for('index'))


@app.route("/square/<number>")
def square(number):
        square = int(number)*int(number)
        return render_template("square.html",square=square)

app.run()

