from flask import Flask
from flask_restful import Api
from models import db

from products import ViewProducts
from product import ViewProduct
from carts import CartProducts,cartProduct


app = Flask(__name__)
api = Api(app)


db_name = 'ecommerce.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
db.init_app(app)


api.add_resource(ViewProducts,'/products')
api.add_resource(ViewProduct,'/products/<int:id>')
api.add_resource(CartProducts,'/cart')
api.add_resource(cartProduct,'/cart/<int:id>')



if __name__ == '__main__':
    from models import Product,CartItem
    with app.app_context():
        db.create_all()
    app.run(debug=True)