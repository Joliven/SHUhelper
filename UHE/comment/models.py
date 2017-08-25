import datetime

from mongoengine import (DateTimeField, ListField,
                         ReferenceField, StringField, GenericReferenceField)

# from config import db
from UHE.extensions import db
from UHE.user.models import User


class Comment(db.Document):
    post = GenericReferenceField()
    user = ReferenceField(User, deref=True)
    content = StringField(default='')
    liked = ListField(ReferenceField(User,deref=True), default=lambda: [])
    created = DateTimeField(default=datetime.datetime.now)
    meta = {
        'ordering': ['-created'],
        'strict': True
    }
    def to_dict(self):
        return {
            'user': self.user.to_dict(),
            'created': str(self.created),
            'content': self.content,
            'id': str(self.id)
        }