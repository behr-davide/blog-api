import abc
from blog.model import Post

class AbstractPostRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, post):
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, post_id):
        raise NotImplementedError


class PostRepository(AbstractPostRepository):
    def __init__(self, session):
        self.session = session
    
    def add(self, post):
        return self.session.add(post)

    def get_by_id(self, post_id):
        return self.session.query(Post).filter_by(post_id=post_id).one()