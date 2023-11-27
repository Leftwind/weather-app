from flask import Flask, render_template
import pandas as pd

#Website Object
app = Flask(__name__)

#Show Stations

estaciones = pd.read_csv("data/stations.txt", skiprows=17)
estaciones = estaciones[['STAID','STANAME                                 ']]


@app.route("/")
def home():
    return render_template("home.html", data=estaciones.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):

    #We only need the temperature for the dic, the rest will be asked to the user. 
    filename = 'data/TG_STAID' + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows = 20, parse_dates=['    DATE'])
       
    temperature = df.loc[df['    DATE']==date]['   TG'].squeeze() /10 
    return {"statioon": station,
            "date": date,
            "temperature": temperature}

if __name__ == '__main__':
   app.run(debug=True, port=5001)
