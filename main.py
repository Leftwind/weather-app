from flask import Flask, render_template


#Website Object
app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<statioon>/<date>")
def about(station, date):
    
    return render_template("about.html")


app.run(debug=True)
