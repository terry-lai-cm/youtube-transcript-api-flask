from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

app = Flask(__name__)

@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    lang_list = ['zh-TW', 'zh-Hant', 'zh', 'en']  # 語言優先順序
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=lang_list)
        return jsonify(transcript)
    except NoTranscriptFound:
        return jsonify({'error': 'No transcript found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
