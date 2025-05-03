# from flask import Flask, request, jsonify
# from utils.detection import predict_phishing  # This function should load your model and return a prediction

# app = Flask(__name__)

# @app.route('/detect', methods=['POST'])
# def detect():
#     # Parse the incoming JSON data
#     data = request.get_json()
#     url = data.get('url')
    
#     if not url:
#         return jsonify({'error': 'No URL provided'}), 400
    
#     try:
#         # Call the prediction function to get the phishing status.
#         # The predict_phishing function should return a dictionary like {'isPhishing': True/False}
#         prediction = predict_phishing(url)
#         return jsonify(prediction)
#     except Exception as e:
#         # If there's an error, return it in the response.
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     # Run the Flask app on port 5000 in debug mode for development.
#     app.run(debug=True, port=5000)

import sys
import os
import traceback
# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify, render_template, url_for
from utils.detection import predict_phishing

app = Flask(__name__)

@app.route('/detect', methods=["POST"])
def detect():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    
    try:
        prediction = predict_phishing(url)
        if prediction.get('isPhishing'):
            # Build the redirect URL (e.g., /phishy) with query parameters
            redirect_url = url_for('phishy_page', 
                                   url=url,
                                   message=prediction.get('message', 'No message available.'),
                                   confidence=prediction.get('confidence', 'N/A'))
            return jsonify({
                'redirect': redirect_url,
                'url': url,
                'message': prediction.get('message'),
                'confidence': prediction.get('confidence')
            })
        else:
            return jsonify(prediction)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/phishy')
def phishy_page():
    url = request.args.get('url', 'N/A')
    message = request.args.get('message', 'No message available.')
    confidence = request.args.get('confidence', 'N/A')
    return render_template('phishy.html', url=url, message=message, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
