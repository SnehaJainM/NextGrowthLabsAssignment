# App Tracker 

## Overview
The App tracker system is a Django-based web application designed to facilitate an interaction between admins and users regarding app downloads. Admins can add Android apps and assign points to users for downloading those apps. Users can view apps, track their points, and upload confirmation screenshots.

## Features

### Admin Facing
- **Add Android Apps**: Admins can add new Android applications to the system.
- **Point Allocation**: Assign points to users for downloading specific apps.
- **Custom Admin Interface**: This project does not use the default Django Admin interface, providing a tailored experience.

### User Facing
- **User Registration & Login**: Users can sign up and log in using a user-friendly interface.
- **User Profile**: Users can view their name, profile information, and points earned.
- **Tasks Completed**: Users can track the tasks they have completed.
- **Screenshot Upload**: Users can drag and drop to upload screenshots as proof of task completion, confirming they have downloaded the app.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or later
- PostgreSQL/MySQL (or any other database)
- Required Python packages (listed in `requirements.txt`)

### Steps to Set Up
 

 **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
 **Run Migrations**
   ```bash
   python manage.py migrate
   ```

 **Run Migrations for custom models**
   ```bash
   python manage.py makemigrations
   ```

 **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

**Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage
 
`http://127.0.0.1:8000/`

### URL Endpoints

- **`/`**: Home page of the application, typically displaying an overview or welcome message in json format.
- **`/adminn/`**: Custom admin page for adding and managing Android apps (admin-facing functionality).
- **`/apps-list/`**: Displays a list of registered apps that users can download and earn points from.
- **`/register/`**: User registration page for new users to create an account.
- **`/login/`**: User login page for existing users to authenticate their accounts.
- **`/logout/`**: Logs out the current user and redirects to the login page.
- **`/profile/`**: User profile page displaying personal information, points earned, and other relevant details.
- **`/tasks/`**: Lists tasks that the user has to complete or needs to complete.
- **`/apps/`**: Displays available apps for users to download and complete tasks for earning points.
- **`/completed-tasks/`**: Shows a list of tasks that the user has completed along with any relevant details.

### For Admins
- Log in to the admin interface using the following credentials:
  - **Username**: `Bhikshu`
    **Password**: `1234!@#$`
  
  - **Username**: `sneha`
    **Password**: `5678%^&*`

- Add Android apps and assign points.

### For Users
- Sign up and log in.
- View available apps, points, and completed tasks.
- Upload screenshots for completed tasks using the drag-and-drop feature.

## Technologies Used
- Django
- HTML/CSS
- Database (PostgreSQL/MySQL)

### Video Recording
- A video recording demonstrating the application’s features and functionalities is available.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## Contact
For any questions or feedback, please reach out to [snehadalal06@gmail.com].

### File Structure


```
my_project/
│
├── manage.py
├── my_project/               # Project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── home/                      # Your Django app
│   ├── migrations/            # Migration files
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py               # Admin configurations
│   ├── apps.py
│   ├── models.py              # Your models
│   ├── tests.py
│   ├── views.py               # Your views
│   ├── forms.py               # Forms for user input
│   └── urls.py                # URLs for the app
│
├── templates/                 # HTML templates
│   └── my_app/
│       ├── base.html
│       ├── home.html
│       ├── admin_page.html
│       └── profile.html     #etc dump all your html templates here 
│
├── static/                    # Static files (CSS, JS, images)
│   └── my_app/
│       ├── styles.css
│       └── scripts.js
│
└── requirements.txt           # List of dependencies
```

### Commands to Start a Project and App

1. **Create a New Django Project**
   ```bash
   django-admin startproject my_project
   ```

2. **Navigate into the Project Directory**
   ```bash
   cd my_project
   ```

3. **Create a New Django App**
   ```bash
   python manage.py startapp my_app
   ```
