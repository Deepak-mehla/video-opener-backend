from flask import Flask, request, redirect
import subprocess

app = Flask(__name__)

@app.route("/process")
def process():
    video_url = request.args.get("video")
    if not video_url:
        return "No video URL", 400

    try:
        cmd = [
    "yt-dlp",
    "-f", "bv*[ext=mp4]/best[ext=mp4]/best",
    "-g",
    video_url
]

        stream_url = subprocess.check_output(cmd).decode().strip()
        return redirect(stream_url)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
