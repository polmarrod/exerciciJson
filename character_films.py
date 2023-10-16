from character import Character
class Character_films(Character):
    def __init__(
        self,
        edited,
        name,
        created,
        gender,
        skin_color,
        hair_color,
        height,
        eye_color,
        mass,
        homeworld,
        birth_year,
        num_of_films,
        first_film,
        alive_at_the_end
        ):
        super().__init__(self,
        edited,
        name,
        created,
        gender,
        skin_color,
        hair_color,
        height,
        eye_color,
        mass,
        homeworld,
        birth_year)
        self.__num_of_films = num_of_films
        self.__first_film = first_film
        self.__alive_at_the_end = alive_at_the_end
    
    @num_of_films.setter
    def num_of_films(self, set_num_of_films):
        self.__num_of_films = set_num_of_films
    
    @first_film.setter
    def first_film(self, set_first_film):
        self.__first_film = set_first_film
    
    @alive_at_the_end.setter
    def alive_at_the_end(self, set_alive_at_the_end):
        self.__alive_at_the_end = set_alive_at_the_end