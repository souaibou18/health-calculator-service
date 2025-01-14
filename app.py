from flask import Flask, request, jsonify, render_template
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    height = data.get('height') 
    weight = data.get('weight') 
    if not height or not weight:
        return jsonify({"error": "Height and weight are required"}), 400
    bmi_value = calculate_bmi(height, weight)
    return jsonify({"bmi": round(bmi_value, 2)})

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    height = data.get('height') 
    weight = data.get('weight') 
    age = data.get('age')
    gender = data.get('gender') 
    if not all([height, weight, age, gender]):
        return jsonify({"error": "Height, weight, age, and gender are required"}), 400
    bmr_value = calculate_bmr(height, weight, age, gender)
    return jsonify({"bmr": round(bmr_value, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
