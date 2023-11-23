from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    class Meta:
        model = Question
        fields = ('subject', 'content')