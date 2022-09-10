from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '78fabf5575579bcb76daea4131c8b06f8d41462b08850e3f'

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about/")
def about_page():
    return render_template("about.html")

@app.route("/result/", methods=['POST', 'GET'])
def potability_calc():
    if request.method == "POST":
        ph = request.form["ph"]
        hard = request.form["hardness"]
        solid = request.form["solids"]
        chamine = request.form["chloramines"]
        sulfate = request.form["sulfate"]
        cond = request.form["conductivity"]
        oc = request.form["oc"]
        thm = request.form["trihalomethanes"]
        turb = request.form["turbidity"]
        
        context = {"ph": ph, "hard": hard, "solid": solid, "chamine": chamine, "sulfate": sulfate, "cond": cond, "oc": oc, "thm": thm, "turb": turb}

        return render_template("results.html", context=context)
    else:
        return redirect("/")
        
        


if  __name__ == "__main__":
    app.run(debug=True)