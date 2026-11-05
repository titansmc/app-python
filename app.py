import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def inici():
    missatge = os.environ.get("MISSATGE", "Falta definir la variable MISSATGE")
    return f"<h1>{missatge}</h1>\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
