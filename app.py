from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def first_project():
  return render_template("home.html")

@app.route("/", methods=["GET", "POST"])
def predicting():
  if request.method == "POST":
    input_data = [
        request.form.get("REGION-CENTROID-COL"),
        request.form.get("REGION-CENTROID-ROW"),
        request.form.get("REGION-PIXEL-COUNT"),
        request.form.get("SHORT-LINE-DENSITY-2"),
        request.form.get("VEDGE-MEAN"),
        request.form.get("VEDGE-SD"),
        request.form.get("HEDGE-MEAN"),
        request.form.get("HEDGE-SD"),
        request.form.get("INTENSITY-MEAN"),
        request.form.get("RAWRED-MEAN"),
        request.form.get("RAWBLUE-MEAN"),
        request.form.get("RAWGREEN-MEAN"),
        request.form.get("EXRED-MEAN"),
        request.form.get("EXBLUE-MEAN"),
        request.form.get("EXGREEN-MEAN"),
        request.form.get("VALUE-MEAN"),
        request.form.get("SATURATION-MEAN"),
        request.form.get("HUE-MEAN")
    ]
    prediction = predict(input_data)
    return render_template("home.html", prediction_text=prediction)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
