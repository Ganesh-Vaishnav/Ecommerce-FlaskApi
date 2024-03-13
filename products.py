from flask_restful import Resource
from flask import Flask,request
from models import Product,db

class ViewProducts(Resource):
    def get(self):
        product_list = Product.query.all()
        return [{
                'id': product.id,
                'name': product.name ,
                'description': product.description,
                'price': product.price,
                'image_url': product.image_url,
            } 
            for product in product_list ]
    
    def post(self):
        data = request.get_json()
        
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        image_url = data.get('image_url')

        new_product = Product(name=name,description=description,
                              price=price,image_url=image_url)
        db.session.add(new_product)
        db.session.commit()

        return {'message': 'Product added in the List'}
        
    
    