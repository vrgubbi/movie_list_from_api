# movie_list_from_api

Requirement:
Python application which serves a page on localhost:8000/movies/. This page contains a plain list of all movies from the Ghibli API. For each movie the people that appear in it will be listed.


Technologies used:
Language: Python3
Web framework: Flask
Python libraries: mentioned in the requirements.txt
Test framework: unittest
API: https://ghibliapi.herokuapp.com/


Introduction:
Written a flask web application which does the following tasks.
- To access movies api, provided by 'Studio Ghibli'.
- Fetch all movies list and characters of each movie using this api.
- Compute the data of two different api endpoints(/films, /people) to establish relationship.
- Display the final data in the frontend webpage.
- It is designed to access at the following url, localhost:8000/movies/


Setup:
- Intall Python version 3, virtual environment(optional but recommended)
- Clone the repository from github.
  	git clone https://github.com/vrgubbi/movie_list_from_api.git
- go to folder 'movie_list_from_api'
	cd movie_list_from_api/
- Install python third party libraries provided in requirements.txt
  	pip install -r requirements.py
- Run the python file 'movies.py'
	python movies.py
- Access the webpage using url, localhost:8000/movies/
- That's it, you can now see the list of movies and it's respective characters acted in that film. 


PEP8 standard:
Code has been developed with pep8 standards.


Tests:
Python's inbuilt UnitTest framework has been used to write testcases.
Test cases has been written in the file test_movies.py
It will test and cover all the necessary points for the main file movies.py
Test cases will be executed using below syntax:
	
	$ python -m unittest test_movies

Following example shows if every test cases are passed:
	$ python -m unittest test_movies
	..
	----------------------------------------------------------------------
	Ran 2 tests in 1.074s

	OK

Following example shows if any of the test cases are failed with debug information:
	$ python -m unittest test_movies
	.F
	======================================================================
	FAIL: test_people_api_status (test_movies.Test)
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "/Users/ichbin/git_projects/movie_list_from_api/test_movies.py", line 19, in test_people_api_status
	    self.assertEqual(movies.status_code, 200)
	AssertionError: 404 != 200

	----------------------------------------------------------------------
	Ran 2 tests in 1.171s

	FAILED (failures=1)


Improvements:
- If there are more requirements comes in the future, we can swich to django from flask, because django can handle bigger applications.
- There is a scope for adding more test cases, which covers varieties of scenarios, also the unittest module can be used from the command line to run tests from modules, classes or even individual test methods.


Finally:
This web appication has been designed to take less time to load.

Instead of making people api endpoint request for each and every movie, only one people api request has been made that has characters list of all the movies, also total counts of both the films and people endpoints api has less than 100. Also it'll avoid making multiple requests for the third party api.

How to setup this project has been explained in the above section, it'll then be accessed using url, localhost:8000/movies/

For look and feel of the webpage, screenshot has been attached in the name 'webpage_screenshot.png'.
