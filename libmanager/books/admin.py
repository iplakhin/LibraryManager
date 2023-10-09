from django.contrib import admin
from books.models import *
from users.models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'genre', 'added_to_lib_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author', 'genre')

admin.site.register(Book, BookAdmin)
admin.site.register(Magazine)
admin.site.register(Category)
admin.site.register(Genres)
admin.site.register(PublishingHouse)

admin.site.register(User)
admin.site.register(BooksUser)


