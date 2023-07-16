from googleapiclient.discovery import build

# Remplacez "YOUR_API_KEY" par votre propre clé d'API YouTube
api_key = "AIzaSyAbdxP65syXSB44odPu5-4DAIGvEbddKNg"

# Initialise l'objet service pour l'API YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

# Identifiant de la playlist
playlist_id = 'PLZ8uoFzxdIgUvin6bM5u4hnG1aufKgZmN'

# Récupère les vidéos de la playlist
playlist_items = youtube.playlistItems().list(
    part='contentDetails',
    playlistId=playlist_id,
    maxResults=50  # Nombre maximal de vidéos à récupérer par requête (max 50)
).execute()

# Parcourt chaque vidéo de la playlist
for item in playlist_items['items']:
    video_id = item['contentDetails']['videoId']
    video_url = f'https://youtu.be/{video_id}'
    print(video_url)
