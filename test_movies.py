from movies import home
import requests


def test_films_api_status():
    movies = requests.get('https://ghibliapi465.'
                          'herokuapp.com/films')
    assert movies.status_code == 200


def test_people_api_status():
    movies = requests.get('https://ghibliapi68765.herokuapp.com/people')
    assert movies.status_code == 200


# def test_converter2():
#     assert get_roman_numerals(1776) == 'MDCCLXXVI', "Should be MDCCLXXVI"


if __name__ == "__main__":
    test_films_api_status()
    test_people_api_status()
    # test_converter2()
    # test_converter3()
    print("Everything passed")
