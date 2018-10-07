# IIITV Project Museum
Before starting any academic project, how often do you think, “What projects my seniors did in this course ?”
Often! right?

This is a portal for IIITV, which provides project documentation done by previous students in various subjects.

### Installation (python 3.6)
- Get the requirements

`$ sudo apt-get install python3-pip`


- Fork and clone the expenses-app repository

	`$ git clone https://github.com/<Username>/IIITV_Project-_Museum`

- Now get the django specific requirements

	`$ cd IIITV_Project-_Museum`

  	`$ pip install django`

- Now run the server

	`$ python manage.py runserver`

open [127.0.0.1:8000](127.0.0.1:8000) in the browser


- Apply the migrations(Already included for ease)

	`python manage.py makemigrations`

	`python manage.py migrate`

- Create the admin

	`python manage.py createsuperuser`

- Add the relevant information

- open [127.0.0.1:8000/admin](127.0.0.1:8000/admin)
