favorite_movies = [
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    },
    {
        "name": "Spirited Away",
        "release_year": 2001,
        "sequels": None
    }
]

def check_movie_year(movie):
    if movie["release_year"] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie["name"]

recent_movies = []

for movie in favorite_movies:
    returned_name = check_movie_year(movie)
    if returned_name is not None:
        recent_movies.append(returned_name)

print(recent_movies)