#!/usr/bin/python3
"""Store first object"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary"""
        return self.__objects

    def new(self, obj):
        """set in __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """store object int a json file"""
        data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    # def reload(self):
    #     if os.path.exists(self.__file_path):
    #         try:
    #             with open(self.__file_path, 'r') as file:
    #                 file_content = file.read()
    #                 if file_content.strip():  # Check if the file is not empty
    #                     data = json.loads(file_content)
    #                     for key, obj_data in data.items():
    #                         class_name = obj_data['__class__']
    #                         del obj_data['__class__']

    #                         class_mapping = {
    #                             'BaseModel': BaseModel,
    #                             'User': User,
    #                             'State': State,
    #                             'City': City,
    #                             'Amenity': Amenity,
    #                             'Place': Place,
    #                             'Review': Review
    #                         }

    #                         if class_name in class_mapping:
    #                             obj_instance = class_mapping[class_name](
    #                                 **obj_data)
    #                             self.__objects[key] = obj_instance
    #                         else:
    #                             print(f"Error: Class '{class_name}' not found.")
    #         except Exception:
    #             pass

    # def reload(self):
    #     if os.path.exists(self.__file_path):
    #         try:
    #             with open(self.__file_path, 'r') as file:
    #                 data = json.load(file)
    #                 for key, obj_data in data.items():
    #                     class_name = obj_data['__class__']
    #                     del obj_data['__class__']
    #                     obj_instance = globals()[class_name](**obj_data)
    #                     self.__objects[key] = obj_instance
    #         except Exception as e:
    #             print(f"Error during reload: {str(e)}")
    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
