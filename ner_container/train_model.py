import pandas as pd
from simpletransformers.ner import NERModel

def train_new_model(new_data_path, model_dir):
    # Charger les nouvelles données à partir du fichier
    new_data = pd.read_csv(new_data_path)

    # Instancier un nouveau modèle de NER
    model = NERModel('bert', model_dir)

    # Re-entraîner le modèle avec les nouvelles données
    model.train_model(new_data)

    # Sauvegarder le modèle entraîné
    model.save_model()

if __name__ == "__main__":
    new_data_path = "new_data.csv" # chemin du fichier de données
    model_dir = "best_model/" # chemin du dossier de modèle sauvegardé

    train_new_model(new_data_path, model_dir)
