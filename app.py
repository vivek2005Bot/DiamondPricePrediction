from flask import Flask,request,render_template
import numpy as np
import socket
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipelines.prediction_pipeline import PredictPipeline,CustomData

application=Flask(__name__)

app=application

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_data():
    if request.method=='GET':
        return render_template('home.html')
    else:
         data=CustomData(
            
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        # this is my final data
         final_data=data.get_data_as_dataframe()
        
         predict_pipeline=PredictPipeline()
        
         pred=predict_pipeline.predict(final_data)
        
         result=round(pred[0],2)
        
         return render_template("result.html",final_result=result)

if __name__ == '__main__':
    host = socket.gethostbyname(socket.gethostname())  # Get the local machine's IP
    port = 8080
    print(f"Server running at http://{host}:{port}/")  # Display clickable URL
    app.run(host=host, port=port, debug=True)