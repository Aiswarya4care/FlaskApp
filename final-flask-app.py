from flask import Flask, render_template, request
import os
import boto3 #Python SDK for AWS
app = Flask(__name__)  # create an app instance
from werkzeug.utils import secure_filename


s3 = boto3.client('s3',
                    aws_access_key_id='AKIASLG5BKZAUK7SI27G',
                    aws_secret_access_key= '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'
                     )
                     
BUCKET_NAME='filter-engine'

@app.route('/')  
def home():
    return render_template("file_upload_to_s3.html")
    
@app.route('/upload',methods=['post'])

def upload():
    
    # If user has submitted the form...
    if request.method == "POST":
        files = request.files.getlist("file")
        
        for f in files:
            if files:
                filename = secure_filename(f.filename)
                f.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                os.remove(os.getcwd()+"/"+filename)
                     
        msg = "Upload Done ! "
		
    return render_template("file_upload_to_s3.html",msg =msg)




if __name__ == "__main__":  # create an app instance
    
	app.run(debug=True)  # create an app instance
