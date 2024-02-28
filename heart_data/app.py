from flask import Flask, render_template,url_for,request
from flask import jsonify
from utils import get_predicated_heart

app = Flask(__name__)

@app.route('/predict_heart' ,method= ['GET'])
def predict_heart():
    print("*"*50)
    data = request.form
    age = eval(data['age'])
    sex = eval(data['sex'])
    cp = eval(data['cp'])
    trestbps = eval(data['trestbps'])
    chol = eval(data['chol'])
    # fbs = eval(data['fbs'])
    # restecg = eval(data['restecg'])
    # thalach = eval(data['thalach'])
    # exang = eval(data['exang'])
    # oldpeak = eval(data['oldpeak'])
    # slope = eval(data['slope'])
    # ca = eval(data['ca'])
    # thal= eval(data['thal']) 
    
    result = get_predicated_heart(age, sex, cp, trestbps, chol)


    return jsonify({"Response":"Successful",
                    'Result':f"Predicted heart data is : {result} "})
    
    
    
if __name__ == "__main__":
    
    app.run(host='0.0.0.0',port=5002,debug=False)



