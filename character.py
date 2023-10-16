class Character:
    def __init__(
        self,
        edited,
        name : str,
        created,
        gender,
        skin_color,
        hair_color,
        height,
        eye_color,
        mass,
        homeworld,
        birth_year):

        self.__edited = edited
        self.__name = name
        self.__created = created
        self.__gender = gender
        self.__skin_color = skin_color
        self.__hair_color = hair_color
        self.__heigth = height
        self.__eye_color = eye_color
        self.__mass = mass
        self.__homeworld = homeworld
        self.__birth_year = birth_year

    @property
    def info(self):
        print(self.__name, self.__gender, self.__homeworld, self.__birth_year)