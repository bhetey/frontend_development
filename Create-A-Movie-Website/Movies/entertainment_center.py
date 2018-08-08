import media
import fresh_tomatoes
import os

# My movie choices, they will be called into the class
great_wall = media.Movie("The Great Wall", 
                        "European mercenaries searching for black powder become embroiled in the defense \
                        of the Great Wall of China against a horde of monstrous creatures.", 
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQkQpwFX-dW5-f3aFplLtOrQwSozX1259tGD1mGxsksk3LPygM1",
                        "https://www.youtube.com/watch?v=avF6GHyyk5c", 
                        "Movie was launched in 2016", 
                        "Director : Yimou Zhang")

fate_of_the_furious = media.Movie("Fate of the Furious", 
                                "When a mysterious woman seduces Dom into the world of terrorism and a betrayal \
                                 of those closest to him, the crew face trials that will test them as never before." ,
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxODI2NDM5Nl5BMl5BanBnXkFtZTgwNjgzOTk1MTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg", 
                                "https://www.youtube.com/watch?v=JwMKRevYa_M", 
                                "Movie was launched in 2017", 
                                "Director :  F. Gary Gray")

home_alone = media.Movie("Home Alone", 
                            "An eight-year-old troublemaker must protect his house from a pair of burglars when he \
                             is accidentally left home alone by his family during Christmas vacation.", 
                            "http://nationalinfantrymuseum.org/wp-content/uploads/2016/11/Home-Alone-25-hi-res.jpg", 
                            "https://www.youtube.com/watch?v=7ptuE1ENhzU", 
                            "Movie was launched in 1990", 
                            "Director :  Chris Columbus")

the_expendables = media.Movie("The Expendables 2", 
                                "Mr. Church reunites the Expendables for what should be an easy paycheck, but when one \
                                 of their men is murdered on the job, their quest for revenge puts them deep in enemy territory and up against an unexpected threat.", 
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcQ9qF-tGkwN1qzXOX0SHFHGO3WUmIhxN8nqmzjpmpuntltW9Pn6",
                                "https://www.youtube.com/watch?v=ip_CYHdyUBs", 
                                "Movie was launched in 2012", 
                                "Director : Simon West")

tomorrow_when_the_war_begin = media.Movie("Tomorrow when the war begins",
                                    "When their country is invaded and their families are taken, eight unlikely high school \
                                     teenagers band together to fight.",
                                    "http://www.gstatic.com/tv/thumb/movieposters/8605167/p8605167_p_v8_aa.jpg",
                                    "https://www.youtube.com/watch?v=efHGC2YoTiI", 
                                    "Movie was launched in 2010",
                                    "Director : Stuart Beattie")

day_of_the_future_past = media.Movie("X- Men, Day Of The Future Past", 
                                    "The X-Men send Wolverine to the past in a desperate effort to change history and prevent \
                                     an event that results in doom for both humans and mutants.", 
                                    "http://t3.gstatic.com/images?q=tbn:ANd9GcSp1xUUrh6IW4gwa8j7p8WxU7Yt21mWhLVwZ5CejaXF6KsrOtjs", 
                                    "https://www.youtube.com/watch?v=pK2zYHWDZKo", 
                                    "Movie was launched in 2014", 
                                    "Director : Bryan Singer")

wonder_woman = media.Movie("Wonder Woman", 
                            "When a pilot crashes and tells of conflict in the outside world, Diana, an Amazonian warrior in training, \
                             leaves home to fight a war, discovering her full powers and true destiny.", 
                            "https://images-na.ssl-images-amazon.com/images/I/91I2JspDFLL._RI_.jpg", 
                            "https://www.youtube.com/watch?v=VSB4wGIdDwo", 
                            "Movie was launched in 2017", 
                            "Director : Patty Jenkins")

rush_hour = media.Movie("Rush Hour", 
                        "A loyal and dedicated Hong Kong inspector teams up with a reckless and loudmouthed LAPD detective to rescue \
                         the Chinese Consul's kidnapped daughter, while trying to arrest a dangerous crime lord along the way.", 
                        "http://www.gstatic.com/tv/thumb/movieposters/21702/p21702_p_v8_ae.jpg", 
                        "https://www.youtube.com/watch?v=JMiFsFQcFLE", 
                        "Movie was launched in 1998", 
                        "Director : Brett Ratner")

coming_to_america = media.Movie("Coming to America", 
                                "An extremely pampered African Prince travels to Queens, New York, and goes undercover to find a wife \
                                whom he can respect for her intelligence and will", 
                                "http://t2.gstatic.com/images?q=tbn:ANd9GcRVQibXx0OsF_6xoE3FUPoMrmcjw19NZJqivD9Xaeq4juHaZ_n2", 
                                "https://www.youtube.com/watch?v=fqfJqLFQSIk", 
                                "Movie was launched in 1988", 
                                "Director : John Landis")

# List of the movies 
movies = [great_wall, fate_of_the_furious, home_alone, the_expendables, tomorrow_when_the_war_begin, day_of_the_future_past, 
        wonder_woman, rush_hour, coming_to_america]

fresh_tomatoes.open_movies_page(movies)




