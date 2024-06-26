from .db import db, environment, SCHEMA, add_prefix_for_prod


class Message(db.Model):
    __tablename__ = "messages"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    msgContent = db.Column(db.String(255), nullable=False)

    # def to_dict(self):
    #     return {"id": self.id, "userId": self.userId, "msgContent": self.msgContent}
