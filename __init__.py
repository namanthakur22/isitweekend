import datetime
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    weekend = now.strftime("%A")
    return render_template("index.html",weekend=weekend)

if __name__=="__main__":
    app.run()
