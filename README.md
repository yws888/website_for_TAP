# website_for_TAP
For the DARE TAP assessment

Technical Requirements:
1. Usage of ORM:

This site is built with Django, which implements an Object-relational Mapper (ORM) that maps Python objects/classes (code) to relational database (SQL is used here) statements. The code for these objects is located in the models.py file.

2. Logging of all CRUD actions.

There are 3 places you can see logs. The first is the terminal (when the server is running) where the logs are printed in this format:

The second is a django.log file located in the online_store directory which would be created when logs are generated. 

Lastly, admin account can also view the logs in the admin page under the log entries section. Here only Create (addition), update (Change) and Delete (Deletion) actions are logged.

3. Explain the following in a README file.
a. Steps required to run your application.(Please provide instructions on how to run your source code locally on our laptop in the README file.)

## Setup (for Mac)
Change Directory to the root of this repository.

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

Start the developmental server
```
python manage.py runserver
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
