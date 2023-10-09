from random import randint

def generate_isbn():
    isbn = ''
    for i in range(13):
        isbn += str(randint(0, 9))
    return print(isbn)

def generate_issn():
    issn = ''
    for i in range(10):
        issn += str(randint(0, 9))
    return print(issn)