from flask import Flask, render_template, request
from flask_cors import CORS
import googlemaps
app = Flask(__name__)
CORS(app)
gmaps = googlemaps.Client(key='')
#app.config.from_object("constants")

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/recherche', methods=['POST'])
def recherche():
    if request.method == 'POST':
        search = request.form.get('search')

        response = gmaps.geocode(search)

        if search:
            return {'message' : response[0]['formatted_address']}
        else:
            return { "message": "Field 'search' " }, 400

#if __name__ == "__main__":
#    app.run()
