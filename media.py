#!/usr/bin/env python
# coding=utf-8
import webbrowser


class Video(object):
    """A model of a Video"""

    def __init__(self, title, duration):
        """Initialize title, duration"""
        print("hahahah")
        self.title = title
        self.duration = duration


class Movie(Video):
    """A model of a Movie inherit from Video"""

    def __init__(self, movie_title, movie_duration, movie_storyline, poster_image, trailer_youtube):  # NOQA
        """Initialize title, durationm, storyline, poster_image_url,traler_youtube"""  # NOQA
        self.title = movie_title
        Video(movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """test function to open url on webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
