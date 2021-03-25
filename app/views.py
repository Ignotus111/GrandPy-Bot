from flask import Flask, render_template, request
from app.apis.api_wiki_media import ApiWiki
from app.apis.api_google_map import ApiGoogle

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    """
    When index page is call, render html template.
    """
    return render_template("index.html")


@app.route("/research", methods=["POST"])
def research():
    """
    When research is called, take script.js data, creates ApiGoogle object with
    it then an ApiWiki object then return wanted params.
    """
    if request.method == "POST":
        search = request.form.get("search")
        answer = ApiGoogle(search)
        story = ApiWiki(answer.wiki)
        if search:
            return {
                "address": answer.address,
                "geocode_lat": answer.latitude,
                "geocode_lng": answer.longitude,
                "story": story.result,
            }
        else:
            return {"message": "Field 'search' "}, 400
