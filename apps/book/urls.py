from django.urls import path
from . import views


# URLs dosen't understand classes. but it understands functional based views only 
# when using a class based view, we have to transform it to function using as_view()


app_name = 'book-urls'
urlpatterns = [
    path("author/", views.list_authors, name="list-author"),
    path("tag/", views.list_tags, name="list-tag"),
    path("list/", views.list_books, name="list-book"),
    path("create/", views.create_books, name="list-book"),
    path('list/list/', views.BooksView.as_view(), name="class-list-book"),   #  to verify we check name= however the path is dynamic we can change at any time
    path('author/<int:pk>', views.DetailAuthor.as_view(), name='detail-author'),
]