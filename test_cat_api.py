import unittest
from unittest.mock import patch, Mock
from cat_api import get_random_cat_image

class TestCatAPI(unittest.TestCase):
    @patch('cat_api.requests.get')
    def test_successful_request(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"url": "https://cdn2.thecatapi.com/images/abc.jpg"}]
        mock_get.return_value = mock_response
        result = get_random_cat_image()
        self.assertEqual(result, "https://cdn2.thecatapi.com/images/abc.jpg")

    @patch('cat_api.requests.get')
    def test_unsuccessful_request(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        result = get_random_cat_image()
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
