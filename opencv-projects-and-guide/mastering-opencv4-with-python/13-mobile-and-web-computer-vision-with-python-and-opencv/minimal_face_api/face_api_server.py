from flask import Flask, request, jsonify
import urllib.request
from face_processing import FaceProcessing


# Initialize application and FaceProcessing
app = Flask(__name__)
face_api = FaceProcessing()


@app.errorhandler(400)
def bad_request(e):
    return jsonify({
        "status": "not ok",
        "message": "this server could not understand your request"
    }), 400


@app.errorhandler(404)
def not_found(e):
    """
    The obtained status code (404) means that the client could communicate with the server,
    but the server could not find what was requested.
    """
    return jsonify({
        "status": "not found",
        "message": "route not found"
    }), 404


@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "status": "internal error",
        "message": "internal error occurred in server"
    }), 500


@app.route("/detect", methods=["GET", "POST", "PUT"])
def detect_human_faces():
    if request.method == "GET":
        if request.args.get("url"):
            with urllib.request.urlopen(request.args.get("url")) as url:
                return jsonify({"status": "ok", "result": face_api.face_detection(url.read())}), 200
        else:
            return jsonify({"status": "bad request", "message": "Parameter url is not present"}), 400
    elif request.method == "POST":
        if request.files.get("image"):
            return jsonify({"status": "ok", "result": face_api.face_detection(request.files["image"].read())}), 200
        else:
            return jsonify({"status": "bad request", "message": "Parameter image is not present"}), 400
    else:
        return jsonify({"status": "failure", "message": "PUT method not supported for API"}), 405


if __name__ == '__main__':
    # Add parameter host='0.0.0.0' to run on your machines IP address
    app.run(host="0.0.0.0")
