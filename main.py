from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@ app.route("/", methods=['POST'])
def error():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]
    user_error = ""
    pass_error = ""
    ver_error = ""
    email_error = ""
    if len(username) == 0:
        user_error = "Please input a username."

    if len(username) <= 3 or len(username) >= 20:
        user_error = "Your username is the worng length, please try again."

    if len(password) == 0:
        pass_error = "Please input a password"

    if len(password) <= 3 or len(password) >= 20:
        pass_error = "Your password is the worng length, please try again."

    if password != verify:
        ver_error = "Your passwords do not match please try again."

    if len(email) == 0:
        email_error= ""
    else:
        if len(email) >= 3 or len(email) <= 20 or email.count("@") != 1 or email.count(".") != 1 or email.count(" ") != 0:
            email_error = "Your email is incorrect, please make sure it has only 1 @, 1 ., zero spaces and is a proper length."

    if  len(user_error) != 0 or len(pass_error) != 0 or len(ver_error) != 0 or len(email_error) != 0:
        return render_template("index.html", user_error=user_error, pass_error=pass_error, ver_error=ver_error, email_error=email_error)
    else:
        return render_template("welcome.html", username=username)

@app.route("/")
def index():
    username= request.args.get("username")
    return render_template("index.html", username=username)

app.run()