from flask import Flask
from routes.book import book
from routes.home import home_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(book, url_prefix="/books")



app.run(debug=True)