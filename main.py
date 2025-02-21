from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
  cDate = datetime.today()
  return f'Today is {cDate}'


@app.route("/contatos")
def contatos():
  return "Contatos"


@app.route("/sobre")
def sobre():
  return "Sobre"


@app.route("/quem-somos")
def quemSomos():
  return "Quem somos"


if __name__ == "__main__":
  app.run(host='0.0.0.0')
