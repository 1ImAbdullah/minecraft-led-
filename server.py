from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/led", methods=["POST"])
def led():
    state = request.form.get("state", "off")
    socketio.emit("led_update", {"state": state})
    return "OK"

@app.route("/")
def index():
    return open("index.html").read()

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8080)
