# Définir l'image de base
FROM python:3.7

# Définir le dossier de travail
WORKDIR /ner

# Copier le code source dans le dossier de travail
COPY . /ner

RUN apt-get update && apt-get install -y libsndfile1

# Installer les dépendances Python
RUN pip install --upgrade pandas
RUN pip install --upgrade scikit-learn
RUN pip install --upgrade transformers
RUN pip install --upgrade simpletransformers
RUN pip install --upgrade torch
RUN pip install --upgrade flask
RUN pip install --upgrade flask_cors

# Exécuter le script principal
CMD [ "python", "./prediction.py" ]
