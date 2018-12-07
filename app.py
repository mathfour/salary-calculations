from flask import Flask, redirect, request, render_template, url_for
from processing import do_calculation

app = Flask(__name__)
# app.config["DEBUG"] = True
comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('comments_page.html', comments=comments)

    # elif request.method == 'POST':
    comments.append(request.form["contents"])
    return redirect(url_for('index'))


@app.route("/adder", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])
        if number1 is not None and number2 is not None:
            result = do_calculation(number1, number2)
            return render_template('results_page.html', result = result)
    return render_template('adder_page.html', errors=errors)

if __name__ == '__main__':
    app.run(debug=True)