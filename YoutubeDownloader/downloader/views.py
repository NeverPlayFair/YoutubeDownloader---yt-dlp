from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import yt_dlp
import imageio_ffmpeg
import os

@csrf_exempt
def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        print(f"[DEBUG] Otrzymany URL: {url}")

        # Usuń np. &t=533s z końca linku
        clean_url = url.split('&')[0]
        print(f"[DEBUG] Oczyszczony URL: {clean_url}")

        # Ścieżka do folderu 'downloads/' w katalogu projektu
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        download_path = os.path.join(BASE_DIR, 'downloads')
        os.makedirs(download_path, exist_ok=True)

        ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mkv',  # kompatybilniejszy niż mp4
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'ffmpeg_location': ffmpeg_path,
            'noplaylist': True,
            'socket_timeout': 30,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            }
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([clean_url])
            print("[DEBUG] Pobieranie zakończone sukcesem (audio + video)")
            return render(request, 'downloader/index.html', {'message': 'Pobrano pomyślnie (wideo + audio).'})
        except Exception as e:
            print(f"[DEBUG] Błąd podczas pobierania: {e}")
            return render(request, 'downloader/index.html', {'error': f'Błąd pobierania: {str(e)}'})

    return render(request, 'downloader/index.html')
