from app import app, db, moment
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'moment': moment, 'User': User, 'Post': Post}