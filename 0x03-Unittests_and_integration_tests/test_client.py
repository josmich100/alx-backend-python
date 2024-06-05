#!/usr/bin/env python3
"""
Test client module
"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google", TEST_PAYLOAD),
        ("abc", TEST_PAYLOAD)
    ])
    @patch("client.get_json")
    def test_org(self, test_org, mock_get):
        """
        test_org method
        """
        test_url = f"https://api.github.com/orgs/{test_org}"
        client = GithubOrgClient(test_org)
        client.org()
        mock_get.assert_called_once_with(test_url)

    @patch("client.GithubOrgClient.org", new_callable=TEST_PAYLOAD)
    def test_public_repos_url(self, mock_org):
        """
        test_public_repos_url method
        """
        client = GithubOrgClient("test")
        self.assertEqual(client._public_repos_url, mock_org["repos_url"])

    @patch("client.GithubOrgClient._public_repos_url",
           new_callable=TEST_PAYLOAD)
    @patch("client.get_json")
    def test_public_repos(self, mock_get, mock_url):
        """
        test_public_repos method
        """
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), mock_get.return_value)
        mock_get.assert_called_once()
        mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        test_has_license method
        """
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    TestIntegrationGithubOrgClient class
    """
    @classmethod
    def setUpClass(cls):
        """
        setUpClass method
        """
        cls.get_patcher = patch("requests.get", side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass method
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public repos """

    def test_public_repos_with_license(self):
        """test public with license"""


if __name__ == "__main__":
    """
    MAIN
    """
    unittest.main()
