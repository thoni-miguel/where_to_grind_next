from flask import Flask, jsonify
from flask_cors import CORS
from get_data_from_wowhead import return_data, save_info
import json

app = Flask(__name__)
CORS(app)

@app.route('/getinfo')
async def get_info():
    with open('data.json', 'r') as json_file:
        info = json.load(json_file)
    return info

@app.route('/loadinfo')
async def load_info():
    await save_info()
    return {
        "sucess": "true"
    }

@app.route('/')
def home():
    return {
        "hello":"there"
    }



if __name__ == "__main__":
    app.run(debug=True)