from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    num = models.AutoField(primary_key=True)
    # primary_key를 지정해줘야 ~~.id field error가 나지 않는다.
    title = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=500, null=True)
    author = models.CharField(max_length=50, null=True)
    tags = models.CharField(max_length=100, null=True)
    start = models.DateTimeField('start', default=timezone.now, null=False)
    end = models.DateTimeField('end', default=timezone.now, null=False)
    regdate = models.DateTimeField('created', default=timezone.now, editable=False, null=False, blank=False)
    updates = models.DateTimeField('date published', default=timezone.now, editable=False, null=False, blank=False)
    
class User(models.Model):
    num = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=500, null=False)
    password = models.CharField(max_length=50, null=False)
    profile = models.ImageField(upload_to="", null=True, blank=True)
    regdate = models.DateTimeField('created', default=timezone.now, editable=False, null=False, blank=False)
    updates = models.DateTimeField('date published', default=timezone.now, editable=False, null=False, blank=False)
