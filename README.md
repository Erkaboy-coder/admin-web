Basic Django Commands:

1. Start a New Project:
   django-admin startproject projectname  ==>  Creates a new Django project.

2. Start a New App:
   python manage.py startapp appname   ==>  Creates a new Django app within your project.

3. Run the Development Server:
   python manage.py runserver  ==>  Starts the Django development server at `http://127.0.0.1:8000/`
   python manage.py runserver 8080

4. Make Migrations:
   python manage.py makemigrations  ==>  Creates new migration files based on the changes in your models.

5. Apply Migrations:
   python manage.py migrate  ==> Applies migrations to your database.

6. Create Superuser:
   python manage.py createsuperuser  ==>  Creates an admin user for accessing the Django admin interface.

