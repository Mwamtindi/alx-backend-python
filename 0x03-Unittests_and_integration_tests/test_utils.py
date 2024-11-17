#!/usr/bin/env python3
"""
Unit tests for the utils module.
This module tests access_nested_map, get_json, & memoize functions
to ensure they work as expected.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns expected value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception_ou):
        """Test that access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(exception_ou, e.exception)


class TestGetJson(unittest.TestCase):
    """ Test cases for get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json fetches JSON content from a URL."""
        # Mock obj with json method that returns test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response):
            # Call get_json function with the test_url
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            # Assert  get method was called once with test_url
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test cases for memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches method results."""
        class TestClass:
            """Test class for memoize."""
            def a_method(self):
                """Return a constant value."""
                return 42

            @memoize
            def a_property(self):
                """Memoized property returning a_method result"""
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            result = test_class.a_property

            self.assertEqual(result, 42)
            patched.assert_called_once()


if __name__ == "__main__":
    unittest.main()
