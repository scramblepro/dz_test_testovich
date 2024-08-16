import unittest
from unittest.mock import patch
from buhgalter import get_person_by_document_number, get_shelf_by_document_number, add_document, documents, directories

class TestDocuments(unittest.TestCase):

    def setUp(self):
        self.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        
        self.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

    def test_get_person_by_document_number(self):
        with patch('buhgalter.documents', self.documents):
            self.assertEqual(get_person_by_document_number("2207 876234"), "Василий Гупкин")
            self.assertEqual(get_person_by_document_number("11-2"), "Геннадий Покемонов")
            self.assertEqual(get_person_by_document_number("10006"), "Аристарх Павлов")
            self.assertEqual(get_person_by_document_number("12345"), "Документ не найден")

    def test_get_shelf_by_document_number(self):
        with patch('buhgalter.directories', self.directories):
            self.assertEqual(get_shelf_by_document_number("2207 876234"), '1')
            self.assertEqual(get_shelf_by_document_number("10006"), '2')
            self.assertEqual(get_shelf_by_document_number("12345"), "Документ не найден на полках")

    def test_add_document(self):
        with patch('buhgalter.documents', self.documents), patch('buhgalter.directories', self.directories):
            result = add_document("passport", "12345", "Новый Человек", "2")
            self.assertEqual(result, "Документ успешно добавлен")
            self.assertIn({"type": "passport", "number": "12345", "name": "Новый Человек"}, self.documents)
            self.assertIn("12345", self.directories['2'])

            result = add_document("passport", "67890", "Другой Человек", "4")
            self.assertEqual(result, "Такой полки не существует")
            self.assertNotIn({"type": "passport", "number": "67890", "name": "Другой Человек"}, self.documents)

if __name__ == '__main__':
    unittest.buhgalter()
