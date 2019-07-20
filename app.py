from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def main_route():
    return render_template('index.html')


@app.route('/get/list', methods=['GET'])
def get_list():
    return jsonify({"data":[["Sam", "Parks","100 Main St."],["Sam", "Parks","100 Main St."],["Sam", "Parks","100 Main St."],["Sam", "Parks","100 Main St."],["Sam", "Parks","100 Main St."],["Sam", "Parks","100 Main St."],["Sam", "Parks","100 Main St."],["Sam", "Parks","100 Main St."],["Sam", "Parks","100 Main St."],["Sam", "Parks","100 Main St."]]}),200


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')