import shutil

from yt_dlp_local.yt_dlp.YoutubeDL import YoutubeDL
import flask
from flask import request, jsonify, send_file, after_this_request
import os


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/download', methods=['POST'])
def predictTextSentiment():
    content = request.json
    print(content)

    url = content['url'].split('&')[0]
    try:
        os.mkdir(content['sessionDir'])
    except OSError as error:
        print(error)


    path = f'{content["sessionDir"]}/song.webm'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{content["sessionDir"]}/song.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        return send_file(path, as_attachment=True)


