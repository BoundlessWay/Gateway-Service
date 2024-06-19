from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Route chính cho gateway
@app.route('/gatway', methods=['POST'])
def gateway():
    data = request.json
    print(data)
    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    # Chuyển tiếp yêu cầu đến một dịch vụ khác
    try:
        response = requests.post('http://localhost:8081/user', json=data)
        print(response)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
