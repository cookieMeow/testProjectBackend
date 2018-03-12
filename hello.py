from flask import Flask, render_template, session, redirect, url_for, escape, request
app = Flask(__name__)

@app.route("/<var>")
def index(var):
    return "Index Page%s" % var

@app.route("/meow")
def meow():
	return "Meow is cute!"

@app.route("/dataAction/<data>", methods=['GET', 'POST'])
def dataAction(data):
	print data
	return "data="+data

if __name__ == "__main__":
    app.run(debug=True)