from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
    ):
    costumer_object = [Customer(c["name"], c["food"]) for c in customers]
    for c in costumer_object:
        CinemaBar.sell_product(product= c.food, costumer= c)
    hall = CinemaHall(number = hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie_name = movie, customers = costumer_object, cleaning_staff = cleaning_staff)
