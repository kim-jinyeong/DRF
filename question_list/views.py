from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class QuestionList(APIView):
    def get(self, request):
        model = Question.objects.all()
        serializer = QuestionSerializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionDetail(APIView):

    def get(self, request, question_id):
        model = Question.objects.get(question_id=question_id)
        serializer = QuestionSerializer(model)
        return Response(serializer.data)
    
    def put(self, request, question_id):
        model = Question.objects.get(question_id = question_id)
        serializer = QuestionSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, question_id):
        model = Question.objects.get(question_id=question_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)