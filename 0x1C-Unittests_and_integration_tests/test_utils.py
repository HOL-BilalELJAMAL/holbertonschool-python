#!/usr/bin/env python3
"""
module
"""


from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    unit testing for access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1), 
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, in1, in2, out):
        """
        Test case
        """
        self.assertEqual(access_nested_map(in1, in2), out)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, in1, in2, exception):
        """
        test case for exception
        """
        with self.assertRaises(exception):
            access_nested_map(in1, in2)


class TestGetJson(unittest.TestCase):
    """
    test cases for get_json
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        test method
        """
        mock = Mock()
        mock.json.return_value = test_payload
        with unittest.mock.patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
            mock.json.assert_called_once_with()


class TestMemoize(unittest.TestCase):
    """
    unittest for memoize
    """

    def test_memoize(self):
        """
        method
        """

        class TestClass:
            """TestClass"""

            def a_method(self):
                """a_method"""

                return 42

            @memoize
            def a_property(self):
                """a_property"""

                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_a_method:
            test = TestClass()
            test.a_property
            test.a_property

            self.assertEqual(test.a_property, 42)
            mock_a_method.assert_called_once()
