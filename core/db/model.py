from . import db


class Users(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))
    role = db.Column(db.String(200))
    registered_on = db.Column(db.String(200))
    last_active = db.Column(db.String(200))
    is_verified = db.Column(db.String(10))
    uses_content_type = db.Column(db.String(10))

    def __init__(self, username, email, password, uses_content_type):
        self.username = username
        self.email = email
        self.password = password
        self.uses_content_type = uses_content_type


class Posts(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(100))
    content_type = db.Column(db.String(100))
    post_type = db.Column(db.String(50))
    author = db.Column(db.String(200))
    created_on = db.Column(db.String(200))
    edited_on = db.Column(db.String(200))
    is_draft = db.Column(db.String(10))
    is_trashed = db.Column(db.String(10))

    def __init__(self, title, content, author, is_draft=False,
                 content_type="html"):
        self.title = title
        self.content = content
        self.author = author
        self.is_draft = is_draft
        self.content_type = "html"
