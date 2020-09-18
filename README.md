# Sentiment analysis predictor using Pytorch
In this project, the sentiment of the reviews is predicted with [BERT](https://huggingface.co/transformers/model_doc/bert.html) transformer using Pytorch framework & deployed Bert model as a **REST API** using **Flask**.

**BERT** is a **B**idirectional **E**ncoding **R**epresentations from **T**ransformers. It’s a bidirectional transformer pre-trained using a combination of masked language modeling objective and next sentence prediction on a large corpus comprising the Toronto Book Corpus and Wikipedia. It is simple & extremly powerful & open sourced by the team at [HuggingFace](https://huggingface.co/).

Dataset has been created for Sentiement Analysis by scraping user reviews for Android apps using Python. This dataset contains user reviews for top 30 free Google play apps in India as of today. Google play scraper is used for this task.

**Deploy BERT Sentiment model using Flask as a Rest API**
The model is trained to classify sentiment (positive,negative) on scraped apps review data from Google play store.
Here is a sample request to the API:

requests.post('http://localhost:5000/predict', files = { 'file': open('review.txt','r')})

If text in the review file has positive sentiment then,Here is the response from API looks like: 

 {                   
 "confidence": 0.9956058859825134,          
  "probabilities": {                   
                "negative": 0.004394036252051592,                  
                "positive": 0.9956058859825134                  
  },                       
  "sentiment": "positive",            
  "text": "b'OMG. I love how easy it is to stick to my schedule. Would recommend to everyone!'"         
}

If text in the review file has negative sentiment, then here is the API response looks like:

{                                         
  "confidence": 0.9994189739227295,          
  "probabilities": {                         
    "negative": 0.9994189739227295,                       
    "positive": 0.0005810490692965686                    
  },          
  "sentiment": "negative",        
  "text": "b'This is a worst app ever used. I will uninstall this app immediately.'
}

**Installation** 

Clone this repo:     

git clone git@github.com:ramachandra742/NLP-projects.git
cd NLP-projects/End-End-Sentiment-analysis-predictor-using-Pytorch  

Install the dependencies: 

pip install -r requirements.txt

Download the pre-trained BERT model:

[Sentiment_Analysis_Bert.pt](https://drive.google.com/file/d/1-2LP_F3s9g_dlTrYrb7ZAQH6lhGn3bzb/)

**Test Setup**

Start Flask development server:

$ export FLASK_APP=predict.py      
$ export FLASK_ENV=development       
$ flask run

Send request to API:

requests.post('http://localhost:5000/predict', files = { 'file' : open('review.txt','r')})

**License**

MIT


