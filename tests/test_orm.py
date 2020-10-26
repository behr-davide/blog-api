import pytest
from blog.model import Post
from datetime import date, timedelta


def test_post_mapper_can_retrieve_post(session):
    session.execute(
        "INSERT INTO posts (title, body, created_at, updated_at)"
        "VALUES ('test title', 'test body', '2020-10-26', '2020-10-25')"
    )

    today = date.today()
    yesterday = today - timedelta(days=1)
    expected = [Post("test title", "test body", today, yesterday)]
    assert session.query(Post).all() == expected