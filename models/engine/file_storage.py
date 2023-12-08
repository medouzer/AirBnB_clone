#!/usr/bin/python3
"""Store first object"""
import json
from models.base_model import BaseModel

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
    #     try:
    #         with open(self.__file_path, 'r') as file:
    #             data = json.load(file)
    #             for key, obj_data in data.items():
    #                 class_name = obj_data['__class__']
    #                 del obj_data['__class__']
    #                 obj_instance = eval(class_name)(**obj_data)
    #                 self.__objects[key] = obj_instance
    #     except FileNotFoundError:
    #         pass
    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                file_content = file.read()
                print("File Content:", file_content)  # Add this line for debugging
                if file_content.strip():  # Check if the file is not empty
                    data = json.loads(file_content)
                    for key, obj_data in data.items():
                        class_name = obj_data['__class__']
                        del obj_data['__class__']
                        obj_instance = eval(class_name)(**obj_data)
                        self.__objects[key] = obj_instance
        except FileNotFoundError:
            # File not found, no need for an error
            pass
        except json.decoder.JSONDecodeError as e:
            # Handle JSON decoding error (if any)
            print(f"Error decoding JSON: {e}")
