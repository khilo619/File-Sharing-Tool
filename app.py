import boto3
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, jsonify, flash, redirect, url_for
from collections import defaultdict

app = Flask(__name__)
app.secret_key = 'WnbXX8NgGMk5W_G6NLeLQTLc9rwrVNb4Nw4SxXyuJ5k'  # Added for flash messages

# AWS S3 Configuration
AWS_BUCKET_NAME = 'thisisbucketname2'
s3_client = boto3.client(
    's3', 
    region_name='us-east-1'
) 

# Allowed file extensions
ALLOWED_EXTENSIONS = {  
    'pdf', 'png', 'jpg', 'jpeg', 'gif', 'bmp', 'txt', 'csv', 'docx', 'xlsx', 'pptx',
    'zip', 'tar', 'rar', '7z', 'mp3', 'wav', 'mp4', 'avi', 'mov', 'html', 'xml'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def categorize_file(filename):
    ext = filename.rsplit('.', 1)[-1].lower()
    if ext in ['pdf']:
        return 'PDF Files'
    elif ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
        return 'Images'
    elif ext in ['mp3', 'wav']:
        return 'Audio'
    elif ext in ['mp4', 'avi', 'mov']:
        return 'Videos'
    elif ext in ['txt', 'csv', 'docx', 'xlsx', 'pptx']:
        return 'Documents'
    elif ext in ['zip', 'rar', 'tar', '7z']:
        return 'Archives'
    elif ext in ['html', 'xml']:
        return 'Web Files'
    else:
        return 'Others'

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(url_for('index'))
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(url_for('index'))
        
        if not allowed_file(file.filename):
            flash('Invalid file type. Allowed types: pdf, png, jpg, txt, zip, mp3, etc.', 'error')
            return redirect(url_for('index'))

        original_filename = secure_filename(file.filename)
        file_extension = original_filename.rsplit('.', 1)[-1].lower()

        # Assign folder based on file extension
        folder = (
            'pdf' if file_extension in ['pdf'] else
            'images' if file_extension in ['jpg', 'jpeg', 'png', 'gif', 'bmp'] else
            'audio' if file_extension in ['mp3', 'wav'] else
            'videos' if file_extension in ['mp4', 'avi', 'mov'] else
            'documents' if file_extension in ['txt', 'csv', 'docx', 'xlsx', 'pptx'] else
            'archives' if file_extension in ['zip', 'rar', 'tar', '7z'] else
            'webfiles' if file_extension in ['html', 'xml'] else
            'others'
        )

        s3_key = f"{folder}/{original_filename}"

        # Upload to S3
        s3_client.upload_fileobj(file, AWS_BUCKET_NAME, s3_key)
        flash(f'File uploaded successfully: {original_filename}', 'success')
        
    except Exception as e:
        flash(f"Error uploading file: {str(e)}", 'error')
    
    return redirect(url_for('index'))

@app.route('/files')
def list_files():
    try:
        response = s3_client.list_objects_v2(Bucket=AWS_BUCKET_NAME)
        files_by_category = defaultdict(list)
        
        if 'Contents' in response:
            for obj in response['Contents']:
                if obj['Key'].endswith('/'):
                    continue
                filename = obj['Key'].split('/')[-1]
                category = categorize_file(filename)
                file_url = f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com/{obj['Key']}"
                files_by_category[category].append({'name': filename, 'url': file_url})
        
        return jsonify(files_by_category)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/delete', methods=['POST'])
def delete_file():
    try:
        data = request.get_json()
        filename = data.get('filename')
        category = categorize_file(filename)
        folder = (
            'pdf' if filename.endswith('.pdf') else
            'images' if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')) else
            'audio' if filename.lower().endswith(('.mp3', '.wav')) else
            'videos' if filename.lower().endswith(('.mp4', '.avi', '.mov')) else
            'documents' if filename.lower().endswith(('.txt', '.csv', '.docx', '.xlsx', '.pptx')) else
            'archives' if filename.lower().endswith(('.zip', '.rar', '.tar', '.7z')) else
            'webfiles' if filename.lower().endswith(('.html', '.xml')) else
            'others'
        )
        
        s3_key = f"{folder}/{filename}"
        s3_client.delete_object(Bucket=AWS_BUCKET_NAME, Key=s3_key)
        return jsonify({'success': True, 'message': f'File {filename} deleted successfully'})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)