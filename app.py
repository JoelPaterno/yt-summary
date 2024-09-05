from flask import Flask, render_template, request, session
from apitest import get_summary
from transcript import get_transcript

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form["url"]
        length = request.form["length"]
        id = url.split("v=", 1)[1]
        transcript = get_transcript(id)
        script = ""
        for dict in transcript:
            script += dict["text"]
        summary = get_summary(url=url, length=length, html=script)
        return render_template("summary.html", url=url, summary=summary)
    else:
        return render_template("index.html")

if  __name__ == "__main__":
    app.run(debug=True)