from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")
@app.route("/19th century")
def twenty():
	return render_template("19th.html")
@app.route("/20th century")
def real_twenty():
	return render_template("20th.html")
@app.route("/21st century")
def first():
	return render_template("21sr.html")
@app.route("/contact")
def con():
	return render_template("contact.html")
@app.route("/timeline")
def time():
	return render_template("timeline.html")

@app.route("/Learn All")
def button():
	return render_template("learnmore.html")

@app.route("/About")
def colbo():
	return render_template("About.html")
@app.route("/Evolvement")
def ev():
	return render_template("evolve.html")





if __name__ == "__main__":
	app.run(debug=True)