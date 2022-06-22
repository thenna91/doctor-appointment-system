Steps to run the Django Project in windows.

i) To install Virtual Environment package , execute below command in command prompt.

pip install virtualenv

ii) Download the attached project & change directory to the "doctor-appointment-system"

   ```cd <<your folder>>\doctor-appointment-system```

iii) Create virtual environment
      ``` virtualenv env ```

iv) Change directory to scripts folder.
       ``` cd env/Scripts ```

v) Activate virtual environment .  
       ``` activate ```

vi) Change directory to Django Application folder.
       ``` cd ../../doctorapp ```

vii) Install dependencies 

      pip install -r requirements.txt

viii) Run the below commands for migrations.
    python manage.py makemigrations

    python manage.py migrate --run-syncdb

ix) Create a user to access Admin URL.

     python manage.py createsuperuser

x) Run the django Project
    ```python manage.py runserver ```
