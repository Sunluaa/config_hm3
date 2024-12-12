import unittest
from main import ConfigParser

class TestConfigParser(unittest.TestCase):

    def setUp(self):
        self.parser = ConfigParser()

    def test_parse_set(self):
        """Тестирует корректность парсинга нескольких строк с оператором 'set'."""
        input_text = """
        set my_var = 42;
        set my_float = 3.14;
        set my_string = "Hello";
        """
        self.parser.parse(input_text)
        self.assertEqual(self.parser.constants["my_var"], 42)
        self.assertEqual(self.parser.constants["my_float"], 3.14)
        self.assertEqual(self.parser.constants["my_string"], "Hello")

    def test_parse_list(self):
        """Тестирует корректность парсинга списков."""
        input_text = """
        set my_list = list(1, 2, 3, 4);
        set another_list = list("a", "b", "c");
        """
        self.parser.parse(input_text)
        self.assertEqual(self.parser.constants["my_list"], [1, 2, 3, 4])
        self.assertEqual(self.parser.constants["another_list"], ["a", "b", "c"])

    def test_parse_table(self):
        """Тестирует корректность парсинга таблиц."""
        input_text = """
        set my_table = table([key1=1, key2=2, key3=3]);
        set nested_table = table([outer_key=table([inner_key=42])]);
        """
        self.parser.parse(input_text)
        self.assertEqual(self.parser.constants["my_table"], {
            "key1": 1,
            "key2": 2,
            "key3": 3
        })
        self.assertEqual(self.parser.constants["nested_table"], {
            "outer_key": {"inner_key": 42}
        })

if __name__ == "__main__":
    unittest.main()
