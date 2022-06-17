# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title: str, director: str, budget: int):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        if self.budget > 100000000:
            return True
        else:
            return False


movie1 = Movie('Matrix', ' Lana Wachowski, Lilly Wachowski', 63000000)
movie2 = Movie('Inception', 'Christopher Nolan', 160000000)
print('Title:', movie1.title, 'Director:', movie1.director, 'Budget:', movie1.budget)
print('Was expensive? ', movie1.was_expensive())
print('Title:', movie2.title, 'Director:', movie2.director, 'Budget:', movie2.budget)
print('Was expensive? ', movie2.was_expensive())
