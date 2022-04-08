# Implementation of Robolabs invoices API with Python/Django

Implemented Robolabs invoice API and displayed the list of invoices in 
page rendered with django

# Installation Guide

```
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> python manage.py runserver
```

# Features:
- Implemented Invoice Page
  - Filter invoices by date range

# Technologies Utilized:

- Python
- Django

# Here are some of the choices that I made during development

- Decoupling the sensitive credentials
  - Option 1: Use `os.getenv('env_name')` or `os.environ['env_name']` 
  - Option 2: Use [Python decouple](https://pypi.org/project/python-decouple/)
  - My choice: I went with python decouple as it help in discoverability of .env files. Config can be declared in .env or .ini file and it provided inbuilt support for type casting


- Validating the data received for the front end
  - Option 1: Pass each value to the validator function and raise validation error accordingly 
  - Option 2: Use Django forms respective FormField and take benefit of inbuilt validation
  - My choice: I went with using the second option as better to use Django's inbuilt form fields and take the benefits of the validation provided by them


- Using form in django template
  - Option 1: Using custom html/css to build the from 
    - ```html
        <form action="." method="post">
            <label for="id_from_date">From date:</label>

            <input type="date" id="id_from_date" name="from_date"
                   value="2022-01-01"
                   min="2018-01-01" max="2022-12-31">
            <label for="id_to_date">To date:</label>

            <input type="date" id="id_to_date" name="to_date"
                   value="2022-01-31"
                   min="2018-01-01" max="2022-12-31">
            <input type="submit" value="Filter">
        </form>
  - Option 2: Using django form to render the form in html
    - ```html
      <form action="." method="post">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Filter">
      </form>
          
  - My choice : I went with option 2 as it is more readable and major logic and validation can be controlled from backend. 

  #it took me approx 2.5 hours to finish this test#
