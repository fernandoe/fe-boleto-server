from django.test import TestCase

from cnab400.layout import itau
from cnab400.remessa import ArquivoRemessa


class TestArquivoRemessa(TestCase):
    def setUp(self):
        self.data_header = {
            'tipo_de_registro': 1,
            'operacao': 2,
            'literal_de_remessa': 'TESTE'
        }

    def test_constructor(self):
        arquivo = ArquivoRemessa(self.data_header, itau.header.DEFAULT)
        self.assertIsNotNone(arquivo)

    def test_initialize_header(self):
        arquivo = ArquivoRemessa(self.data_header, itau.header.DEFAULT)
        row = arquivo.initialize_header()
        self.assertEqual(400, len(row))
