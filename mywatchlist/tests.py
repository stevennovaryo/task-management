from http import client
from multiprocessing.connection import Client
from pydoc import cli
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse

class MyWatchListTests(TestCase):
    def test_html_status(self): 
        client = Client()
        response = client.get(reverse("mywatchlist:show_watchlist"))
        self.assertEqual(response.status_code, 200)
    
    def test_xml_status(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_xml"))
        self.assertEqual(response.status_code, 200)
    
    def test_json_status(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_json"))
        self.assertEqual(response.status_code, 200)
