from flask import Flask, request
from simpletransformers.ner import NERModel
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
model = NERModel('bert', "outputs/checkpoint-480-epoch-5/", use_cuda=False)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sentence = data['sentence']
    prediction, model_outputs = model.predict([sentence])

    # Extraire les informations de la prédiction
    entities = {}
    for item in prediction[0]:
        for key, value in item.items():
            if value is not None and value.startswith("B-"):
                if value[2:] not in entities:
                    entities[value[2:]] = key

    # Structurer les informations
    response = {
        'sentence': sentence,
        'start': entities.get('GEOS', ''),
        'end': entities.get('GEOE', '')
    }

    return json.dumps(response)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)


# from flask import Flask, request
# from simpletransformers.ner import NERModel
# from flask_cors import CORS
# import json

# app = Flask(__name__)
# CORS(app)
# model = NERModel('bert', "outputs/checkpoint-340-epoch-5/", use_cuda=False)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     sentence = data['sentence']
#     prediction, model_outputs = model.predict([sentence])

#     # Extraire les villes de départ et d'arrivée à partir des labels "B-geoS" et "B-geoE"
#     start = None
#     end = None
#     for item in prediction[0]:
#         label = item['entity']
#         word = item['word']
#         if label == 'B-geoS':
#             start = word
#         elif label == 'B-geoE':
#             end = word

#     # Structurer les informations
#     response = {
#         'sentence': sentence,
#         'start': start if start is not None else 'Marseille',
#         'end': end if end is not None else ''
#     }

#     return json.dumps(response)


# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5001, debug=True)
