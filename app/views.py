from flask import Flask, render_template, request
import googlemaps

app = Flask(__name__)

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
            return {'address' : response[0]['formatted_address'],
            'geocode_lat': response[0]['geometry']['location']['lat'],
            'geocode_lng': response[0]['geometry']['location']['lng']
            }
        else:
            return { "message": "Field 'search' " }, 400

#if __name__ == "__main__":
#    app.run()
