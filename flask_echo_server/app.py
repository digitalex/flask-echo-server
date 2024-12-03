from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/strlen')
def strlen():
    text = request.args.get('text')
    if text is None:
        return jsonify({"error": "Missing 'text' query parameter"}), 400
    length = len(text)
    return jsonify({"length": length})

if __name__ == "__main__":
    app.run(debug=True)

