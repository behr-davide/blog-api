from datetime import date
from flask import Flask, request
from blog.orm import start_mappers
from blog import services, unit_of_work

app = Flask(__name__)
start_mappers()

@app.route("/post", methods=["POST"])
def create_blog_post():
    current_date = date.today()
    services.add_blog_post(
        request.json["title"], request.json["body"],
        unit_of_work.SqlAlchemyUnitOfWork
    )
    return "OK", 201