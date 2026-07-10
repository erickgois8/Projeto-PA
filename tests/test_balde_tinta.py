import unittest
from types import SimpleNamespace
from unittest.mock import Mock

from controller.balde_tinta import BaldeTinta


class TestBaldeTinta(unittest.TestCase):
    def test_preencher_altera_cor_do_objeto_clicado(self):
        figura = SimpleNamespace(id=7, cor_preenchimento="")
        figuras = SimpleNamespace(dados=[figura])
        canvas = Mock()
        canvas.find_overlapping.return_value = [7]
        desenho = Mock()
        cores = SimpleNamespace(preenchimento="#123456")

        balde = BaldeTinta(canvas, figuras, cores, desenho)
        balde.preencher(SimpleNamespace(x=10, y=20))

        self.assertEqual(figura.cor_preenchimento, "#123456")
        desenho.redesenhar_figuras.assert_called_once_with(canvas, figuras)


if __name__ == "__main__":
    unittest.main()
