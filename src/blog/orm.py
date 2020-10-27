from blog.model import Post
from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date
)
from sqlalchemy.orm import mapper


metadata = MetaData()

posts = Table(
    "posts", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(50)),
    Column("body", String(1000)),
    Column("created_at", Date),
    Column("updated_at", Date)
)

def start_mappers():
    mapper(Post, posts)