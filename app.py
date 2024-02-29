from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template("base.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080,   debug=True)
