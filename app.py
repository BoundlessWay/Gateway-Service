from flask import Flask, request, jsonify
import requests
from flasgger import Swagger, swag_from
from services.user_service import get_user_data
from services.event_service import get_event_data

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/gateway', methods=['POST'])
@swag_from('swagger/gateway_swagger.yml')
def gateway():
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    try:
        service_name = data.get('service')
        if service_name == 'user':
            response = get_user_data()
        elif service_name == 'order':
            response = get_event_data()
        else:
            return jsonify({'error': 'Unknown service'}), 400

        return response

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
