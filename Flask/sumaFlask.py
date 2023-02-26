from flask import *

# Autor: Jesus Angel Juarez Zazueta

app = Flask(__name__)
app.secret_key="SaikoBall18"

@app.route("/", methods=["POST","GET"])
def index():
    a=0
    b=0
    r=0
    if request.method == "POST":
        try:
            a = int(request.form["a"])
            b = int(request.form["b"])
            r = a+b
        except:
            r = "No se puede"
    return render_template('./index.html',a=a,b=b,resultado=r)

if __name__ == "__main__":
    app.run(debug=True)