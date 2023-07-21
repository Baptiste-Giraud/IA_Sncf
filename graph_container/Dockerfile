# Spécifier l'image de base
FROM python:3.8

# Copier le code dans le conteneur Docker
COPY . /graph

# Définir /app comme répertoire de travail
WORKDIR /graph

# Installer les dépendances nécessaires
RUN pip install pandas networkx flask flask_cors

# Définir la commande pour exécuter le code
CMD ["python", "main.py"]
