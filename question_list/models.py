from django.db import models

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)