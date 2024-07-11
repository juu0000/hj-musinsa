from flask import Flask, request, jsonify
from iam_utils import get_old_iam

app = Flask(__name__)

@app.route('/old-iam', methods=['GET'])
def old_iam():
    try:
        n_hours = int(request.args.get('hours'))
        old_iams = get_old_iam(n_hours)
        return jsonify(old_iams), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
