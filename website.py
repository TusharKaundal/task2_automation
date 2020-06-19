from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<name>/")
def home(name):
        return render_template("index.html",content=name)
@app.route("/")
def defaulthome():
        return render_template("index.html",content='Tushar Kaundal')
if __name__ == "__main__" :
     app.run(debug=True,host='0.0.0.0')
