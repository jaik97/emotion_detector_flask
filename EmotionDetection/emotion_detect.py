import requests #Import the requests library to handle the HTTPS requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} #Set the headers required for the API request
    myobj = { "raw_document": { "text": text_to_analyse } } #Create a dictionary with the text to be analysed
    response = requests.post(url, json = myobj, headers = header) # Send a POST requests to the text and headers
    
    #formatting the response recieved
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        #finding the score of each emotion from the json response
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        #To find the domoninant emotion create a dictonary of the emotions and find the highest key value
        emotions = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
                    'joy': joy_score, 'sadness': sadness_score}

        dominant_emotion_name = max(zip(emotions.values(), emotions.keys()))[1]

        final_response = emotions
        final_response['dominant_emotion'] = dominant_emotion_name
    elif response.status_code == 400:
        final_response = {'anger': None, 'disgust': None, 'fear': None,
                    'joy': None, 'sadness': None, 'dominant_emotion': None}

    #Return the final_response
    return final_response