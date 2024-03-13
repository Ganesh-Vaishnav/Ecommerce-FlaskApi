# Flask E-Commerce API

### This is a simple Flask-based backend API for a basic e-commerce platform.
### Created a RESTful API with an integration to SQLite database.

### Installation
- Clone the repository.
- Create a virtual environment and activate it.
- Run given command in your terminal.
```sh
pip install -r requirements.txt
```
- Run app.py in your terminal.
```sh
python app.py
```

## Overview
- Created a backend application using **Flask**.
- Used **Flask-RESTful** for creating a REST API
- Created API endpoints of GET,PUSH,DELETE
- CRUD operations on SQLite Database

## Screenshots of API output in Postman

- `GET /products`: Returns a list of all products.
  
![image](https://github.com/Ganesh-Vaishnav/Ecommerce-FlaskApi/assets/91007617/463d195c-29d7-4ddd-a4b1-0820f647fb03)

- `GET /products/<id>`: Returns details of a specific product.
  
![image](https://github.com/Ganesh-Vaishnav/Ecommerce-FlaskApi/assets/91007617/5231337d-61a2-4bc8-8d68-aa5b958eb9d6)

- `POST /cart`: Adds a product to the cart.
  
  ![image](https://github.com/Ganesh-Vaishnav/Ecommerce-FlaskApi/assets/91007617/94e33f0a-379e-4267-83e4-1c47cdd5b58d)
  
- `GET /cart`: Retrieves the cart items.
  
![image](https://github.com/Ganesh-Vaishnav/Ecommerce-FlaskApi/assets/91007617/b3594acd-f354-4a98-a12d-ce47b8cb7a1c)

- `DELETE /cart/<id>`: Removes a specific item from the cart.
  
![image](https://github.com/Ganesh-Vaishnav/Ecommerce-FlaskApi/assets/91007617/39f6e583-1258-4615-bc1c-0138fcbabc6a)

