from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/index")
def get_page():
    return render_template("index.html")


@app.post("/index")
def enter_number():
    number = request.form.get("number")

    context = {"number": number, "result": int(number) ** 2}
    return render_template("result.html", **context)


if __name__ == "__main__":
    app.run()
