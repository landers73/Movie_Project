import media
import fresh_tomatoes
import json

# this module loads the server's movie data from a json file
# (entertainment_center.json) it then creats a series of movies
# of the class Movie and adds each to a list
# the list is passed to another program - fresh_tomatoes -
# which generates the web page.

movie_list = []
movie_data = json.loads(open('entertainment_center.json').read())
for lucy in movie_data['movie']:
        my_movie = media.Movie(lucy['Title'], lucy['Plot'], lucy['Poster'], lucy['Trailer'])
        movie_list.append(my_movie)

fresh_tomatoes.open_movies_page(movie_list)
     








