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

# Exposer le port sur lequel Flask s'exécute
EXPOSE 5000

# Définir la variable d'environnement pour Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Commande pour démarrer l'application Flask
CMD ["flask", "run"]