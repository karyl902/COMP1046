


server = Catalogue()
sever.add.movie(
    Movie("The Matrix", ['Action', 'Sci-Fi'], 136, "M")
)
server.add.movie(
    Movie("The Expendables", 'Action', 103, "MA15+")
)
server.add.movie(
    Movie("Antz", ['Comedy', 'Adanventure'], 83, "PG")
)
server.add.movie(
    Movie("Star Wars", ['Action', 'Adventure','Sci-Fi'], 121, "PG")
)
antz = server.search_by_name("Antz")
antz.display_details()

sci_fi = server.search_by_genre("Sci-Fi")
for sci_fi_movie in sci_fi:
    sci_fi_movie.display_details()
    pass