from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your turret's ngrok URL
TURRET_URL = "https://7aecb3c3fa0f.ngrok-free.app/fire"

@app.route('/trigger', methods=['POST'])
def trigger_turret():
    try:
        print("📩 Request received to fire turret")

        # Optional: check a secret token
        data = request.get_json()
        if data.get("token") != "SECRET123":
            return jsonify({"error": "Unauthorized"}), 401

        # Fire the turret
        response = requests.post(TURRET_URL)
        print(f"➡️ Turret fired! Status: {response.status_code}")
        return jsonify({"status": "fired"}), 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

