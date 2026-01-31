from flask import Flask, render_template
import os

app = Flask(__name__)

print("STATIC FOLDER PATH:", app.static_folder)
print("TEMPLATE FOLDER PATH:", app.template_folder)
print("CURRENT WORK DIR:", os.getcwd())

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
