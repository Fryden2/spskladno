from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/1")
def home():
    return "Hello World!"

@app.route("/2")
def pozdrav_ze_souboru():
    return render_template("pozdrav.html")

@app.route("/3")
def pozdrav_ze_souboru_CSS():
    return render_template("pozdrav_CSS.html")

@app.route("/4")
def pozdrav_s_promenou():
    return render_template("pozdrav_promnena.html", message = "Čau světe!")

@app.route("/5")
def pozdrav_img():
    image_url = url_for('static', filename='images/obrázek.jpg')
    return render_template("pozdrav_image.html", image_url=image_url)

@app.route("/6", methods=["GET", "POST"])
def prvniformularcislo():
    result = None
    if request.method == "POST":
        number = request.form.get("number", type=int)
        if number is not None:
            result = number + 1
    return render_template("formular_cislo.html", result=result)

if __name__ == "__main__":
    app.run()