from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/time")
def get_time():
    now_utc = datetime.now(timezone.utc)
    # Local time according to the server’s timezone
    now_local = datetime.now()
    payload = {
        "utc_iso": now_utc.isoformat(),
        "local_iso": now_local.isoformat(),
        "server": "flask-warmup",  # extra field
    }
    return jsonify(payload), 200

@app.get("/ping")
    x = {
        "message": "API is alive"
    }

if __name__ == "__main__":
    # Fixed port for consistency
    app.run(host="0.0.0.0", port=5000, debug=True)
