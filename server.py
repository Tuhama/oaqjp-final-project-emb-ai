"""
Module for the Emotion Detection Flask application.
This module provides an interface to analyze text for emotional content
using the EmotionDetection library.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyzes the provided text from the request arguments and returns
    a formatted string with emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Get the emotion dictionary from the detector
    response = emotion_detector(text_to_analyze)

    # Handle cases where the input might be invalid or empty
    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Return a formatted string instead of a raw dictionary for the UI
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index.html page for the application home route.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
