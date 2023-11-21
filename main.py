from flask import Flask, render_template


#Website Object
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<statioon>/<date>")
def about(station, date):

    #We only need the temperature for the dic, the rest will be asked to the user. 

    return {"statioon": station,
            "date": date,
            "temperature": temperature}

if __name__ == '__main__':
   app.run(debug=True, port=5001)
