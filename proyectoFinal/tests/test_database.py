import copy
import unittest
import database as db
import helpers
import config
import csv

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista= [
            db.Cliente("19E", "Edgar", "Milá"),
            db.Cliente("21C", "Carla", "de la Cruz"),
            db.Cliente("23A", "Ana", "Milá"),
        ]
    def test_buscar_cliente(self):
        cliente_existente= db.Clientes.buscar("23A")
        cliente_inexistente= db.Clientes.buscar("28C")
        self.assertEqual(cliente_existente, db.Clientes.lista[2])
        self.assertIsNone(cliente_inexistente)
        
    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39X', 'Andrea', 'de la Cruz')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')    
        self.assertEqual(nuevo_cliente.nombre, 'Andrea')    
        self.assertEqual(nuevo_cliente.apellido, 'de la Cruz')    
    
    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('21C'))
        cliente_modificado = db.Clientes.modificar('21C', 'Carlita', 'de la Cruz')
        self.assertEqual(cliente_a_modificar.nombre, 'Carla')
        self.assertEqual(cliente_modificado.nombre, 'Carlita')
    
    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('19E')
        cliente_rebuscado = db.Clientes.buscar('19E')
        self.assertEqual(cliente_borrado.dni, '19E')
        self.assertIsNone(cliente_rebuscado)
    
    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('19E', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('23SDSD', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('A23', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('19E')
        db.Clientes.borrar('21C')
        db.Clientes.modificar('23A', 'Ana María', 'Milá')
        dni, nombre, apellido = None, None, None
        
        with open(config.DATABASE_PATH, newline='\n', encoding='UTF-8') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)
            self.assertEqual(dni, '23A')
            self.assertEqual(nombre, 'Ana María')
            self.assertEqual(apellido, 'Milá')
    