from flask import Flask,render_template,request,send_file,send_from_directory,jsonify
import pandas as pd
import numpy as np
import csv
app=Flask(__name__)
#@app.route("ground.csv")
#@app.route("/ground.csv",methods=['GET','POST'])
# DOWNLOAD_DIRECTORY = "D:\sem7\bda\ipl_app"
# app.config["CLIENT_CSV"]="D:\sem7\bda\ipl_app"

@app.route("/csv", methods=['GET', 'POST'])
def data():
    j = []
    with open('ground.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            j.append(row)
    return jsonify(j)







    # data=pd.read_csv('ground.csv')
    # j = [np.array(['venue', 'counts'])]
    # for i in file.values:
    #     j.append(i)


    # csv_filename="ground.csv"
    # data=pd.read_csv(csv_filename)
    # # return render_template('base.html',data=data)
    # try:
    #     return jsonify(data)
    # except FileNotFoundError:
    #     abort(404)
@app.route("/")
def index():
    return render_template('test.html')
    # csv_filename = "ground.csv"
    # data = pd.read_csv(csv_filename)
    # return render_template('base.html',data=data)

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')
if __name__=="__main__":
    app.run(debug=True)