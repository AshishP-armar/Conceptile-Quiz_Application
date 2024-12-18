# Conceptile-Quiz_Application

## Quiz App

A web-based quiz application built using Django. The app allows users to take quizzes and tests their knowledge with multiple-choice questions.


## Features
- Randomized quiz generation for each session.
-   View quiz performance after completion.

## Technologies Used
- Python 
- Django 
- MySQL (configurable) 
-  HTML, CSS, JavaScript (for front-end)ntrol


## Installation
1. Make Virtual ENV:
```bash
python3 -m vevn .venv
. .venv/bin/actiavte   # To activate virtual env
```
2. Clone the repository:
   ```bash
   git clone https://github.com/AshishP-armar/Conceptile-Quiz_Application.git
   cd Conceptile_Quiz_Application
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt  # For Flask
   ```
 
4. DataBase: 
  #### Update the `DATABASES` section in `settings.py` with your database credentials:
  


```base
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # or 'django.db.backends.postgresql'
        'NAME': 'Quiz_App',
        'USER': 'root',
        'PASSWORD': 'Atp@4466',
        'HOST': 'localhost',
        'PORT': '3306',  # or '5432' for PostgreSQL
    }
}
```
Copy code
```bash
create database Quiz_App # run this in mysql
python manage.py migrate # in your project root
```
## Run file to add Some quetions in DB
```bash
python fakequetions.py
```
## Run the project.
```bash
python manage.py runserver
```
## Contact

For queries or collaboration, reach out to:
- **Email**: ashishparmar9817@gmail.com
- **LinkedIn**: [Ashish Parmar](https://www.linkedin.com/in/ashish-parmar-20b5a42bb)
