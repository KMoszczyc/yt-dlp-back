# from yt_dlp_local.yt_dlp.YoutubeDL import YoutubeDL
import yt_dlp
import flask
from flask import request, send_file, jsonify
import os

from flask.cli import load_dotenv
from flask_cors import cross_origin, CORS

load_dotenv()

COOKIE = os.getenv('COOKIE')
app = flask.Flask(__name__)
print('App started and working! Yay!')

@app.route('/wakeup', methods=['GET'])
@cross_origin()
def wake_up():
    """  An endpoint to make sure the flask dyno wakes up with the front on Heroku """
    return jsonify("Yes master, yt-dlp backend is at your service. Just please don't download too much or Youtube will block us. :(")

@app.route('/download', methods=['POST'])
@cross_origin()
def download_yt_song():
    """ Endpoint for downloading mp3's from youtube by yt-dlp """

    content = request.json
    print(content)

    url = content['url'].split('&')[0]
    try:
        os.mkdir(content['sessionDir'])
    except OSError as error:
        print(error)

    dir_path = os.path.join(os.path.abspath(os.getcwd()), 'data', content["sessionDir"])
    final_path = os.path.join(os.path.abspath(os.getcwd()), 'data', content["sessionDir"], 'song.m4a')
    print(final_path)
    ydl_opts = {
        'format': 'bestaudio/best',
        'cookies': COOKIE,
        'outtmpl': os.path.join(dir_path, 'song.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        return send_file(final_path, as_attachment=True)
