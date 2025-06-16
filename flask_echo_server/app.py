from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/bugreport', methods=['POST'])
def bugreport():
    data = request.get_json()
    print(f"Bug report: {data['report']}")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)

