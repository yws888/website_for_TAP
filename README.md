# website_for_TAP
For the DARE TAP assessment


Technical Requirements:
1. Usage of ORM:

This site is built with Django, which implements an Object-relational Mapper (ORM) that maps Python objects/classes (code) to relational database (SQL is used here) statements. The code for these objects is located in the models.py file.



2. Logging of all CRUD actions.

There are 3 places you can see logs. The first is the terminal (when the server is running) where the logs are printed in this format:

The second is a django.log file located in the online_store directory which would be created when logs are generated. These logs log the HTTP requests made to API endpoints

Lastly, admin account can also view the logs in the admin page under the log entries section. Here only Create (addition), update (Change) and Delete (Deletion) actions are logged.



3. Explain the following in a README file.
a. Steps required to run your application.(Please provide instructions on how to run your source code locally on our laptop in the README file.)


## Setup (for Mac)
Change Directory (cd) to the root of this repository.

Install virtualenv if not already on your laptop (assuming pip is already installed)

```
pip install virtualenv
```

Create virtual environment

```
virtualenv venv
```

Activate virtual environment
```
source venv/bin/activate
```

Install dependencies 
```
pip install -r requirements.txt
```

Start the developmental server (Assumption is that this portion does not require a production ready server)
```
python manage.py runserver
```

Website should then be accessible at:
```
http://localhost:8000/
```

## Setup (for Windows)
Change Directory to the root of this repository.

Set up virtual environment
```
py -m venv env
```

Install dependencies 
```
py -m pip install -r requirements.txt
```

Start the server
```
py manage.py runserver
```


b. Explain how you would deploy this app on a cloud environment (Bonus: How you would
do this with serverless components).

To deploy on an AWS EC2 (Ubuntu) instance:

-Assuming one is able to set it up and SSH into it,

git clone and change Directory (cd) to the root of this repository.

install binaries if not already present:
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3-pip
pip install virtualenv
```

Create a virtual environment and activate it
```
virtualenv venv
source venv/bin/activate
```

Install dependencies 
```
pip install -r requirements.txt
```

Update the ALLOWED_HOSTS in settings.py file with public IP address of the EC2 instance, e.g.
```
ALLOWED_HOSTS = ["88.88.88.88"]
```

Create security rules in the AWS config settings to allow TCP incoming traffic on ports 80

Next, we would use gunicorn and nginx to have a production-ready server:

First nginx is installed:
```
sudo apt install nginx
```

Next we can create a socket file for gunicorn:
```
sudo nano /etc/systemd/system/gunicorn.socket
```

Adding the following content to it:
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Next we can create the service file (config) for gunicorn. 
```
sudo nano /etc/systemd/system/gunicorn.service
```

change the User, WorkingDirectory, ExecStart if need be
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/website_for_TAP
ExecStart=/home/ubuntu/venv/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock website_for_TAP.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start and enable the guicorn service
```
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

Next we can create the configuration file for Nginx:
```
sudo nano /etc/nginx/sites-available/website_for_TAP
```

change the IP address accordingly

```
server {
    listen 80;
    server_name <IP address>;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/website_for_TAP;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

create a symbolic link:
```
sudo ln -s /etc/nginx/sites-available/website_for_TAP /etc/nginx/sites-enabled/
```

Finally, restart nginx:
```
sudo systemctl restart nginx
```

If all works well, the website should be accessible on the IP address and port 80 via HTTP

c. Explain security hardening techniques on a cloud environment.

“input validation”: 
“logging”:

You may include a section with the assumptions, interpretations you have made about the requirements above or notes on your architecture decisions.


Assumptions/Interpretations:

-

Notes on architecture decisions:
-I have used the Django framework for this website, which follows a Model-View-Template architecture. The data interface  is in the models (models.py), app business logic is in the views (views.py), and output is in the templates (html files).

![Alt text](<Screenshot 2023-09-18 at 2.55.37 pm.png>)


Please send us a link to your repository when you complete your assessment via this form:
https://go.gov.sg/csgdaretap2024

Grading Criteria / Matric
You will be graded on:
• Readability and code cleanliness
• Good coding practices
• Code structure/design, e.g. modularity, testability
• User Experience
• Git best practices (Gitflow)
• Documentation
• Ease of running source code without external troubleshooting
