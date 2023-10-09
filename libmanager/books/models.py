from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from slugify import CYRILLIC, Slugify


def slugify_function(text: str) -> str:
    """Slugify text, also works with cyrillic letters."""
    slugify = Slugify(pretranslate=CYRILLIC)
    return slugify(text).lower()


class TestModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    author = models.CharField(max_length=255, verbose_name='Автор')
    year = models.IntegerField(verbose_name='Год')
    genre = models.ForeignKey("Genres", on_delete=models.PROTECT, null=True, verbose_name='Жанр')
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name='Категория')
    pub_house = models.ForeignKey("PublishingHouse", on_delete=models.PROTECT, null=True, verbose_name='Издательство')
    isbn = models.CharField(max_length=10, unique=True)
    total_amount = models.IntegerField(verbose_name='Всего')
    gived_away = models.IntegerField(default=0, blank=True, null=True)
    added_to_lib_date = models.DateField(auto_now_add=True, verbose_name='Добавлена')

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ['title']

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book', kwargs={'book_id': self.id})

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    number = models.IntegerField()
    genre = models.ForeignKey("Genres", on_delete=models.PROTECT, null=True)
    pub_house = models.ForeignKey("PublishingHouse", on_delete=models.PROTECT, null=True)
    issn = models.CharField(max_length=8, unique=True)
    total_amount = models.IntegerField()
    added_to_lib_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Журналы'
        verbose_name_plural = 'Журналы'
        ordering = ['title']

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name",
                         editable=True,
                         slugify_function=slugify_function,
                         allow_duplicates=False,
                         db_index=True)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_cat", kwargs={"cat_slug": self.slug})

class Genres(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name",
                         editable=True,
                         slugify_function=slugify_function,
                         allow_duplicates=False,
                         db_index=True)

    class Meta:
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_genre", kwargs={"genre_slug": self.slug})



class PublishingHouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Издательства'
        verbose_name_plural = 'Издательства'
        ordering = ['id']

    def __str__(self):
        return self.name
