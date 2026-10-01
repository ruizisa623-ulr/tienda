from django.test import TestCase
from .models import Producto


class ProductoEstadoTests(TestCase):
	def test_estado_checkbox_en_creacion_y_edicion(self):
		datos = {
			"nombre": "Producto de prueba",
			"categoria": "Prueba",
			"precio": "10.00",
			"cantidad": "2",
		}

		self.client.post("/productos/crear/", datos)
		producto = Producto.objects.get(nombre="Producto de prueba")
		self.assertFalse(producto.estado)

		self.client.post(f"/productos/editar/{producto.id}/", {**datos, "estado": "True"})
		producto.refresh_from_db()
		self.assertTrue(producto.estado)

		self.client.post(f"/productos/editar/{producto.id}/", datos)
		producto.refresh_from_db()
		self.assertFalse(producto.estado)
