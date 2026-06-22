from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/deity")
def deity():
    return render_template("deity.html")

@app.route("/timings")
def timings():
    return render_template("timings.html")

@app.route("/aarti")
def aarti():
    return render_template("aarti.html")

@app.route("/chalisa")
def chalisa():
    return render_template("chalisa.html")

@app.route("/mantras")
def mantras():
    return render_template("mantras.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/videos")
def videos():
    return render_template("videos.html")

@app.route("/donation")
def donation():
    return render_template("donation.html")

@app.route("/trust")
def trust():
    return render_template("trust.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)