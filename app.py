from flask import Flask, abort,render_template, session,request, redirect, url_for,jsonify,Blueprint
import os


app = Flask(__name__)

        
# Api pour afficher la page index
@app.route("/", methods=["POST","GET"])
def index():
    return render_template("index.html")


# Api pour gerer les fichier
@app.route("/fichier", methods=["POST","GET"])
def fichier():
    return render_template("fichier.html")


# Api pour gerer les types de nutrition 
@app.route("/phylum", methods=["POST","GET"])
def phylum():
    return render_template("phylum.html")
    
    
if __name__ == "__main__":
    app.run( debug=True)

