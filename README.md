# Module 5 Python Flask API server

This is an API server made with Python Flask that allows users to add, get, list and delete products.

The API uses a single JSON file as its database.

The API endpoints are: 
- List products: `GET /products`
- Get product details: `GET /products/<id>`
- Add product: `POST /products`
- Delete product: `DELETE /products/<id>` 


## Start API on Windows PowerShell
```
$env:FLASK_ENV = "development"
$env:FLASK_APP = "app.py"
flask run -p 5001  
```

## Start API on Linux
```
export FLASK_ENV=development
export FLASK_APP=app.py
flask run -p 5001  
```

This starts the API server on port 5001.


The front-end web server: https://github.com/kollaaj/Module_5_python_web_server

