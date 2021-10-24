# from yt_dlp_local.yt_dlp.YoutubeDL import YoutubeDL
import yt_dlp
import flask
from flask import request, send_file, jsonify
import os
from flask_cors import cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True
print('App started and working! Yay!')

@app.route('/wakeup', methods=['GET'])
@cross_origin()
def wakeUp():
    """  An endpoint to make sure the flask dyno wakes up with the front on Heroku """

    return jsonify("Yes master, I'm awake.")

@app.route('/download', methods=['POST'])
@cross_origin()
def downloadYTSong():
    """ Endpoint for downloading mp3's from youtube by yt-dlp """

    content = request.json
    print(content)

    url = content['url'].split('&')[0]
    try:
        os.mkdir(content['sessionDir'])
    except OSError as error:
        print(error)

    path = f'{content["sessionDir"]}song.webm'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{content["sessionDir"]}song.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        return send_file(path, as_attachment=True)
