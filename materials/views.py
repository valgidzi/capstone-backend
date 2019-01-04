from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from materials.models import Material
from materials.serializers import MaterialSerializer


@api_view(['GET', 'POST'])
def material_list(request, format=None):
    """
    List all code materials, or create a new material.
    """
    if request.method == 'GET':
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def material_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code material.
    """
    try:
        material = Material.objects.get(pk=pk)
    except Material.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MaterialSerializer(material)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from django.shortcuts import render
#
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from materials.models import Material
# from materials.serializers import MaterialSerializer
#
# # Create your views here.
# @csrf_exempt
# def material_list(request):
#     """
#     List all materials, or create a new material.
#     """
#     if request.method == 'GET':
#         materials = Material.objects.all()
#         serializer = MaterialSerializer(materials, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MaterialSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def material_detail(request, pk):
#     """
#     Retrieve, update or delete a material.
#     """
#     try:
#         material = Material.objects.get(pk=pk)
#     except Material.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = MaterialSerializer(material)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = MaterialSerializer(material, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         material.delete()
#         return HttpResponse(status=204)
