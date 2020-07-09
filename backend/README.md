# Backend Instructions

### Tech Stack:
    **framework**
        - Django
    **database**
        - postgresql


### Installing postgresql
    **for mac**
        - download postgresql mac version
    1. setting postgres datbase password
        a. go into the postgre database
        b. set password as `root` in order to match the django setting (change it in `settings.py` if you want in the DATABASE section)
    2. check the port
        make sure the port of the postgresql is `5432`
    3. create database: petadoptiondb
        CREATE DATABASE petadotiondb;

### Connecting postgresql in django
    **Make sure you install `psycopg2`**
    with the code `pip install psycopg2` in your virtual environment


### Starting the server
    - make sure you are in the $backend$ folder
    ```python3 manage.py runserver```

### Database migrations
    - make changes to models
    ```python3 manage.py makemigrations```
    - migrate data
    ```python3 manage.py migrate```

### Managing Data on server
    1. login to [localhost](http://localhost:8000/admin)
    2. The super user name has been set:
        * user: `pet_adoption_admin`
        * password: `password: summer_2020_pet_admin_root`
    3. Then you can manage: add/delete/update the database with example data for now

### TODO: 
    1. Check whether we need to implement the User class provided that django already has a built in user class that provides authority management
        - inherit it?
        - make a new one?
    2. The Immune class requires more information
        - brainstorm on what fields do we need
    3. The Image Class
        - How do we store image? Link? Image File?
    4. Data Validation
        - How should we validate the information before storing it database?
            a. Validate it on frontend vs. backend 