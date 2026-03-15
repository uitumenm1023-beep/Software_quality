from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# LANDING PAGE
@app.route("/", methods=["GET", "POST"])
def landing():

    if request.method == "POST":
        name = request.form["name"]

        return redirect(url_for("bmi_page", name=name))

    return render_template("index1.html")


# BMI PAGE
@app.route("/bmi", methods=["GET", "POST"])
def bmi_page():

    username = request.args.get("name", "Guest")

    result = None
    bmi = None
    error = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height_cm = float(request.form["height"])

            if weight <= 0 or height_cm <= 0:
                error = "Height and weight must be greater than 0."
            else:
                height_m = height_cm / 100
                bmi = weight / (height_m ** 2)
                bmi = round(bmi, 2)
                result = get_bmi_status(bmi)

        

        except ValueError:
            error = "Please enter valid numbers."

    return render_template(
        "index.html",
        username=username,
        result=result,
        bmi=bmi,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)