import requests
import json

# Sending a POST request to the sentiment analysis API
response = requests.post(url, json=myobj, headers=header)

# Parsing the JSON response from the API
formatted_response = json.loads(response.text)

emotions = formatted_response['emotionPredictions'][0]['emotion']
anger_score = emotions['anger']
disgust_score = emotions['disgust']
fear_score = emotions['fear']
joy_score = emotions['joy']
sadness_score = emotions['sadness']

# Find the emotion with the highest score
dominant_emotion = max(emotions, key=emotions.get)

return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
}