from flask import Flask, render_template, request, session
from apitest import get_summary
from webscraper import scrape_website, extract_body_content, clean_body_content

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form["url"]
        length = request.form["length"]
        summary = get_summary(url=url, length=length)
        webpage = scrape_website(url)
        webpage = extract_body_content(webpage)
        webpage = clean_body_content(webpage)
        return render_template("summary.html", url=url, summary=summary, html=webpage)
    else:
        return render_template("index.html")

if  __name__ == "__main__":
    app.run(debug=True)