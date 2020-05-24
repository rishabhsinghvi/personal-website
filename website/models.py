from flask_login import UserMixin
from website import db, login_manager
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hash_pw = db.Column(db.String(512), nullable=False)


class BlogPost(db.Model):
    blog_id = db.Column(db.Integer, primary_key = True)
    blog_title = db.Column(db.String(512), nullable = False)
    blog_html = db.Column(db.Text, nullable=False)
    blog_delta = db.Column(db.Text, nullable = False)
    blog_created = db.Column(db.DateTime, default=datetime.utcnow())
    blog_image = db.Column(db.Text, nullable = True)

    @property
    def serialize(self):
        return {
            'blog_id': self.blog_id,
            'blog_title': self.blog_title,
            'blog_html': self.blog_html,
            'blog_delta': self.blog_delta,
            'blog_created': self.blog_created,
            'blog_image': self.blog_image
        }


class Tag(db.Model):
    tag_id = db.Column(db.Integer, primary_key = True)
    tag_name = db.Column(db.String(30), nullable = False)
    
    @property
    def serialize(self):
        return {
            'tag_id': self.tag_id,
            'tag_name': self.tag_name
        }




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
