import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Patch FileStorage to avoid writing to the file during tests
        patcher = patch('models.engine.file_storage.FileStorage._FileStorage__file_path', new_callable=str)
        self.addCleanup(patcher.stop)
        self.mocked_file_path = patcher.start()

    def test_base_model_init(self):
        """Test initialization of BaseModel."""
        new_model = BaseModel()
        
        # Check attributes
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_base_model_str(self):
        """Test __str__ method of BaseModel."""
        new_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(new_model.id, new_model.__dict__)
        self.assertEqual(str(new_model), expected_str)

    def test_base_model_save(self):
        """Test save method of BaseModel."""
        with patch('models.engine.file_storage.FileStorage.save') as mock_save:
            new_model = BaseModel()
            old_updated_at = new_model.updated_at
            new_model.save()

            # Check if updated_at is updated after save
            self.assertNotEqual(old_updated_at, new_model.updated_at)
            # Check if FileStorage save method is called
            mock_save.assert_called_once()

    def test_base_model_to_dict(self):
        """Test to_dict method of BaseModel."""
        new_model = BaseModel()
        obj_dict = new_model.to_dict()

        # Check if the keys are present
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

        # Check if values are correct types
        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIsInstance(obj_dict['__class__'], str)

    def test_base_model_init_with_arguments(self):
        """Test initialization of BaseModel with arguments."""
        data = {
            'id': 'test_id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-01T12:30:00.000000',
            'name': 'Test Model'
        }

        new_model = BaseModel(**data)

        # Check if attributes are set correctly
        self.assertEqual(new_model.id, 'test_id')
        self.assertEqual(new_model.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(new_model.updated_at, datetime(2023, 1, 1, 12, 30, 0))
        self.assertEqual(new_model.name, 'Test Model')

        # Additional check for integration with FileStorage
        with patch('models.engine.file_storage.FileStorage.new') as mock_new:
            new_model = BaseModel(**data)

            # Check if FileStorage new method is called
            mock_new.assert_called_once_with(new_model)

if __name__ == '__main__':
    unittest.main()
