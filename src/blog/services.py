from datetime import date

from blog import model, unit_of_work


def add_blog_post(title, body, uow):
    today = date.today()
    with uow:
        new_post = model.Post(title, body, today, today)
        uow.posts.add(new_post)
        uow.commit()