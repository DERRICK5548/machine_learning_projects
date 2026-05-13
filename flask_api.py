from flask import Flask, request, jsonify
import joblib
import pandas as pd

# creating object of Flask class
app = Flask(__name__)

# loading model
model = joblib.load('loan_approval_v1.0.0.pkl')

# COMMON HTTP methods: **GET** -retrieves data, **POST**- send data, **PUT** - update data

# home route
@app.route('/') # localhost -> localhost:5000/
def home():
    return{
        'message': 'Loan Approval API running'
    }
# prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # receive json data from the client
    data = request.get_json()
    print("Data incoming...")
    print(data)

    # validate recieved data
    required = ['age', 'income', 'loan_amount', 'credit_score','job_type','education']
    for field in required:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
        
    # make prediction
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return jsonify({ 
        'approved':bool(prediction),
        'confidence': round(probability, 4),
        'message': 'Approved' if prediction else 'Not approved, Next time'
    })
@app.route('/health')

def health():
    
    return jsonify({ 
       'status': 'ok',
       'model': 'loan_approval'
    })



   


if __name__ == '__main__':
    app.run(debug=True, port=5000)
