from flask_restful import Resource
from flask import Flask,jsonify
from models import Product

class ViewProduct(Resource):
    def get(self,id):
        product = Product.query.get_or_404(id)
        return  {
                'id': product.id,
                'name': product.name ,
                'description': product.description,
                'price': product.price,
                'image_url': product.image_url,
            } 