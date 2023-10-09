from django.db import models
from django.urls import reverse


class Manager(models.Model):
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    birthdate = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(max_length=1, verbose_name="Пол", default='F')
    photo = models.ImageField(upload_to="profiles/", blank=True, verbose_name="Фото")
    reg_date = models.DateTimeField(auto_now_add=True)
    contacts = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = 'Читатели'
        verbose_name_plural = 'Читатели'
        ordering = ['reg_date']

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return reverse('getprofile', kwargs={'user_id': self.id})


class BooksUser(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey("books.Book", on_delete=models.RESTRICT)
    user_id = models.ForeignKey("User", on_delete=models.RESTRICT)
    start_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return f"User {self.user_id} has book {self.book_id}"
