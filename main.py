from entity.concert import Concert
from entity.concert_hall import ConcertHall
from entity.date import Date
from entity.role import Role
from entity.user import User
from repositories.main_repository import MainRepository

if __name__ == '__main__':
    main_repo = MainRepository()

    user1 = User('Aleksandrina', 21, 'sasha', '123456', 'sashii00@abv.bg')
    user2 = User('Peter', 25, 'peter', '123456', 'petur11@abv.bg')
    user3 = User('Georgi', 18, 'georgi', '123456', 'georgi22@abv.bg')
    hall1 = ConcertHall('Arena Armeec', 'Alabala Street 1200', 800)
    hall2 = ConcertHall('Zala 1', 'NDK Street 1200', 500)
    hall3 = ConcertHall('Mladejki dom', 'Brumbrum Street 158', 200)
    concert1 = Concert('Grafa', Date(30, 3, 2022), 100, hall1)
    concert2 = Concert('Orlin Goranov', Date(25, 4, 2022), 200, hall1)

    main_repo.users_repo.add(user1)
    main_repo.users_repo.add(user2)
    main_repo.users_repo.add(user3)
    main_repo.concert_hall_repo.add(hall1)
    main_repo.concert_hall_repo.add(hall2)
    main_repo.concert_hall_repo.add(hall3)
    main_repo.concerts_repo.add(concert1)
    main_repo.concerts_repo.add(concert2)

    main_repo.show_all()

    concert2.singer = 'Mihaela Fileva'
    main_repo.concerts_repo.update(concert2)
    main_repo.show_all()

    main_repo.concert_hall_repo.save()
    main_repo.concerts_repo.save()
    main_repo.users_repo.save()

    main_repo.concert_hall_repo.load()
    main_repo.concerts_repo.load()
    main_repo.users_repo.load()
    print('\n', 'After Loading:')
    main_repo.show_all()

