from flask_restful import Resource
from flask import Flask,request
from models import CartItem,Product ,db

class CartProducts(Resource):
    def get(self):
        cart_list = CartItem.query.all()

        return [{
            'id': product.id, 
            'product_id': product.product_id,
            'quantity': product.quantity
            } 
            for product in cart_list]
    
    def post(self):
        data = request.get_json()
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        if product_id is None:
            return {'message' : 'Enter Product Id properly'}
        
        product = Product.query.get_or_404(product_id)

        cart_product = CartItem(product_id=product.id,quantity=quantity)
        db.session.add(cart_product)
        db.session.commit()
        return {'message': 'Your product is added to cart successfully'}
    
class cartProduct(Resource):
    def delete(self,id):
        product = CartItem.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()

        return {'message': 'Item removed successfully'} 
    