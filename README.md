# Web Application for Greetings

This web application is designed to greet users and send them a congratulatory email. It allows users to add their name, receive a greeting on the website, and optionally receive a congratulatory email.

## Features
- Users can enter their name to receive a greeting on the website.
- After entering their name, users can opt to receive a congratulatory email.
- The application sends emails using a custom email service (SMTP).

## Requirements
- Python 3.x
- Virtual environment (recommended)
- Gmail or another email service for sending emails

## Installation

Follow the steps below to set up the application on your local machine.

### 1. Clone the repository
To get started, clone this repository to your local machine:
```bash
git clone https://github.com/vladduucckk/web-application-for-greetings
cd web-application-for-greetings
```


### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate mac/linux
venv\Scripts\activate windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. 5. Set up your environment variables

For security reasons, secret keys, email, and password are not stored in the code. Instead, you’ll need to create a .env file in the root directory of the project and provide your email configuration there.

Example .env file:
```bash
SECRET_KEY=your_secret_key
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
```

[greetings site](https://vladduucckk.pythonanywhere.com/)

### License

### Key Points:
1. **Cloning the repository**: First step to getting the code onto the local machine.
2. **Setting up a virtual environment**: For isolation of dependencies.
3. **Activating the virtual environment**: Needed to work within the environment.
4. **Installing requirements**: Ensures all necessary libraries are installed.
5. **Environment variables**: Secret keys and email credentials are hidden in the `.env` file, not stored in the code.

