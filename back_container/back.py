from flask import Flask, request
from flask_cors import CORS
import requests
import mysql.connector as sql
import html

app = Flask(__name__)
CORS(app)

conn = sql.connect(
  host="db",
  user="ia",
  password="pass",
  database="ia",
  charset="utf8mb4"
)

def get_stop_id(city_start, city_end):
    cursor = conn.cursor()
    cursor.execute("""SELECT stop_id, stop_name FROM stops WHERE stop_name LIKE %s and stop_id LIKE %s""", ("%" + city_start + "%", "%StopPoint:OCETrain%"))
    start_gare = cursor.fetchall()

    cursor.execute("""SELECT stop_id, stop_name FROM stops WHERE stop_name LIKE %s and stop_id LIKE %s""", ("%" + city_end + "%", "%StopPoint:OCETrain%"))
    end_gare = cursor.fetchall()
    return {"start": start_gare, "end": end_gare}

<<<<<<< HEAD
@app.route("/send-audio", methods=["POST"])
def receive_audio():
    audio = json.loads(request.get_data())
=======
def id_to_city(result_data):
    cursor = conn.cursor()
    sql = 'SELECT stop_id, stop_name FROM stops WHERE stop_id IN ({})'.format(','.join(['%s']*len(result_data)))
    cursor.execute(sql, result_data)
    gare_list = cursor.fetchall()
    gares = {id: name for id, name in gare_list}
    gare_list = [gares[id] for id in result_data]
    return gare_list

# def id_to_city(result_data):

#     cursor = conn.cursor()
#     sql = 'SELECT stop_name FROM stops WHERE stop_id IN ({})'.format(','.join(['%s']*len(result_data)))
#     cursor.execute(sql, result_data)
#     gare_list = [row[0] for row in cursor.fetchall()]
#     return gare_list

@app.route("/send-audio", methods=["GET"])
def receive_audio():
    transcription = request.args.get('destination')
>>>>>>> docker
    # Appel de Wave2vec
    # headers = {'Content-Type': 'application/octet-stream'}
    # response = requests.post("http://speech_service:8002/audio", headers=headers, data=audio)
    # return response.text
    # Appel du NER

    headers = {'Content-Type': 'application/json'}
<<<<<<< HEAD
    data = {'sentence': str(audio["destination"])}
    cities = requests.post("http://ner_service:5001/predict", headers=headers, json=data)
    return cities.json()
=======
    data = {'sentence': transcription}
    prediction = requests.post("http://ner_service:5001/predict", headers=headers, json=data).json()
    prediction["end"] = "Agde"
    prediction["start"] = "Marseille"
>>>>>>> docker

    stop_list = get_stop_id(prediction["start"], prediction["end"])
    #MODIFIER POUR GERER LES DEUX LISTES EN MEME TEMPS
    if not stop_list:
        return {"error": "No trainstation founded"}

    gare_depart = stop_list["start"][0][0]
    gare_arrive = stop_list["end"][0][0]
    # return {"start": gare_depart, "end": gare_arrive}
    result_data = requests.get("http://graph:8001/shortest_path?gare_depart=" + gare_depart + "&gare_arrive=" + gare_arrive).json()
    # return {"msg": result_data["result"]}
    gare_list = id_to_city(result_data["result"])
    return {"gares": gare_list, "time": result_data["time"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
