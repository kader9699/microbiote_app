# Utiliser une image Python de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt ./
COPY app.py ./
COPY model.py ./
COPY templates/ ./templates/
COPY static/ ./static/
COPY Fichier/ ./Fichier/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port Flask (par défaut 5000)
EXPOSE 5000

# Commande pour démarrer l'application avec Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
