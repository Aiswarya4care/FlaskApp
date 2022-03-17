from flask import Flask, render_template, request
import boto3 #Python SDK for AWS
app = Flask(__name__)  # create an app instance
import os

UPLOAD_FOLDER = "uploads"
BUCKET = "filter-engine"

s3 = boto3.client('s3',
                    aws_access_key_id='AKIASLG5BKZAUK7SI27G',
                    aws_secret_access_key= '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'
                     )
                     
BUCKET_NAME='filter-engine'

@app.route('/')  
def home():
    return render_template("file_upload_to_s3.html")
    

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        s3.upload_file(f"uploads/{f.filename}", BUCKET)
    return render_template("file_upload_to_s3.html")




if __name__ == "__main__":  # create an app instance
    
	app.run(debug=True)  # create an app instance
