from flask import Flask, render_template, request
from EmotionDetection.emotion_detect import emotion_detector

app = Flask("Emotion Detector Application")

@app.route('/emotionDetector')
def emo_detect():
    """
    This code recieved the text from the HTML interface and
    runs emotion detector over it using emotion_detector() 
    function. The output return shows the various emotions 
    and their confidence score along with the most dominant 
    emotion.
    """

    #Retrieve the text to analyze from the request argument
    text_to_analyse = request.args.get('textToAnalyze')

    #Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyse)

    #Extract the emotions from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    else:
        #Return the response of the list of emotions
        response = f"For the given statement, the system response is 'anger':{anger_score}, 'digust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
        return response

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application 
    page over the Flask channel
    '''

    return render_template('index.html')

if __name__=="__main__":
    '''
    This function executes the flask app and deploys it on the localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)