import os
from flask import Flask
from flask import render_template
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)


@app.route("/")
def main():
    client = MongoClient("mongodb+srv://ayutrisna:ayu123@cluster0-kbkau.mongodb.net/test?retryWrites=true")

    db = client.tes
    collection = db.tes
    cursor = collection.find({})

    result = ""

    for tes in cursor:
        result += tes["nama"]
        result += "\n"
        result += tes["nim"]
        result += "\n"
        result += "\n"

    return render_template("index.html", data=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
