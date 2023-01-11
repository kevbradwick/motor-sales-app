import pathlib
import pickle

import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)


DATA_DIR = pathlib.Path(__file__).parent.resolve() / "data"

with open(str(DATA_DIR / "2023-01-10_Audi_A3.bin"), "rb") as fp:
    MODEL = pickle.load(fp)


@app.get("/")
def predict():
    mileage = request.args.get("mileage", "")
    year = request.args.get("year", "")

    if not year.isdigit() or not mileage.isdigit():
        return jsonify({"error": "mileage and/or year not set"}), 400

    data = {"mileage": [int(mileage)], "year": int(year)}
    df = pd.DataFrame(data=data)

    result = MODEL.predict(df[["year", "mileage"]])

    return jsonify({"result": result[0]}), 200
