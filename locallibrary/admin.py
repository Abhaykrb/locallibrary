from django.contrib import admin

from .models import Language, Author, Genre, Book, BookInstance
admin.site.register(Language)
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
# Define the admin class


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name',
              ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


pass


admin.site.register(Author, AuthorAdmin)

# We canget all bookinstance byclicking booklink inhorizontaltable


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
# Toavoid extra options
    extra = 0

# Register the Admin classes for Book using the decorator


@ admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # threecolumns with title ,author and display_genre weillbe shown in admin
    # fieldnamesshould be as same as mentioned in models
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    pass

# Register the Admin classes for BookInstance using the decorator


@ admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    pass
