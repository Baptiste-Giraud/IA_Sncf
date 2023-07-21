# Spécifier l'image de base
FROM python:3.8

# Copier le code dans le conteneur Docker
COPY . /speech

# Définir /speech comme répertoire de travail
WORKDIR /speech

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir pydub soundfile huggingsound Flask flask-cors datasets jiwer

# Installer les dépendances spécifiques à libsndfile
RUN apt-get update && apt-get install -y libsndfile1

# Définir la commande pour exécuter le code
CMD ["python", "main.py"]
