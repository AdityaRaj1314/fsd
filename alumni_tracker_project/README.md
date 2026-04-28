# Alumni Tracker Project

This is a Django project designed to track alumni details (Name, USN, Passing Year, Company) and filter them based on their graduation year.

## How to Execute the Project

1. **Activate your Virtual Environment** (if you have one in your main folder):
   ```powershell
   cd "c:\Users\Aditya Raj\fsd"
   .venv\Scripts\Activate.ps1
   ```
2. **Navigate to the Project Directory**:
   ```powershell
   cd "alumni_tracker_project"
   ```
3. **Run Database Migrations** (if you make changes to models):
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Start the Development Server**:
   ```powershell
   python manage.py runserver
   ```
5. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## File Structure and Functionality (Where to put what)

When working on this Django project, follow this standard structure:

- **`manage.py`**: The command-line utility for administrative tasks (running server, migrations). Do not modify this file.
- **`alumni_tracker_project/settings.py`**: Add your created apps (e.g., `alumni`) to `INSTALLED_APPS` here.
- **`alumni_tracker_project/urls.py`**: The main URL configuration. Route main paths here using `include('alumni.urls')`.
- **`alumni/models.py`**: Define your database schema (Tables/Classes like `Alumni`) here.
- **`alumni/views.py`**: Write your core logic here. Handle user requests, interact with models, and render HTML templates.
- **`alumni/urls.py`**: Define route endpoints specific to this app and map them to views.
- **`alumni/templates/alumni/`**: Store all your HTML files (e.g., `index.html`, `search.html`) inside this folder.
