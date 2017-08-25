#!/usr/bin/env python
# coding=utf-8
import media
import fresh_tomatoes
# toy_story movie: movie_title, movie_duration, story_line, post_image and movie_trailr  # NOQA
toy_story = media.Movie("toy_story",
                        "1:10:40",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/zh/d/dc/Movie_poster_toy_story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


# avatar movie: movie_title, movie_duration, story_line, post_image and movie_trailr  # NOQA
avatar = media.Movie("Avatar",
                     "1:01:44",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY&t=2s")

# titanic movie: movie_title, movie_duration, story_line, post_image and movie_trailr  # NOQA
titanic = media.Movie("Titanic",
                      "1:01:23",
                      "A love story",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=ZQ6klONCq4s")

# twentytwo movie: movie_title, movie_duration, story_line, post_image and movie_trailr  # NOQA
twentytwo = media.Movie("22",
                        "1:31:49",
                        "A story need to remember",
                        "https://upload.wikimedia.org/wikipedia/zh/0/05/Twenty_Two_%282017_movie%29.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=XD3CqSMejE0")

# Set the movies that will be passed to the media file
movies = [twentytwo, avatar, titanic, toy_story]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
