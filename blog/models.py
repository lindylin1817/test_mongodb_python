from django.db import models
from mongoengine import Document

# Create your models here.

class TestModel(Document)
    test_key = StringField(required=True)
    test_value = StringField(max_length=50)
