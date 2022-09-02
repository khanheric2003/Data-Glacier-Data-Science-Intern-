from turtle import setx
from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)
df = pd.read_csv("VietNamH.csv")

@app.route('/')
def index():
    sex = sorted(df["sex"].unique())
    urban_opt = sorted(df["urban"].unique())
    return render_template('index.html', sex=sex,urban_opt=urban_opt)

if __name__=="__main__": 
    app.run(debug=True)
