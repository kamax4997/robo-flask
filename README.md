# FLASK REST API

REST API for Robolabs Service

## Live demo
You can find the link [here](https://robolabs.herokuapp.com)

# Installation Guide

```python
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> flask run
```

## Save dependencies to the requirements.txt
```
> pip freeze > requirements.txt
```

# Features:

- [Integrated Swagger UI](http://localhost:5000)
- [Implemented Invoice Page](http://localhost:5000/invoice)
  - Filter invoices by date_from and date_to

# Technologies Utilized:

- Python
- Flask
- REST

# Packages:

- Flask
- flask-restplus
- python-dateutil
- requests
- werkzeug
