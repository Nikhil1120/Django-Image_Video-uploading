# Django-Image_Video-uploading

# Image and Video Uploading Web Application

This project is a web application for uploading images and videos using **Django**, **REST API**, **MySQL**, and a **UI** built with **HTML/CSS/JavaScript**. The application allows users to upload, view, and manage their media files securely.


## Features
- **Image Upload**: Users can upload images to the server and view them.
- **Video Upload**: Users can upload videos, which are stored and can be accessed later.
- **Secure Authentication**: Only authorized users can upload and manage their files.
- **RESTful API**: Provides API endpoints for uploading, retrieving, and deleting media files.
- **File Management**: Allows users to view and manage their uploaded files.

## Technologies Used
- **Backend**: Django, Django REST Framework (DRF)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Tools**: 
  - Visual Studio Code (VSCode)
  - Postman (for API testing)
  - MySQL Workbench (for database management)

## Project Setup

### Prerequisites
- Python 3.x
- MySQL Server
- Node.js (if needed for frontend dependencies)
- VSCode (or any other code editor of your choice)

### Installation Steps

1. Clone the repository**:
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate     # For Windows
3.Install dependencies:
  pip install -r requirements.txt
4. Configure MySQL Database:
   -->Create a new MySQL database.
   -->Update the DATABASES section in settings.py with your MySQL credentials.
5. Migrate the database:
   python manage.py migrate
6. Run the development server:
   python manage.py runserver

# Tools
Visual Studio Code (VSCode): A powerful code editor used for developing and managing the application.
MySQL Workbench: Used to interact with the MySQL database.
Postman: To test the API endpoints during development.


   
