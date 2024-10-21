from flask import Flask, abort,render_template, flash,session,request, redirect, url_for,jsonify,Blueprint
import os
from model import FileManager
from werkzeug.utils import secure_filename



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'Fichier')
app.config['ALLOWED_EXTENSIONS'] = {'xls', 'xlsx', 'csv'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
app.secret_key = "t0pS3cr3t!2024" 

def allowed_file(filename):
    """
    Vérifie si le fichier a une extension autorisée.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
        
# Api pour afficher la page index
@app.route("/", methods=["POST","GET"])
def index():
    return render_template("index.html")


# Api pour gerer les fichier
@app.route("/fichier", methods=["POST","GET"])
def fichier():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('Aucun fichier sélectionné')
            return redirect(request.url)

        file = request.files['file']
        
        if file.filename == '':
            flash('Aucun fichier sélectionné')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)
            # Garde le fichier dans la session
            session['file_path'] = file_path
            file_manager = FileManager(file_path)
            file_manager.load_data()
            data = file_manager.Extraction_data_Phylum('Bacteroidetes')   
            return redirect(request.url)

    return render_template("fichier.html")


# Api pour gerer les types de nutrition 
@app.route("/analyse", methods=["POST","GET"])
def analyse():
    #session.clear()
    file_manager = FileManager(session['file_path'])
    file_manager.load_data()
    bacterie_labels,phylum_labels,nutriment_labels = file_manager.Get_Select_Name()
    if request.method == "POST":
        if 'file_path' not in session:
            flash('Veuillez d\'abord soumettre un fichier avant de faire une recherche.')
            return redirect(url_for('analyse'))   
        phylum = request.form['phylum']  
        bacterie = request.form['bacterie']
        nutriment = request.form['nutriment']
        type = request.form['type']
        print(phylum,nutriment,bacterie,type)
        data = file_manager.Get_Data(bacterie,phylum,nutriment,type)
        # Convertir le DataFrame en une liste de dictionnaires
        data_dict = data.to_dict(orient='records')
        return render_template("analyse.html",data = data_dict,bacterie_labels=bacterie_labels,phylum_labels=phylum_labels,nutriment_labels=nutriment_labels)
    return render_template("analyse.html",bacterie_labels=bacterie_labels,phylum_labels=phylum_labels,nutriment_labels=nutriment_labels)
    
    
if __name__ == "__main__":
    app.run( debug=True)

