from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Customers list
customers = []

@app.route('/customers', methods=['GET'])
def get_customers():
    response = jsonify({'customers': customers}), 200

    return response

@app.route('/customers', methods=['POST'])
def new_customer():
    request_data = request.get_json()
    customer_data = request_data['customer']

    customers.append({'name': customer_data['name'], 'email': customer_data['email']})

    return 'OK', 201


if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port="5000", debug=True)