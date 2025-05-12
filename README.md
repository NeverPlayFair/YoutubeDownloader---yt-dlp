YouTube Video Downloader (Audio + Video, MKV Format)

A browser-based YouTube video downloader built with Django and yt-dlp, designed for downloading high-quality audio + video directly to a server-local "downloads/" folder.
No system-wide ffmpeg needed — fully self-contained using imageio-ffmpeg.

## FEATURES

Paste any YouTube link and download full video

Audio + video merged into .mkv file

Files saved locally to downloads/ folder inside the Django project

Uses ffmpeg automatically without installing it system-wide

Cleans up URL params like &t=... or &list=...

Runs fully in your browser (no JavaScript required)

## TECH STACK

Django – Python Web Framework

yt-dlp – Robust YouTube/media downloader

ffmpeg – Required for stream merging (used via Python)

imageio-ffmpeg – Provides ffmpeg binary automatically

HTML/CSS – Minimal user interface

## REQUIREMENTS

Python 3.9+ or Anaconda

Internet connection (for downloads)

Optional: Git

## ENVIRONMENT SETUP (using Anaconda)

conda create --name DownloadEnv python=3.10
conda activate DownloadEnv

Install Python dependencies:

pip install django yt-dlp imageio-ffmpeg

## RUNNING THE PROJECT

Run Django migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

Paste a YouTube video URL and click Download.


## Demo
![image](https://github.com/user-attachments/assets/6e6cfd34-6f53-40b6-a5d6-875397ca7195)
![image](https://github.com/user-attachments/assets/c307e157-0556-49d1-94d3-a2ecd730f98f)
![image](https://github.com/user-attachments/assets/17af10e2-9e89-42c3-85f2-354a68476262)

