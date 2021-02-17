from flask import Flask, render_template, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#app.config.from_object("constants")

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/recherche', methods=['POST'])
def recherche():
    if request.method == 'POST':
        search = request.form.get('search')

        # comprendre search

        # appel a l'api de google map

        # quand resultat retourner le resultat
        if search:
            return { 'message': '75001 Paris' }
        else:
            return { "message": "Field 'search' " }, 400

#if __name__ == "__main__":
#    app.run()
