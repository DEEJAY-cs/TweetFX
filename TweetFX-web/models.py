from server import app,db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(max), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class LabelledTweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(280), nullable=False)
    datestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sentiment = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"LabelledTweets('{self.sentiment}', '{self.tweet}')"