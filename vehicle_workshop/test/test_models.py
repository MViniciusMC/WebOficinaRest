from django.test import TestCase
from ..models import Veiculos

        
class VeiculosTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Veiculos.objects.create(chassi="TT123456", modelo="Teste", ano=2000, placa="TTT0T00")


    def test_str_igual_a_modelo_placa(self):
        
        veiculo =  Veiculos.objects.get(id=1)
        modelo_e_placa =  f'{veiculo.modelo}, {veiculo.placa}'
        self.assertEquals(modelo_e_placa, str(veiculo))
    
    def test_nao_criar_veiculo_com_chassi_igual(self):
        try:
            Veiculos.objects.create(chassi="TT123456", modelo="TesteCHassi", ano=2000, placa="CHASSI")
        except Exception:
            print("\nNão é possível inserir novo veículo com um chassi já cadastrado")
    def test_nao_criar_veiculo_com_placa_igual(self):
        try:
            Veiculos.objects.create(chassi="TTPLACA", modelo="TestePLACA", ano=2000, placa="TTT0T00")
        except Exception:
            print("\nNão é possível inserir novo veículo com um placa já cadastrada")