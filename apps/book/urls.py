from django.urls import path
from . import views

app_name = 'book-urls'
urlpatterns = [
    path("author/", views.list_authors, name="list-author"),
    path("tag/", views.list_tags, name="list-tag"),
    path("list/", views.list_books, name="list-book"),
    path("create/", views.create_books, name="list-book"),
]


{
    "isbn": "1-189-59413-7",
    "title": "Individual book teach defense defense hand their m",
    "description": "Form team nor wall. Support great without a. Majority mouth bank grow build poor state.Meeting organization until leader you. Miss painting fight these.\nDecision buy put behind color bed. Control pass mention late I daughter. Right especially stage church during environment note.Different drug contain place record president. Lot end she they five.\nDrop month there kind I agency change. Produce fight lose west member body.",
    "page_count": 400,
    "category": "pr",
    "published_date": 1982,
    "publisher": "Russell-Miranda",
    "edition": 2,
    "book_format": "hc",
    "tags": [1, 2, 3],
    "lang": "English",
    "authors": [{"id": 1, "role": "author"}, {"id": 33, "role": "co_author"}],
}
