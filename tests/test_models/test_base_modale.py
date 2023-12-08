import json
import os
import unittest
from datetime import datetime
from io import StringIO
import sys
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.filepath = FileStorage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up the test environment."""
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    def test_basemodel_init(self):
        """Test BaseModel initialization."""
        new = BaseModel()
        # Your existing test assertions for BaseModel.__init__()

    def test_basemodel_init2(self):
        """Test BaseModel initialization with dictionary."""
        new = BaseModel()
        new.name = "John"
        new.my_number = 89
        new2 = BaseModel(**new.to_dict())
        # Your existing test assertions for BaseModel.__init2__()

    def test_basemodel_init3(self):
        """Test BaseModel initialization with updated attributes."""
        new = BaseModel()
        new2 = BaseModel(new.to_dict())
        # Your existing test assertions for BaseModel.__init3__()

    def test_save_storage(self):
        """Test BaseModel save method and storage interaction."""
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(self.filepath))
        with open(self.filepath, "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    # Add more test cases as needed

class TestBase(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Clean up the test environment."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization_positive(self):
        """Test positive cases for BaseModel initialization."""
        # Your existing test assertions for TestBase.test_initialization_positive()

    def test_dict(self):
        """Test BaseModel to_dict method."""
        # Your existing test assertions for TestBase.test_dict()

    def test_save(self):
        """Test BaseModel save method."""
        # Your existing test assertions for TestBase.test_save()

    def test_save_storage(self):
        """Test BaseModel save method and storage interaction."""
        # Your existing test assertions for TestBase.test_save_storage()

    def test_str(self):
        """Test BaseModel __str__ method."""
        # Your existing test assertions for TestBase.test_str()

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
