#!/usr/bin/env python3
'''
Test utils module
'''


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''
    TestAccessNestedMap class
    '''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        test_access_nested_map method
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), "a"),
        ({'a': 1}, ('a', 'b'), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''
        test_access_nested_map_exception method
        '''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    TestGetJson class
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''
        test_get_json method
        '''
        class MockResponse:
            '''
            MockResponse class
            '''
            def json(self):
                '''
                json method
                '''
                return test_payload

        with patch('requests.get') as mock_get:
            mock_get.return_value = MockResponse()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''
    TestMemoize class
    '''
    def test_memoize(self):
        '''
        test_memoize method
        '''
        class TestClass:
            '''
            TestClass class
            '''
            def a_method(self):
                '''
                a_method method
                '''
                return 42

            @memoize
            def a_property(self):
                '''
                a_property method
                '''
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock_method.assert_called_once()
