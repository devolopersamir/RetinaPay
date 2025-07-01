from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    user = data['user']
    amount = data['amount']

    with open('db.json', 'r') as f:
        db = json.load(f)

    if user not in db:
        return jsonify({"status": "error", "message": "User not found"})

    if db[user]['balance'] < amount:
        return jsonify({"status": "error", "message": "Insufficient balance"})

    db[user]['balance'] -= amount

    with open('db.json', 'w') as f:
        json.dump(db, f, indent=4)

    return jsonify({"status": "success", "message": f"Withdrawn {amount}৳ successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
