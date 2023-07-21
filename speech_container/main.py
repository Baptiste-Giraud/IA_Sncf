from huggingsound import SpeechRecognitionModel
from datasets import load_dataset, load_metric, Audio, Dataset
from difflib import SequenceMatcher
import soundfile as sf
from flask import Flask, request
from flask_cors import CORS
import os



app = Flask(__name__)
CORS(app)
model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-french")

@app.route("/audio", methods=["POST"])
def receive_audio():
    audio = request.get_data()
    with open("record.wav", "wb") as f:
        f.write(audio)
    
    while not os.path.exists("record.wav"):
        pass

    transcriptions = model.transcribe(["record.wav"])
    transcription = transcriptions[0]["transcription"].title()
    return transcription




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
# print("Wer:", jiwer.wer(data.lower(), stock[0].lower()))
# print("Mer:", jiwer.mer(data.lower(), stock[0].lower()))
# print("Wil:", jiwer.wil(data.lower(), stock[0].lower()))