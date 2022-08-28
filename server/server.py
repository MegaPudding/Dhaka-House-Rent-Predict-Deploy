from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'Locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    Area = float(request.form['total_sqft'])
    Location = request.form['Location']
    Bed = int(request.form['Bed'])
    Bath = int(request.form['Bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(Location,Area,Bed,Bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting python flask server...")
    app.run()