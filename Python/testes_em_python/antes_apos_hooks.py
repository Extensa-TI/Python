"""
hooks -> são os testes em si, ou seja, a execução dos testes

setup() -> executado antes de cada método de teste. É util para criarmos instâncias
de objetos e outros dados.

tearDown -> executado ao final de cada método de teste. É útil para excluir ou fechar
conexões com banco de dados. 
"""

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown vai rodar após o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown vai rodar após o teste
        pass

    def tearDown(self):
        # configuração do tearDown
        pass

