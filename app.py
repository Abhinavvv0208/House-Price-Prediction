'''from flask import Flask,request,jsonify
import util

app= Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/predict_home_price',methods=['GET','POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
            'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
        })

        response.headers.add('Access-Control-Allow-Origin','*')
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    util.load_saved_artifacts()
    print("Starting Python Flask Server For House Price Prediction...")
    app.run()
'''

from flask import Flask, request, jsonify
import util
import os

app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])  # Removed GET for clarity
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        response = jsonify({
            'estimated_price': estimated_price
        })
        response.status_code = 200
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.status_code = 400  # Set HTTP error code

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    util.load_saved_artifacts()
    print("Starting Python Flask Server For House Price Prediction...")
    app.run()
