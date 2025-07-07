# FileSharing tool

A modern, user-friendly web application for uploading, browsing, downloading, and deleting files, powered by Flask.

---

## Features

- **Drag & Drop File Upload**
- **Category Browsing** (PDFs, Images, Audio, Videos, Documents, Archives, Web Files, Others)
- **Download & Delete Files**
- **Responsive UI** (Tailwind CSS, Font Awesome)
- **AWS S3 Storage** (secure, scalable cloud storage)

---

## Demo

[▶️ Watch the Demo Video on Google Drive](https://drive.google.com/file/d/1enLu2fE_hrCS6RH1p5p4osS60gMrY_TZ/view?usp=drive_link)

---

## Screenshots

**Main Page**  
![Main Page](screen-shots/main%20page.PNG)

**All Files**  
![All Files](screen-shots/all%20files.PNG)

**PDFs**  
![PDFs](screen-shots/pdfs.PNG)

**Images**  
![Images](screen-shots/images.PNG)

**Documents**  
![Documents](screen-shots/docs.PNG)

---

## Getting Started (Local Development)

### Prerequisites

- Python 3.8+
- Flask (`pip install flask`)
- boto3 (`pip install boto3`)
- AWS account with S3 bucket (for cloud storage)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/File-Handling-Tool.git
    cd File-Handling-Tool
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure AWS S3:**
    - Set your bucket name in `app.py` (`AWS_BUCKET_NAME = 'your-bucket-name'`).
    - Configure AWS credentials (see below).

4. **Run the app:**
    ```bash
    python app.py
    ```

5. **Open in your browser:**
    - Visit [http://localhost:5000](http://localhost:5000)

---

## Deployment on AWS

### 1. **Create an S3 Bucket**
- Go to the [AWS S3 Console](https://s3.console.aws.amazon.com/s3/).
- Click **Create bucket**.
- Give it a unique name (e.g., `your-bucket-name`).
- Choose a region and create the bucket.

### 2. **Set Up IAM Role for EC2**
- Go to the [IAM Console](https://console.aws.amazon.com/iam/).
- Create a new role:
  - **Trusted entity:** AWS service
  - **Use case:** EC2
- Attach the policy: `AmazonS3FullAccess` (or a more restrictive policy for production).
- Name the role (e.g., `FileShareS3Role`).

### 3. **Launch an EC2 Instance**
- Go to the [EC2 Console](https://console.aws.amazon.com/ec2/).
- Launch a new instance (Amazon Linux 2 or Ubuntu recommended).
- Assign the IAM role you created to the instance.
- Open security group ports: **80** (HTTP), **22** (SSH), and **5000** (for Flask dev server, optional).

### 4. **Connect to EC2 and Deploy**
- SSH into your EC2 instance:
    ```bash
    ssh -i your-key.pem ec2-user@your-ec2-public-dns
    ```
- Install Python, pip, and git if not already installed.
- Clone your repository:
    ```bash
    git clone https://github.com/yourusername/File-Handling-Tool.git
    cd File-Handling-Tool
    ```
- Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
- Run your Flask app:
    ```bash
    python app.py
    ```
- (For production, use [Gunicorn](https://gunicorn.org/) and a reverse proxy like Nginx.)

### 5. **No AWS Credentials Needed in Code**
- Because your EC2 instance has the IAM role attached, `boto3` will automatically use those permissions to access S3.
- **Never hardcode AWS credentials in your code.**

---

## Usage

- **Upload:** Drag and drop or select a file, then click "Upload Now".
- **Browse:** Use category buttons or "All Files" to view uploaded files.
- **Download:** Click the download icon next to any file.
- **Delete:** Click the trash icon and confirm deletion.

---

## Project Structure

```
File-Handling-Tool/
│
├── app.py
├── requirements.txt
├── templates/
│   └── upload.html
├── styles.css
├── screen-shots/
│   ├── all files.PNG
│   ├── docs.PNG
│   ├── images.PNG
│   ├── main page.PNG
│   └── pdfs.PNG
└── README.md
```

---

## Security Notes

- **Never commit AWS credentials** to your repository.
- Use IAM roles for EC2 for secure, temporary credentials.
- Restrict S3 bucket permissions as much as possible.

---

## License

MIT License

---

**Made with ❤️ by [KhiLo](https://github.com/khilo619)**
