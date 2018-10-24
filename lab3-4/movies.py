class Movies(object):

    def __init__(self, movie_controller, client_controller, rental_controller):
        self.__movie_controller = movie_controller
        self.__client__controller = client_controller
        self.__rental_controller = rental_controller

    def add_movies(self):
        try:
            movieID = int(input("Introduce the ID: "))
            title = input("Introduce the movie title: ")
            description = input("Describe the movie!")
            genre = input("Which genre?")

            self.__movie_controller.add_moviet(movieID, title, description, genre)
        except StoreError as se:
            print(se)


    def print_movies(self):
        l = self.__movie_controller.print_movies()
        for e in l:
            print(e)

    def print_all_options(self):
        print("        1. Add movies\n\
        2. Print movies")

    def main(self):
        while True:
            self.print_all_options()
            options = {1:self.add_movies, 2: self.print_movies}
            try:
                op = int(input("Choose the option: "))
            except ValueError:
                print("Wrong option")
                return
            options[op]()

if __name__ == '__main__':
    try:
        movies = Movies()
        movies.main()
    except Exception as ex:
        print("Exceptie in aplicatie: ", ex)