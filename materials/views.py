from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from materials.models import Material, Text, Handout
from materials.serializers import MaterialSerializer, TextSerializer, HandoutSerializer
from django.http import Http404
import requests
import os


class MaterialList(APIView):
    """
    List all materials, or create a new material.
    """
    def get(self, request, format=None):
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        response = Response(serializer.data)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, format=None):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaterialDetail(APIView):
    """
    Retrieve, update or delete a material.
    """
    def get_object(self, pk):
        try:
            return Material.objects.get(pk=pk)
        except Material.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        material = self.get_object(pk)
        serializer = MaterialSerializer(material)
        response = Response(serializer.data)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def put(self, request, pk, format=None):
        material = self.get_object(pk)
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        material = self.get_object(pk)
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TextList(APIView):
    """
    List all texts, or create a new text.
    """
    def get(self, request, format=None):
        texts = Text.objects.all()
        serializer = TextSerializer(texts, many=True)
        response = Response(serializer.data)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, format=None):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            response['Access-Control-Allow-Origin'] = '*'
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
                    definition = ', '.join(data['shortdef'])
                else:
                    definition = data['shortdef'][0]
                definitions.append(definition)
            return Response({"definitions": definitions}, status=status.HTTP_200_OK)
        return Response({"error": "Request failed"}, status=r.status_code)

class HandoutList(APIView):
    def get(self, request, format=None):
        handouts = Handout.objects.all()
        serializer = HandoutSerializer(handouts, many=True)
        response = Response(serializer.data)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    def post(self, request, format=None):
        serializer = HandoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
