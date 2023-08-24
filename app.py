#from flask import Flask

#app = Flask(__name__)

#@app.route("/")
from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_link = request.form['video_link']
        try:
            yt = YouTube(video_link)
            
            if 'audio' in request.form:
                stream = yt.streams.filter(only_audio=True).first()
                if stream:
                    download_link = stream.url
                else:
                    error_message = "No audio stream available."
                    return render_template('index.html', error_message=error_message)
            else:
                stream = yt.streams.get_highest_resolution()
                if stream:
                    download_link = stream.url
                else:
                    error_message = "No video stream available."
                    return render_template('index.html', error_message=error_message)

            return render_template('index.html', download_link=download_link)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template('index.html', error_message=error_message)
    return render_template('index.html')

#if __name__ == '__main__':
    #app.run(debug=True)


if __name__=="__main__":
    app.run(host="0.0.0.0")
