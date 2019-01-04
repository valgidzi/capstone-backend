from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Material
from .serializers import MaterialSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_material(title="", level=""):
        if title != "" and level != "":
            Material.objects.create(title=title, level=level)

    def setUp(self):
        # add test data
        self.create_material("test title 1", "a1")
        self.create_material("test title 2", "a2")
        self.create_material("test title 3", "b1")
        self.create_material("test title 4", "b2")


class GetAllMaterialTest(BaseViewTest):

    def test_get_all_materials(self):
        """
        This test ensures that all materials added in the setUp method
        exist when we make a GET request to the materials/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            '/materials/')
        # fetch the data from db
        expected = Material.objects.all()
        serialized = MaterialSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
