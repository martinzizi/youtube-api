#https://www.youtube.com/@andrenavarroII/videos
#https://www.youtube.com/channel/UCv5OAW45h67CJEY6kJLyisg

import os
import random
from youtube_api_key import api_key
from googleapiclient.discovery import build


# ID de la chaîne YouTube pour laquelle vous voulez récupérer les videos
channel_id = "enter_id_here"

# Nombre total de vidéos à récupérer
num_videos = 100

# Nombre de vidéos par requête (maximum : 50)
videos_per_request = 50

# Calculer le nombre total de requêtes nécessaires
num_requests = (num_videos + videos_per_request - 1) // videos_per_request


youtube = build("youtube", "v3", developerKey=api_key)


video_urls = []

# Effectuer les requêtes en paginant les résultats
for request_num in range(num_requests):
    search_response = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=videos_per_request,
        pageToken="" if request_num == 0 else next_page_token
    ).execute()

    # Extraire les IDs de vidéo
    video_ids = [item['id']['videoId'] for item in search_response['items'] if item['id']['kind'] == 'youtube#video']

    # Générer les URLs des vidéos
    video_urls.extend([f"https://youtu.be/{video_id}" for video_id in video_ids])
    next_page_token = search_response.get('nextPageToken')

    # Arrêter la boucle si on a atteint le nombre total de vidéos
    if len(video_urls) >= num_videos:
        break

# Écrire les URLs dans un fichier texte
with open("output.txt", "w") as file:
    for url in video_urls:
        file.write(url + "\n")

# Afficher un message de confirmation
print("Les URLs ont été enregistrées dans le fichier output.txt.")