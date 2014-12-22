from django.shortcuts import render
from app.models import TestModel

# Create your views here.

entry = TestModel(test_key='arthur')
entry.test_value = 'Wang'
entry.save()
