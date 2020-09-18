from flask import Flask,request,jsonify
from model import Model

model=Model()

Allowed_extensions = {'txt','dat','doc','pdf'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in Allowed_extensions
app = Flask(__name__)
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error':"File doesn't exist"})
        if not allowed_file (file.filename):
            return jsonify({'error':'File format not supported'})


        try:
            text=file.read()
            sentiment,confidence,probabilities=model.predict(str(text))
            data={
            'text':str(text),
            'sentiment':sentiment,
            'confidence':confidence.item(),
            'probabilities':probabilities
            } 
            return jsonify(data)
        except:
            return {'error':'prediction error'}
