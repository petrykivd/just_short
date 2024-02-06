from flask import (
    Flask,
    render_template,
    request,
    redirect
)

from db.database import SessionLocal
from db.models import Link

from utils.short_link_helper import (
    generate_short_link,
    save_link,
    get_link
)

app = Flask(__name__)

db = SessionLocal()


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        url = request.form["link"]
        short_url, url = generate_short_link(url)
        save_link(url=url, short_url=short_url)
        return redirect(f"/short_links/{short_url}")
    else:
        return render_template("index.html")


@app.route("/short_links/<short_url>", methods=["GET"])
def short_link(short_url):
    new_link = get_link(short_url=short_url, request=request)
    return render_template("short_link.html", new_link=new_link)


@app.route("/<short_url>", methods=["GET"])
def redirect_link(short_url):
    existing_link = db.query(Link).filter_by(short_url=short_url).first()
    if existing_link:
        return redirect(existing_link.url)
    return "Your short link is deactivated"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
