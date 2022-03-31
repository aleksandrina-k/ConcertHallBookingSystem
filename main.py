from entity.concert import Concert
from entity.concert_hall import ConcertHall
from entity.registered_user import RegisteredUser
from repositories.main_repository import MainRepository

if __name__ == '__main__':
    main_repo = MainRepository()

    user1 = RegisteredUser('sasha', '123456', 'sashii00@abv.bg', 22)
    user2 = RegisteredUser('peter', '123456', 'petur11@abv.bg', 25)
    user3 = RegisteredUser('georgi', '123456', 'georgi22@abv.bg', 18)
    hall1 = ConcertHall('Arena Armeec', 'Alabala Street 1200', 800)
    hall2 = ConcertHall('Zala 1', 'NDK Street 1200', 500)
    hall3 = ConcertHall('Mladejki dom', 'Brumbrum Street 158', 200)
    concert1 = Concert('Grafa', '2022-03-30', 100, hall1)
    concert2 = Concert('Orlin Goranov', '2022-04-25', 200, hall1)

    main_repo.registered_users_repo.add(user1)
    main_repo.registered_users_repo.add(user2)
    main_repo.registered_users_repo.add(user3)
    main_repo.concert_hall_repo.add(hall1)
    main_repo.concert_hall_repo.add(hall2)
    main_repo.concert_hall_repo.add(hall3)
    main_repo.concerts_repo.add(concert1)
    main_repo.concerts_repo.add(concert2)

    main_repo.show_all()

    concert2.singer = 'BTS'
    main_repo.concerts_repo.update(concert2)
    main_repo.show_all()
