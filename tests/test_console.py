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
#         h = ("Updates an instance by adding or updating attribute\n"
#              "Usage: update <class name> <id> <attribute name> \"<attribute value>\"")
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
#                     HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]} name")
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
#                 expected = ['[{}] {}'.format(k, v) for k, v in storage.all().items()]
#                 self.assertEqual(expected, f.getvalue().strip())

#         """ Testing Update Command """
#         cmds = ["update"]
#         valid_classes = HBNBCommand().valid_classes
#         for cmd in cmds:
#             for clas in valid_classes:
#                 with patch('sys.stdout', new=StringIO()) as f:
#                     HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]} name 'New Name'")
#                     expected = 'New Name'
#                     if clas == "User":
#                         expected = "New Name"
#                     # Add other expected outputs based on the class
#                     self.assertEqual(expected, getattr(storage.all()[f"{clas}.{id_dict[clas]}"], "name"))

# # ... (If you have other tests or code after this point)

# if __name__ == '__main__':
#     unittest.main()
# hgtzhbvgfcdrdfcfcut
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestHBNBCommandPrompt(unittest.TestCase):
    """Testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommandHelp(unittest.TestCase):
    """Testing help messages of the HBNB command interpreter."""

    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  clear  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_quit(self):
        msg = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_EOF(self):
        msg = "Ctrl-D to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(msg, output.getvalue().strip())

    # Add other help tests as needed

    def test_help_create(self):
        msg = ("Creates a new instance :\n"
               "Usage: create <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_show(self):
        msg = ("Prints the string representation of an instance\n"
               "Usage: show <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_help_destroy(self):
        h = ("Deletes an instance\n"
             "Usage: destroy <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        h = ("Prints all string representation of all\n"
             "instances based or not on the class name\n"
             "Usage1: all\n"
             "Usage2: all <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        h = ("Updates an instance by adding or updating attribute\n"
             "Usage: update <class name> <id><attribute name> \"<attribute value>\"")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())


class ConsoleTestCase(unittest.TestCase):
    """Testing errors and create object functionality"""

    def test_error(self):
        """Testing errors"""
        cmd_classname = ["create", "update", "show", "destroy"]
        cmd_id = ["update", "show", "destroy"]
        cmd_attr = ["update"]

        """ class name missing """
        for cmd in cmd_classname:
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class name missing **"
                HBNBCommand().onecmd(cmd)
                self.assertEqual(expected, f.getvalue().strip())

        """ class doesn't exist """
        class_dont_exist = ["create x", "update x",
                            "show x", "destroy x", "all x"]
        for cmd in class_dont_exist:
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class doesn't exist **"
                HBNBCommand().onecmd(cmd)
                self.assertEqual(expected, f.getvalue().strip())

        """ instance id missing """
        cmds = ["update", "show", "destroy"]
        valid_classes = HBNBCommand().valid_classes
        for cmd in cmds:
            for clas in valid_classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** instance id missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas}")
                    self.assertEqual(expected, f.getvalue().strip())

        """ no instance found """
        cmds = ["update", "show", "destroy"]
        valid_classes = HBNBCommand().valid_classes
        wrong_id = "x"
        for cmd in cmds:
            for clas in valid_classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** no instance found **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {wrong_id}")
                    self.assertEqual(expected, f.getvalue().strip())

    def test_create_object(self):
        """Testing for create """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            key = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            key = "User.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())

        # Add other create tests for different classes

        """Value missing"""
        new_BaseModel = BaseModel()
        new_User = User()
        new_State = State()
        new_City = City()
        new_Amenity = Amenity()
        new_Place = Place()
        new_Review = Review()
        id_BaseModel = new_BaseModel.id
        id_User = new_User.id
        id_State = new_State.id
        id_City = new_City.id
        id_Amenity = new_Amenity.id
        id_Place = new_Place.id
        id_Review = new_Review.id
        id_dict = {"BaseModel": id_BaseModel, "User": id_User,
                   "State": id_State, "City": id_City, "Amenity": id_Amenity,
                   "Place": id_Place, "Review": id_Review}
        cmds = ["update"]
        valid_classes = HBNBCommand().valid_classes
        for cmd in cmds:
            for clas in valid_classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** value missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]} name")
                    self.assertEqual(expected, f.getvalue().strip())

        """ Testing Show Command """
        cmds = ["show"]
        valid_classes = HBNBCommand().valid_classes
        for cmd in cmds:
            for clas in valid_classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]}")
                    expected = str(new_BaseModel)
                    if clas == "User":
                        expected = str(new_User)
                    # Add other expected outputs based on the class
                    self.assertIn(expected, f.getvalue().strip())

        """ Testing Destroy Command """
        cmds = ["destroy"]
        valid_classes = HBNBCommand().valid_classes
        for cmd in cmds:
            for clas in valid_classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]}")
                    self.assertNotIn(id_dict[clas], storage.all().keys())

        """ Testing All Command """
        cmds = ["all"]
        for cmd in cmds:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"{cmd}")
                expected = ['[{}] {}'.format(k, v)
                            for k, v in storage.all().items()]
                self.assertEqual(expected, f.getvalue().strip())

        """ Testing Update Command """
        cmds = ["update"]
        valid_classes = HBNBCommand().valid_classes
        for cmd in cmds:
            for clas in valid_classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"{cmd} {clas}{id_dict[clas]} name 'New Name'")
                    expected = 'New Name'
                    if clas == "User":
                        expected = "New Name"
                    # Add other expected outputs based on the class
                    self.assertEqual(expected, getattr(storage.all()
                                                       [f"{clas}.{id_dict[clas]}"], "name"))


if __name__ == '__main__':
    unittest.main()
