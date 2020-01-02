# FileStore
Projects and document system using pinax document and django-user-accounts from pinax

Home Page Image
https://github.com/kwabena-aboah/FileStore/blob/master/static/img/home.png

Create Folder image
https://github.com/kwabena-aboah/FileStore/blob/master/static/img/create_folder.png

Upload File Image
https://github.com/kwabena-aboah/FileStore/blob/master/static/img/upload.png

User Menu Image
https://github.com/kwabena-aboah/FileStore/blob/master/static/img/user_menu.png

Account Settings Image
https://github.com/kwabena-aboah/FileStore/blob/master/static/img/account_settings.png

Account Password Image
https://github.com/kwabena-aboah/FileStore/blob/master/static/img/account_password.png


============
Installation
============
clone the repo from github and install
1. git clone https://github.com/kwabena-aboah/FileStore.git
2. cd /directory/of/app
3. pip install -r requirements.txt
4. go to your settings.py and configure your email settings:

  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_HOST_USER = '' # your email address here
  EMAIL_HOST_PASSWORD = r'' # your password goes here
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True
  EMAIL_USE_SSL = False
  DEFAULT_FROM_EMAIL = 'Admin<admin@127.0.0.1:8000>'
  
4. run migrations using 'python manage.py migrate' command
5. to create admin user use the command 'python manage.py createsuperuser'
6. start the application using the command 'python manage.py runserver'

============
Todo
============
1. Add Plagiarism Checker to scan files uploaded to the platform


License
-------
FileStore is licensed under MIT, see ``LICENSE.txt``.
