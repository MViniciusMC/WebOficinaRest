from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class UserSignUpTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        # Criar um usuário para autenticação
        cls.user = User.objects.create_user(username='Teste', password='teste123')

    def setUp(self):
        # Logar o usuário antes de cada teste
        self.client.login(username='Teste', password='teste123')
        

    def test_se_metodo_post_funciona_corretamente(self):
        data = {"chassi":"AA321456", 
    "modelo":"Teste", 
    "ano":"1886", 
    "placa":"11a111",
        }
        url = reverse('API:VeiculosViewSet-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("POST  ok")
    def teste_se_metodo_get_funciona_corretamente(self):
        url = reverse('API:VeiculosViewSet-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("GET ok")
        

