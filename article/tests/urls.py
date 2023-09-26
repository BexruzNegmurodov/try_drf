from django.test import TestCase
from django.urls import reverse


class TestArticleList(TestCase):
    def test_list_url(self):
        status = 200
        url = reverse('article:list')
        client_code = self.client.get(url).status_code
        self.assertEqual(status, client_code)
