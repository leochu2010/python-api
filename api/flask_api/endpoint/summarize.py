from flask import Blueprint, request
from api.flask_api.service.text_rank import TextRank


summarize_apis = Blueprint("summarize_apis", __name__)
text_rank = TextRank()

@summarize_apis.route('/api/textrank', methods=['POST'])
def get_text_rank():
    text = request.form['text']
    summary = text_rank.get_highest_rank(text, 3)
    return '\n'.join(summary)

