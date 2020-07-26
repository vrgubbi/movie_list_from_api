import unittest
from movies import home
import requests


class Test(unittest.TestCase):
    """
    The class that inherits unittest.TestCase
    """

    def test_films_api_status(self):
        # Checks films api endpoint status
        movies = requests.get('https://ghibliapi.'
                              'herokuapp.com/films')
        self.assertEqual(movies.status_code, 200)

    def test_people_api_status(self):
        # Checks people api endpoint status
        movies = requests.get('https://ghibliapi.herokuapp.com/people')
        self.assertEqual(movies.status_code, 200)


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
