from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from materials.models import Handout
from materials.serializers import HandoutSerializer
from django.http import Http404
import requests
import os
from textstat import textstat


class TextScore(APIView):
    def level_score(self, text):
        score = textstat.text_standard(text)
        grade = int(score[0])
        levels = {
            0: "A1 - Low",
            1: "A1 - High",
            2: "A2 - Low",
            3: "A2 - High",
            4: "B1 - Low",
            5: "B1 - High",
            6: "B2 - Low",
            7: "B2 - High",
            8: "C1 - Low",
            9: "C1 - High",
            10: "C2 - Low",
            11: "C2 - High",
        }
        return levels[grade]

    def post(self, request):
        text = request.data['text']
        score = self.level_score(text)
        return Response({"text": text, "score": score})

class Definitions(APIView):
    def get(self, request):
        word = request.GET['word']
        key = os.environ.get('LEARNER_API_KEY')
        r = requests.get(f'https://www.dictionaryapi.com/api/v3/references/learners/json/{word}?key={key}')
        definitions = []
        if r.status_code == 200:
            response = r.json()
            for data in response:
                if len(data['shortdef']) > 1:
                    for item in data['shortdef']:
                        definitions.append(item)
                else:
                    definitions.append(data['shortdef'][0])
            return Response({"definitions": definitions})
        return Response({"error": "Request failed"}, status=r.status_code)

class HandoutList(APIView):
    def get(self, request, format=None):
        handouts = Handout.objects.all()
        serializer = HandoutSerializer(handouts, many=True)
        response = Response(serializer.data)
        return response

    def post(self, request, format=None):
        serializer = HandoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HandoutDetail(APIView):
    def get_object(self, pk):
        try:
            return Handout.objects.get(pk=pk)
        except Handout.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        handout = self.get_object(pk)
        serializer = HandoutSerializer(handout)
        response = Response(serializer.data)
        return response

    def put(self, request, pk, format=None):
        handout = self.get_object(pk)
        serializer = HandoutSerializer(handout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        handout = self.get_object(pk)
        handout.delete()
        return Response({"id": pk})
