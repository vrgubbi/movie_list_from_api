# movie_list_from_api

Requirement:
Python application which serves a page on localhost:8000/movies/. This page contains a plain list of all movies from the Ghibli API. For each movie the people that appear in it will be listed.

Technologies used:
Language: Python3
Web framework: Flask
Python libraries: mentioned in the requirements.txt
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
Test cases has been written in the file test_movies.py
It will test the main code flow and cover all the necessary points for the main file movies.py
Test cases will be executed using below syntax:
	python test_movies.py

Following example shows if every test cases are passed:
	$ python test_movies.py 
		Everything passed

Following example shows if any of the test cases are failed with debug information:
	$ python test_movies.py 
		Traceback (most recent call last):
		  File "test_movies.py", line 20, in <module>
		    test_films_api_status()
		  File "test_movies.py", line 6, in test_films_api_status
		    assert movies.status_code == 200
		AssertionError



Finally:
This web appication has been designed to take less time to load,  max within 1 second
