import webbrowser
import os

class Movie():
    """ 
    This class was created to store movie related details
    like the trailer of the movie, the director etc. 
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, launch_date, movie_director):
        """
        this function has stored variables that is being intitiated by the init function. 
        then a space is created in the memory of the computer for this variables 
        each variable is named according to what they meant. 

        for example, movie_title takes the movie title and then returns the title of the movie,
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.launch_year = launch_date
        self.film_director = movie_director     
        
    def showing_trailer(self):
        """
        this function used imported module called webbroswer to  
        open your web browser and then play the trailer 
        """
        webbrowser.open(self.trailer_youtube_url)
        