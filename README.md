# FileSharing Tool

A modern, user-friendly web application for uploading, browsing, downloading, and deleting files, powered by Flask and AWS S3.

## Features

- **Drag & Drop File Upload**: Effortlessly upload files with a modern drag-and-drop interface.
- **Category Browsing**: View files by type (PDFs, Images, Audio, Videos, Documents, Archives, Web Files, Others).
- **Download & Delete**: Download or delete files directly from the browser.
- **Responsive UI**: Clean, mobile-friendly design using Tailwind CSS and Font Awesome.
- **AWS S3 Storage**: All files are securely stored and managed in your Amazon S3 bucket.

## Screenshots

![Upload & Browse](screenshots/upload_browse.png)
![Delete Confirmation](screenshots/delete_modal.png)

## Demo

[Live Demo Link (if available)](https://your-demo-url.com)

## Getting Started

### Prerequisites

- Python 3.8+
- AWS account with an S3 bucket
- AWS credentials configured (via environment variables, AWS CLI, or IAM role)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/fileshare-pro.git
    cd fileshare-pro
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure AWS credentials:**
    - Set up your AWS credentials using [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) or environment variables:
      ```bash
      export AWS_ACCESS_KEY_ID=your-access-key
      export AWS_SECRET_ACCESS_KEY=your-secret-key
      export AWS_DEFAULT_REGION=us-east-1
      ```

4. **Set your S3 bucket name:**
    - Edit `app.py` and set `AWS_BUCKET_NAME` to your bucket.

5. **Run the app:**
    ```bash
    python app.py
    ```

6. **Open in your browser:**
    - Visit [http://localhost:5000](http://localhost:5000)

## Project Structure

```
File-Handling-Tool/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── upload.html
│   └── styles.css
├── static/
│   └── (optional static files)
└── README.md
```

## Usage

- **Upload**: Drag and drop or select a file, then click "Upload Now".
- **Browse**: Use category buttons or "All Files" to view uploaded files.
- **Download**: Click the download icon next to any file.
- **Delete**: Click the trash icon and confirm deletion.

## Security Notes

- **Never commit AWS credentials** to your repository.
- Use IAM roles or environment variables for credentials.
- Ensure your S3 bucket permissions are secure.

## License

[MIT License](LICENSE)

## Credits

- [Flask](https://flask.palletsprojects.com/)
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Tailwind CSS](https://tailwindcss.com/)
- [Font Awesome](https://fontawesome.com/)

---

**Made with ❤️ by [Your Name](https://github.com/yourusername)**
