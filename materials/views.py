from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from materials.models import Material
from materials.serializers import MaterialSerializer
from django.http import Http404

class MaterialList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaterialDetail(APIView):
    """
    Retrieve, update or delete a code material.
    """
    def get_object(self, pk):
        try:
            return Material.objects.get(pk=pk)
        except Material.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        material = self.get_object(pk)
        serializer = MaterialSerializer(material)
        return Response(serializer.data)

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
