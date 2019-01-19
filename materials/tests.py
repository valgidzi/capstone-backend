from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Handout
from .serializers import HandoutSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_handout(text="", words="", definitions="", user="", score="", title=""):
        if text != "" and words != "" and definitions != "" and user != "" and score != "" and title != "":
            Handout.objects.create(text=text, words=words, definitions=definitions, user=user, score=score, title=title)

    def setUp(self):
        # add test data
        self.test1 = self.create_handout("test1", "test1", "test1", "test1", "test1", "test1")
        self.test2 = self.create_handout("test 2", "test 2", "test 2", "test 2", "test 2", "test 2")
        self.test3 = self.create_handout("test 3", "test 3", "test 3", "test 3", "test 3", "test 3")


class GetAllHandoutTest(BaseViewTest):

    def test_get_all_handouts(self):
        """
        This test ensures that all handouts added in the setUp method
        exist when we make a GET request to the handouts/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            '/handouts/')
        # fetch the data from db
        expected = Handout.objects.all()
        serialized = HandoutSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
