
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    if (prediction >= 0.5):
        a = "Phishing"
    else:
        a = "Not a Phishing"
    return render_template('test.html',prediction_text="This is a {} Website".format(str(a)))
     

if __name__ == "__main__":
    app.run(debug=True)