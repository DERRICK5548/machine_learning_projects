import requests

# POST request with application data
response = requests.post( 
    'https://127.0.0.1:5000/predict',
    json={ 
        'age'=:32, 'income':75000, 'loan_amount': 25000, 'credit_score':720,
        'job_type': 'employed', 'education': 'degree'
    }
)
result = response.json()
print(result)
print("/n End of response")

