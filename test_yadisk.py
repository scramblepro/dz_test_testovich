import unittest
import requests
from OAuthtoken import token

class TestYandexDiskAPI(unittest.TestCase):
    BASE_URL = "https://cloud-api.yandex.net/v1/disk"
    HEADERS = {"Authorization": token}

    def setUp(self):
        """Подготовка перед каждым тестом."""
        # Создаем папку "test_folder" перед тестом на существующую папку
        self.existing_folder_path = "test_folder"
        requests.put(f"{self.BASE_URL}/resources?path={self.existing_folder_path}", headers=self.HEADERS)

    def test_create_folder(self):
        """Положительный тест на создание папки."""
        folder_path = "new_test_folder"
        response = requests.put(f"{self.BASE_URL}/resources?path={folder_path}", headers=self.HEADERS)
        
        self.assertEqual(response.status_code, 201, "Ожидается код ответа 201")
        
        # Проверяем, что папка появилась на Диске
        response = requests.get(f"{self.BASE_URL}/resources?path={folder_path}", headers=self.HEADERS)
        self.assertEqual(response.status_code, 200, "Ожидается код ответа 200")
        self.assertIn("name", response.json(), "Ответ должен содержать имя папки")
        self.assertEqual(response.json()["name"], folder_path, "Имя созданной папки должно совпадать с ожидаемым")
    
    def test_create_existing_folder(self):
        """Отрицательный тест на создание уже существующей папки."""
        response = requests.put(f"{self.BASE_URL}/resources?path={self.existing_folder_path}", headers=self.HEADERS)
        
        self.assertEqual(response.status_code, 409, "Ожидается код ответа 409 при создании уже существующей папки")
    
    def test_create_folder_invalid_name(self):
        """Отрицательный тест на создание папки с некорректным именем."""
        folder_path = ":*?|"
        response = requests.put(f"{self.BASE_URL}/resources?path={folder_path}", headers=self.HEADERS)
        
        self.assertEqual(response.status_code, 400, "Ожидается код ответа 400 при создании папки с некорректным именем")
    
    def tearDown(self):
        """Удаление тестовых папок после выполнения тестов."""
        # Удаляем все тестовые папки после каждого теста
        folders_to_delete = ["test_folder", "new_test_folder"]
        for folder in folders_to_delete:
            requests.delete(f"{self.BASE_URL}/resources?path={folder}&permanently=true", headers=self.HEADERS)

if __name__ == "__main__":
    unittest.main()
