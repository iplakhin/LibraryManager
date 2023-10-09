from datetime import date
from books.models import *
from users.models import *

def giveaway_a_book(user_id, book: Book) -> BooksUser:
    user = User.objects.filter(id=user_id).first()
    try:
        gived_book = BooksUser(
            book_id=book,
            user_id=user,
            expiration_date=date(2023, 10, 14),
            is_expired=False
        )
        gived_book.save()
        return gived_book
    except:
        raise ValueError("Ошибка записи в БД")


