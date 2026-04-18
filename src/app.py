from flask import Flask, jsonify, request, render_template, Response, stream_with_context, send_file
from flask_cors import CORS
import json
import getPython as gP
import io
app = Flask(__name__)
# allow requests from multiple origins.
CORS(app)

@app.route("/")
def initial():
    return render_template("app.html")

# get the get request/get text from the response. 
# create a get request for a webpage, and then generate the pdf.
@app.route("/getWebpage", methods=['POST'])
def getW():
    response = request.get_json()
    list = gP.getPrompt(response)
    jsonObj = {"link": list[0], "text": list[1]}
    jsonResult = jsonify(json.dumps(jsonObj))
    return jsonResult

@app.route("/fetch-page", methods=['POST'])
def fetch_page():
    data = request.get_json()
    url = data.get('url', '').strip()
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    try:
        from weasyprint import HTML
        pdf_bytes = HTML(url=url).write_pdf()
        return send_file(
            io.BytesIO(pdf_bytes),
            mimetype='application/pdf',
            as_attachment=True,
            download_name='fetched-page.pdf'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/chatMessage", methods=["POST"])
def chat_message():
    data = request.get_json()
    try:
        chat_history = data.get("chatHistory", [])

        def generate():
            stream = gP.getChatResponse(chat_history)

            for chunk in stream:
                content = chunk.get("message", {}).get("content", "")
                if content:
                    yield content

        return Response(
            stream_with_context(generate()),
            content_type="text/plain; charset=utf-8"
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
