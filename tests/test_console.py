# import unittest
# from unittest.mock import patch
# from io import StringIO
# from console import HBNBCommand
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# from models import storage


# class TestHBNBCommandPrompt(unittest.TestCase):
#     """Testing prompting of the HBNB command interpreter."""

#     def test_prompt_string(self):
#         self.assertEqual("(hbnb) ", HBNBCommand.prompt)

#     def test_empty_line(self):
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd(""))
#             self.assertEqual("", output.getvalue().strip())


# class TestHBNBCommandHelp(unittest.TestCase):
#     """Testing help messages of the HBNB command interpreter."""

#     def test_help(self):
#         h = ("Documented commands (type help <topic>):\n"
#              "========================================\n"
#              "EOF  all  clear  create  destroy  help  quit  show  update")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help"))
#             self.assertEqual(h, output.getvalue().strip())

#     def test_help_quit(self):
#         msg = "Quit command to exit the program"
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help quit"))
#             self.assertEqual(msg, output.getvalue().strip())

#     def test_help_EOF(self):
#         msg = "Ctrl-D to exit the program"
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help EOF"))
#             self.assertEqual(msg, output.getvalue().strip())

#     # Add other help tests as needed

#     def test_help_create(self):
#         msg = ("Creates a new instance :\n"
#                "Usage: create <class name>")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help create"))
#             self.assertEqual(msg, output.getvalue().strip())

#     def test_help_show(self):
#         msg = ("Prints the string representation of an instance\n"
#                "Usage: show <class name> <id>")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help show"))
#             self.assertEqual(msg, output.getvalue().strip())

#     def test_help_destroy(self):
#         h = ("Deletes an instance\n"
#              "Usage: destroy <class name> <id>")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help destroy"))
#             self.assertEqual(h, output.getvalue().strip())

#     def test_help_all(self):
#         h = ("Prints all string representation of all\n"
#              "instances based or not on the class name\n"
#              "Usage1: all\n"
#              "Usage2: all <class name>")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help all"))
#             self.assertEqual(h, output.getvalue().strip())

#     def test_help_update(self):
#         h = ("Updates an instance by adding or updating attribute\n")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help update"))
#             self.assertEqual(h, output.getvalue().strip())


# class ConsoleTestCase(unittest.TestCase):
#     """Testing errors and create object functionality"""

#     def test_error(self):
#         """Testing errors"""
#         cmd_classname = ["create", "update", "show", "destroy"]
#         cmd_id = ["update", "show", "destroy"]
#         cmd_attr = ["update"]

#         """ class name missing """
#         for cmd in cmd_classname:
#             with patch('sys.stdout', new=StringIO()) as f:
#                 expected = "** class name missing **"
#                 HBNBCommand().onecmd(cmd)
#                 self.assertCountEqual(expected, f.getvalue().strip())

#         """ class doesn't exist """
#         class_dont_exist = ["create x", "update x",
#                             "show x", "destroy x", "all x"]
#         for cmd in class_dont_exist:
#             with patch('sys.stdout', new=StringIO()) as f:
#                 expected = "** class doesn't exist **"
#                 HBNBCommand().onecmd(cmd)
#                 self.assertCountEqual(expected, f.getvalue().strip())

#         """ instance id missing """
#         cmds = ["update", "show", "destroy"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     expected = "** instance id missing **"
#                     HBNBCommand().onecmd(f"{cmd} {clas}")
#                     self.assertCountEqual(expected, f.getvalue().strip())

#         """ no instance found """
#         cmds = ["update", "show", "destroy"]
#         valid_classes = HBNBCommand().valid_classes
#         wrong_id = "x"
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     expected = "** no instance found **"
#                     HBNBCommand().onecmd(f"{cmd} {clas} {wrong_id}")
#                     self.assertCountEqual(expected, f.getvalue().strip())

#     def test_create_object(self):
#         """Testing for create """
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
#             key = "BaseModel.{}".format(output.getvalue().strip())
#             self.assertIn(key, storage.all().keys())

#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("create User"))
#             key = "User.{}".format(output.getvalue().strip())
#             self.assertIn(key, storage.all().keys())

#         # Add other create tests for different classes

#         """Value missing"""
#         new_BaseModel = BaseModel()
#         new_User = User()
#         new_State = State()
#         new_City = City()
#         new_Amenity = Amenity()
#         new_Place = Place()
#         new_Review = Review()
#         id_BaseModel = new_BaseModel.id
#         id_User = new_User.id
#         id_State = new_State.id
#         id_City = new_City.id
#         id_Amenity = new_Amenity.id
#         id_Place = new_Place.id
#         id_Review = new_Review.id
#         id_dict = {"BaseModel": id_BaseModel, "User": id_User,
#                    "State": id_State, "City": id_City, "Amenity": id_Amenity,
#                    "Place": id_Place, "Review": id_Review}
#         cmds = ["update"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     expected = "** value missing **"
#                     HBNBCommand().onecmd(
#                         f"{cmd} {clas} {id_dict[clas]} name")
#                     self.assertCountEqual(expected, f.getvalue().strip())

#         """ Testing Show Command """
#         cmds = ["show"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]}")
#                     expected = str(new_BaseModel)
#                     if clas == "User":
#                         expected = str(new_User)
#                     # Add other expected outputs based on the class
#                     self.assertIn(expected, f.getvalue().strip())

#         """ Testing Destroy Command """
#         cmds = ["destroy"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]}")
#                     self.assertNotIn(id_dict[clas], storage.all().keys())

#         """ Testing All Command """
#         cmds = ["all"]
#         for cmd in cmds:
#             with patch('sys.stdout', new=StringIO()) as f:
#                 HBNBCommand().onecmd(f"{cmd}")
#                 expected = ['[{}] {}'.format(k, v)
#                             for k, v in storage.all().items()]
#                 self.assertEqual(expected, f.getvalue().strip())

#         """ Testing Update Command """
#         cmds = ["update"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     HBNBCommand().onecmd(
#                         f"{cmd} {clas} {id_dict[clas]} name 'New Name'")
#                     expected = 'New Name'
#                     if clas == "User":
#                         expected = "New Name"
#                     # Add other expected outputs based on the class
#                     self.assertEqual(expected, getattr(storage.all()[
#                         f"{clas}.{id_dict[clas]}"], "name"))

# # ... (If you have other tests or code after this point)


# if __name__ == '__main__':
#     unittest.main()

# hgtzhbvgfcdrdfcfcut
# import unittest
# from unittest.mock import patch
# from io import StringIO
# from console import HBNBCommand
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# from models import storage


# class TestHBNBCommandPrompt(unittest.TestCase):
#     """Testing prompting of the HBNB command interpreter."""

#     def test_prompt_string(self):
#         self.assertEqual("(hbnb) ", HBNBCommand.prompt)

#     def test_empty_line(self):
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd(""))
#             self.assertEqual("", output.getvalue().strip())


# class TestHBNBCommandHelp(unittest.TestCase):
#     """Testing help messages of the HBNB command interpreter."""

#     def test_help(self):
#         h = ("Documented commands (type help <topic>):\n"
#              "========================================\n"
#              "EOF  all  clear  create  destroy  help  quit  show  update")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help"))
#             self.assertEqual(h, output.getvalue().strip())

#     def test_help_quit(self):
#         msg = "Quit command to exit the program"
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help quit"))
#             self.assertEqual(msg, output.getvalue().strip())

#     def test_help_EOF(self):
#         msg = "Ctrl-D to exit the program"
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help EOF"))
#             self.assertEqual(msg, output.getvalue().strip())

#     # Add other help tests as needed

#     def test_help_create(self):
#         msg = ("Creates a new instance :\n"
#                "Usage: create <class name>")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help create"))
#             self.assertEqual(msg, output.getvalue().strip())

#     def test_help_show(self):
#         msg = ("Prints the string representation of an instance\n"
#                "Usage: show <class name> <id>")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help show"))
#             self.assertEqual(msg, output.getvalue().strip())

#     def test_help_destroy(self):
#         h = ("Deletes an instance\n"
#              "Usage: destroy <class name> <id>")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help destroy"))
#             self.assertEqual(h, output.getvalue().strip())

#     def test_help_all(self):
#         h = ("Prints all string representation of all\n"
#              "instances based or not on the class name\n"
#              "Usage1: all\n"
#              "Usage2: all <class name>")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help all"))
#             self.assertEqual(h, output.getvalue().strip())

#     def test_help_update(self):
#         h = ("Updates an instance by
# adding or updating attribute\n"
#              "Usage: update <class name>
# <id><attribute name> \"<attribute value>\"")
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help update"))
#             self.assertEqual(h, output.getvalue().strip())


# class ConsoleTestCase(unittest.TestCase):
#     """Testing errors and create object functionality"""

#     def test_error(self):
#         """Testing errors"""
#         cmd_classname = ["create", "update", "show", "destroy"]
#         cmd_id = ["update", "show", "destroy"]
#         cmd_attr = ["update"]

#         """ class name missing """
#         for cmd in cmd_classname:
#             with patch('sys.stdout', new=StringIO()) as f:
#                 expected = "** class name missing **"
#                 HBNBCommand().onecmd(cmd)
#                 self.assertEqual(expected, f.getvalue().strip())

#         """ class doesn't exist """
#         class_dont_exist = ["create x", "update x",
#                             "show x", "destroy x", "all x"]
#         for cmd in class_dont_exist:
#             with patch('sys.stdout', new=StringIO()) as f:
#                 expected = "** class doesn't exist **"
#                 HBNBCommand().onecmd(cmd)
#                 self.assertEqual(expected, f.getvalue().strip())

#         """ instance id missing """
#         cmds = ["update", "show", "destroy"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     expected = "** instance id missing **"
#                     HBNBCommand().onecmd(f"{cmd} {clas}")
#                     self.assertEqual(expected, f.getvalue().strip())

#         """ no instance found """
#         cmds = ["update", "show", "destroy"]
#         valid_classes = HBNBCommand().valid_classes
#         wrong_id = "x"
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     expected = "** no instance found **"
#                     HBNBCommand().onecmd(f"{cmd} {clas} {wrong_id}")
#                     self.assertEqual(expected, f.getvalue().strip())

#     def test_create_object(self):
#         """Testing for create """
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
#             key = "BaseModel.{}".format(output.getvalue().strip())
#             self.assertIn(key, storage.all().keys())

#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("create User"))
#             key = "User.{}".format(output.getvalue().strip())
#             self.assertIn(key, storage.all().keys())

#         # Add other create tests for different classes

#         """Value missing"""
#         new_BaseModel = BaseModel()
#         new_User = User()
#         new_State = State()
#         new_City = City()
#         new_Amenity = Amenity()
#         new_Place = Place()
#         new_Review = Review()
#         id_BaseModel = new_BaseModel.id
#         id_User = new_User.id
#         id_State = new_State.id
#         id_City = new_City.id
#         id_Amenity = new_Amenity.id
#         id_Place = new_Place.id
#         id_Review = new_Review.id
#         id_dict = {"BaseModel": id_BaseModel, "User": id_User,
#                    "State": id_State, "City": id_City, "Amenity": id_Amenity,
#                    "Place": id_Place, "Review": id_Review}
#         cmds = ["update"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     expected = "** value missing **"
#                     HBNBCommand().onecmd(
# f"{cmd} {clas} {id_dict[clas]} name")
#                     self.assertEqual(expected, f.getvalue().strip())

#         """ Testing Show Command """
#         cmds = ["show"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]}")
#                     expected = str(new_BaseModel)
#                     if clas == "User":
#                         expected = str(new_User)
#                     # Add other expected outputs based on the class
#                     self.assertIn(expected, f.getvalue().strip())

#         """ Testing Destroy Command """
#         cmds = ["destroy"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]}")
#                     self.assertNotIn(id_dict[clas], storage.all().keys())

#         """ Testing All Command """
#         cmds = ["all"]
#         for cmd in cmds:
#             with patch('sys.stdout', new=StringIO()) as f:
#                 HBNBCommand().onecmd(f"{cmd}")
#                 expected = ['[{}] {}'.format(k, v)
#                             for k, v in storage.all().items()]
#                 self.assertEqual(expected, f.getvalue().strip())

#         """ Testing Update Command """
#         cmds = ["update"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     HBNBCommand().onecmd(
# f"{cmd} {clas}{id_dict[clas]} name 'New Name'")
#                     expected = 'New Name'
#                     if clas == "User":
#                         expected = "New Name"
#                     # Add other expected outputs based on the class
#                     self.assertEqual(expected, getattr(storage.all()
#                               [f"{clas}.{id_dict[clas]}"], "name"))


# if __name__ == '__main__':
#     unittest.main()

# import unittest
# from unittest.mock import patch
# from io import StringIO
# from console import HBNBCommand
# from models.base_model import BaseModel
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review
# from models import storage


# class TestHBNBCommandPrompt(unittest.TestCase):
#     def test_prompt_string(self):
#         self.assertEqual("(hbnb) ", HBNBCommand.prompt)

#     def test_empty_line(self):
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd(""))
#             self.assertEqual("", output.getvalue().strip())


# class TestHBNBCommandHelp(unittest.TestCase):
#     def test_help(self):
#         expected_output = (
#             "Documented commands (type help <topic>):\n"
#             "========================================\n"
#             "EOF  all  create  destroy  help  quit  show  update"
#         )

#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("help"))
#             self.assertEqual(expected_output, output.getvalue().strip())


# class TestHBNBCommandErrors(unittest.TestCase):
#     def test_class_name_missing(self):
#         cmd_list = ["create", "update", "show", "destroy"]
#         for cmd in cmd_list:
#             with patch('sys.stdout', new=StringIO()) as f:
#                 expected = "** class name missing **"
#                 HBNBCommand().onecmd(cmd)
#                 self.assertEqual(expected, f.getvalue().strip())


# class TestHBNBCommandCreateObject(unittest.TestCase):

#     def test_create_object(self):
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
#             key = "BaseModel.{}".format(output.getvalue().strip())
#             self.assertIn(key, storage.all().keys())

#         # Add similar test methods for other classes...

#     def test_value_missing(self):
#         new_base_model = BaseModel()
#         id_base_model = new_base_model.id
#         with patch('sys.stdout', new=StringIO()) as f:
#             expected = "** value missing **"
#             HBNBCommand().onecmd(f"update BaseModel {id_base_model} name")
#             self.assertEqual(expected, f.getvalue().strip())


# if __name__ == '__main__':
#     unittest.main()
# //////////

# import unittest
# from unittest.mock import patch
# from io import StringIO
# from console import HBNBCommand
# from models.base_model import BaseModel
# from models import storage
# import models


# class TestHBNBCommand(unittest.TestCase):
#     def setUp(self):
#         self.cmd = HBNBCommand()

#     def test_create_instance(self):
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.cmd.onecmd("create BaseModel")
#             created_instance_id = output.getvalue().strip()
#             self.assertIn(created_instance_id, storage.all())
#             self.assertIsInstance(storage.all()[created_instance_id], BaseModel)

#     def test_show_instance(self):
#         test_instance = BaseModel()
#         test_instance.id = "test_id"
#         models.storage.save()

#         with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
#             self.cmd.onecmd("show BaseModel test_id")
#             expected_output = f"[BaseModel] (test_id) {test_instance.to_dict()}"
#             actual_output = mock_stdout.getvalue().strip()

#             # Check if the expected output is in the actual output
#             self.assertIn(expected_output, actual_output)

#             # Check if the actual output is not 'no instance found'
#             self.assertNotEqual('** no instance found **', actual_output)





#     def test_quit_command(self):
#         with patch("builtins.input", return_value='EOF'):
#             with self.assertRaises(SystemExit):
#                 self.cmd.cmdloop()

#     def test_invalid_command(self):
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.cmd.onecmd("invalid_command")
#             self.assertIn("invalid_command", output.getvalue().strip())

#     def test_empty_line(self):
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.assertFalse(self.cmd.onecmd(""))
#             self.assertEqual("", output.getvalue().strip())

#     def test_help_command(self):
#         with patch("sys.stdout", new=StringIO()) as output:
#             self.cmd.onecmd("help")
#             self.assertIn("Documented commands", output.getvalue().strip())


# if __name__ == '__main__':
#     unittest.main()

# hada test akhor mn 3alam khor hhhh

#!/usr/bin/python3
"""Defines unittests for console.py.
"""
from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Base class for testing Console.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_simple(self):
        """Tests basic commands.
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("?")
            self.assertIsInstance(f.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIsInstance(f.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Prints string representation of all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Prints string representation of all instances.")

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Prints the string representation of an instance."
            HBNBCommand().onecmd("? show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Prints the string representation of an instance."
            HBNBCommand().onecmd("help show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Updates an instance based on the class name and id."
            HBNBCommand().onecmd("? update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Updates an instance based on the class name and id."
            HBNBCommand().onecmd("help update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Deletes an instance based on the class name and id."
            HBNBCommand().onecmd("? destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as f:
            msg = "Deletes an instance based on the class name and id."
            HBNBCommand().onecmd("help destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "To get help on a command, type help <topic>.")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "To get help on a command, type help <topic>.")


class TestBaseModel(unittest.TestCase):
    """Testing `Basemodel `commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_basemodel(self):
        """Test all basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all BaseModel')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "green"
            HBNBCommand().onecmd(f'show BaseModel {b1.id}')
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            HBNBCommand().onecmd(f'update BaseModel {b1.id} name "Ife"')
            self.assertEqual(b1.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            HBNBCommand().onecmd(f'update BaseModel {b1.id} age 25')
            self.assertIn("age", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.savings = 25.67
            HBNBCommand().onecmd(f'update BaseModel {b1.id} savings 35.89')
            self.assertIn("savings", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 60
            cmmd = f'update BaseModel {b1.id} age 10 color "green"'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", b1.__dict__.keys())
            self.assertNotIn("color", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 10)

    def test_destroy_basemodel(self):
        """Test destroy basemodel object.
        """
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(f'destroy BaseModel {bm.id}')
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.all().keys())


class TestBaseModelDotNotation(unittest.TestCase):
    """Testing `Basemodel `commands using dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """Test create basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'BaseModel.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_basemodel(self):
        """Test count basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == BaseModel:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_basemodel(self):
        """Test all basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('BaseModel.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[BaseModel]')

    def test_show_basemodel(self):
        """Test show basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.show({b1.id})'))
            res = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_basemodel(self):
        """Test update basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, name, "Ife")'))
            self.assertEqual(b1.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.update({b1.id}, age, 25)'))
            self.assertIn("age", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 60
            cmmd = f'BaseModel.update({b1.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", b1.__dict__.keys())
            self.assertNotIn("color", b1.__dict__.keys())
            self.assertEqual(b1.__dict__["age"], 10)

    def test_update_basemodel_dict(self):
        """Test update basemodel object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            b1 = BaseModel()
            b1.age = 75
            cmmd = f'BaseModel.update({b1.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(b1.__dict__["age"], 25)
            self.assertIsInstance(b1.__dict__["age"], int)

    def test_destroy_basemodel(self):
        """Test destroy basemodel object.
        """
        with patch('sys.stdout', new=StringIO()):
            bm = BaseModel()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'BaseModel.destroy({bm.id})'))
            self.assertNotIn("BaseModel.{}".format(
                bm.id), storage.all().keys())


class TestUser(unittest.TestCase):
    """Testing the `user` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_user(self):
        """Test all user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(f'show User {us.id}')
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cecilia"
            HBNBCommand().onecmd(f'update User {us.id} name "Ife"')
            self.assertEqual(us.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            HBNBCommand().onecmd(f'update User {us.id} age 25')
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.savings = 25.67
            HBNBCommand().onecmd(f'update User {us.id} savings 35.89')
            self.assertIn("savings", us.__dict__.keys())
            self.assertEqual(us.__dict__["savings"], 35.89)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'update User {us.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_destroy_user(self):
        """Test destroy user object.
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(f'destroy User {us.id}')
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())


class TestUserDotNotation(unittest.TestCase):
    """Testing the `user` command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_user(self):
        """Test create user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'User.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_user(self):
        """Test count user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == User:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_user(self):
        """Test all user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[User]')

    def test_show_user(self):
        """Test show user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.show({us.id})'))
            res = f"[{type(us).__name__}] ({us.id}) {us.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_user(self):
        """Test update user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({us.id}, name, "Ife")'))
            self.assertEqual(us.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({us.id}, age, 25)'))
            self.assertIn("age", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 60
            cmmd = f'User.update({us.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", us.__dict__.keys())
            self.assertNotIn("color", us.__dict__.keys())
            self.assertEqual(us.__dict__["age"], 10)

    def test_update_user_dict(self):
        """Test update user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            us = User()
            us.age = 75
            cmmd = f'User.update({us.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(us.__dict__["age"], 25)
            self.assertIsInstance(us.__dict__["age"], int)

    def test_destroy_user(self):
        """Test destroy user object.
        """
        with patch('sys.stdout', new=StringIO()):
            us = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.destroy({us.id})'))
            self.assertNotIn("User.{}".format(
                us.id), storage.all().keys())


class TestState(unittest.TestCase):
    """Testing the `state` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Test create state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_state(self):
        """Test all state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all State')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "green"
            HBNBCommand().onecmd(f'show State {st.id}')
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Cecilia"
            HBNBCommand().onecmd(f'update State {st.id} name "Ife"')
            self.assertEqual(st.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            HBNBCommand().onecmd(f'update State {st.id} age 25')
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'update State {st.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_destroy_state(self):
        """Test destroy state object.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(f'destroy State {st.id}')
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())


class TestStateDotNotation(unittest.TestCase):
    """Testing the `state` command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_state(self):
        """Test create state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'State.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_state(self):
        """Test count state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == State:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_state(self):
        """Test all state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('State.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[State]')

    def test_show_state(self):
        """Test show state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.show({st.id})'))
            res = f"[{type(st).__name__}] ({st.id}) {st.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_state(self):
        """Test update state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({st.id}, name, "Ife")'))
            self.assertEqual(st.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.update({st.id}, age, 25)'))
            self.assertIn("age", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 60
            cmmd = f'State.update({st.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", st.__dict__.keys())
            self.assertNotIn("color", st.__dict__.keys())
            self.assertEqual(st.__dict__["age"], 10)

    def test_update_state_dict(self):
        """Test update state object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            st = State()
            st.age = 75
            cmmd = f'State.update({st.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(st.__dict__["age"], 25)
            self.assertIsInstance(st.__dict__["age"], int)

    def test_destroy_state(self):
        """Test destroy state object.
        """
        with patch('sys.stdout', new=StringIO()):
            st = State()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'State.destroy({st.id})'))
            self.assertNotIn("State.{}".format(
                st.id), storage.all().keys())


class TestReview(unittest.TestCase):
    """Testing the `review` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Test create review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_review(self):
        """Test all review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Review')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Test show review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "green"
            HBNBCommand().onecmd(f'show Review {rv.id}')
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Test update review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Cecilia"
            HBNBCommand().onecmd(f'update Review {rv.id} name "Ife"')
            self.assertEqual(rv.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            HBNBCommand().onecmd(f'update Review {rv.id} age 25')
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'update Review {rv.id} age 10 color green)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_destroy_review(self):
        """Test destroy review object.
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(f'destroy Review {rv.id}')
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())


class TestReviewDotNotation(unittest.TestCase):
    """Testing the `review` command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_review(self):
        """Test create review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Review.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_review(self):
        """Test count review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Review:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_review(self):
        """Test all review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Review.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Review]')

    def test_show_review(self):
        """Test show review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.show({rv.id})'))
            res = f"[{type(rv).__name__}] ({rv.id}) {rv.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_review(self):
        """Test update review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, name, "Ife")'))
            self.assertEqual(rv.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.update({rv.id}, age, 25)'))
            self.assertIn("age", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 60
            cmmd = f'Review.update({rv.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", rv.__dict__.keys())
            self.assertNotIn("color", rv.__dict__.keys())
            self.assertEqual(rv.__dict__["age"], 10)

    def test_update_review_dict(self):
        """Test update review object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            rv = Review()
            rv.age = 75
            cmmd = f'Review.update({rv.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(rv.__dict__["age"], 25)
            self.assertIsInstance(rv.__dict__["age"], int)

    def test_destroy_review(self):
        """Test destroy review object.
        """
        with patch('sys.stdout', new=StringIO()):
            rv = Review()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Review.destroy({rv.id})'))
            self.assertNotIn("Review.{}".format(
                rv.id), storage.all().keys())


class TestPlace(unittest.TestCase):
    """Testing the `place` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_place(self):
        """Test create place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Place.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_place(self):
        """Test all place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Place')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Place]')

    def test_show_place(self):
        """Test show place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.eyes = "green"
            HBNBCommand().onecmd(f'show Place {pl.id}')
            res = f"[{type(pl).__name__}] ({pl.id}) {pl.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_place(self):
        """Test update place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.name = "Cecilia"
            HBNBCommand().onecmd(f'update Place {pl.id} name "Ife"')
            self.assertEqual(pl.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 75
            HBNBCommand().onecmd(f'update Place {pl.id} age 25')
            self.assertIn("age", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 60
            cmmd = f'update Place {pl.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", pl.__dict__.keys())
            self.assertNotIn("color", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 10)

    def test_destroy_place(self):
        """Test destroy place object.
        """
        with patch('sys.stdout', new=StringIO()):
            pl = Place()
            HBNBCommand().onecmd(f'destroy Place {pl.id}')
            self.assertNotIn("Place.{}".format(
                pl.id), storage.all().keys())


class TestPlaceDotNotation(unittest.TestCase):
    """Testing the `place` command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_place(self):
        """Test create place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Place.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Place.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_place(self):
        """Test count place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Place:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_place(self):
        """Test all place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Place.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Place]')

    def test_show_place(self):
        """Test show place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.show({pl.id})'))
            res = f"[{type(pl).__name__}] ({pl.id}) {pl.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_place(self):
        """Test update place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update({pl.id}, name, "Ife")'))
            self.assertEqual(pl.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.update({pl.id}, age, 25)'))
            self.assertIn("age", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 60
            cmmd = f'Place.update({pl.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", pl.__dict__.keys())
            self.assertNotIn("color", pl.__dict__.keys())
            self.assertEqual(pl.__dict__["age"], 10)

    def test_update_place_dict(self):
        """Test update place object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            pl = Place()
            pl.age = 75
            cmmd = f'Place.update({pl.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(pl.__dict__["age"], 25)
            self.assertIsInstance(pl.__dict__["age"], int)

    def test_destroy_place(self):
        """Test destroy place object.
        """
        with patch('sys.stdout', new=StringIO()):
            pl = Place()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Place.destroy({pl.id})'))
            self.assertNotIn("Place.{}".format(
                pl.id), storage.all().keys())


class TestAmenity(unittest.TestCase):
    """Testing the `amenity` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_amenity(self):
        """Test create amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Amenity.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_amenity(self):
        """Test all amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all Amenity')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Amenity]')

    def test_show_amenity(self):
        """Test show amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.eyes = "green"
            HBNBCommand().onecmd(f'show Amenity {am.id}')
            res = f"[{type(am).__name__}] ({am.id}) {am.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_amenity(self):
        """Test update amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.name = "Cecilia"
            HBNBCommand().onecmd(f'update Amenity {am.id} name "Ife"')
            self.assertEqual(am.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 75
            HBNBCommand().onecmd(f'update Amenity {am.id} age 25')
            self.assertIn("age", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 60
            cmmd = f'update Amenity {am.id} age 10 color green)'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", am.__dict__.keys())
            self.assertNotIn("color", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 10)

    def test_destroy_amenity(self):
        """Test destroy amenity object.
        """
        with patch('sys.stdout', new=StringIO()):
            am = Amenity()
            HBNBCommand().onecmd(f'destroy Amenity {am.id}')
            self.assertNotIn("Amenity.{}".format(
                am.id), storage.all().keys())


class TestAmenityDotNotation(unittest.TestCase):
    """Testing the `amenity` command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_amenity(self):
        """Test create amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'Amenity.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("Amenity.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_amenity(self):
        """Test count amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == Amenity:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_amenity(self):
        """Test all amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('Amenity.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[Amenity]')

    def test_show_amenity(self):
        """Test show amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.show({am.id})'))
            res = f"[{type(am).__name__}] ({am.id}) {am.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_amenity(self):
        """Test update amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update({am.id}, name, "Ife")'))
            self.assertEqual(am.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.update({am.id}, age, 25)'))
            self.assertIn("age", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 60
            cmmd = f'Amenity.update({am.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", am.__dict__.keys())
            self.assertNotIn("color", am.__dict__.keys())
            self.assertEqual(am.__dict__["age"], 10)

    def test_update_amenity_dict(self):
        """Test update amenity object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            am = Amenity()
            am.age = 75
            cmmd = f'Amenity.update({am.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(am.__dict__["age"], 25)
            self.assertIsInstance(am.__dict__["age"], int)

    def test_destroy_amenity(self):
        """Test destroy amenity object.
        """
        with patch('sys.stdout', new=StringIO()):
            am = Amenity()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'Amenity.destroy({am.id})'))
            self.assertNotIn("Amenity.{}".format(
                am.id), storage.all().keys())


class TestCity(unittest.TestCase):
    """Testing the `city` commands.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_city(self):
        """Test create city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City')
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("City.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_city(self):
        """Test all city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all City')
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[City]')

    def test_show_city(self):
        """Test show city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.eyes = "green"
            HBNBCommand().onecmd(f'show City {cty.id}')
            res = f"[{type(cty).__name__}] ({cty.id}) {cty.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_city(self):
        """Test update city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.name = "Cecilia"
            HBNBCommand().onecmd(f'update City {cty.id} name "Ife"')
            self.assertEqual(cty.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 75
            HBNBCommand().onecmd(f'update City {cty.id} age 25')
            self.assertIn("age", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 60
            cmmd = f'update City {cty.id} age 10 color green'
            HBNBCommand().onecmd(cmmd)
            self.assertIn("age", cty.__dict__.keys())
            self.assertNotIn("color", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 10)

    def test_destroy_city(self):
        """Test destroy city object.
        """
        with patch('sys.stdout', new=StringIO()):
            cty = City()
            HBNBCommand().onecmd(f'destroy City {cty.id}')
            self.assertNotIn("City.{}".format(
                cty.id), storage.all().keys())


class TestCityDotNotation(unittest.TestCase):
    """Testing the `city` command's dot notation.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_city(self):
        """Test create city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'City.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("City.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_city(self):
        """Test count city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == City:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_city(self):
        """Test all city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('City.all()'))
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], '[City]')

    def test_show_city(self):
        """Test show city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.eyes = "green"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.show({cty.id})'))
            res = f"[{type(cty).__name__}] ({cty.id}) {cty.__dict__}"
            self.assertEqual(f.getvalue().strip(), res)

    def test_update_city(self):
        """Test update city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.name = "Cecilia"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update({cty.id}, name, "Ife")'))
            self.assertEqual(cty.__dict__["name"], "Ife")

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 75
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.update({cty.id}, age, 25)'))
            self.assertIn("age", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 25)

        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 60
            cmmd = f'City.update({cty.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", cty.__dict__.keys())
            self.assertNotIn("color", cty.__dict__.keys())
            self.assertEqual(cty.__dict__["age"], 10)

    def test_update_city_dict(self):
        """Test update city object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            cty = City()
            cty.age = 75
            cmmd = f'City.update({cty.id}, {{"age": 25,"color":"black"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(cty.__dict__["age"], 25)
            self.assertIsInstance(cty.__dict__["age"], int)

    def test_destroy_city(self):
        """Test destroy city object.
        """
        with patch('sys.stdout', new=StringIO()):
            cty = City()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'City.destroy({cty.id})'))
            self.assertNotIn("City.{}".format(
                cty.id), storage.all().keys())