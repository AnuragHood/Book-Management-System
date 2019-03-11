from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
   
    path('book_new', views.BookCreate.as_view(), name='book_new'),
    path('book_view/<int:pk>', views.BookView.as_view(), name='book_view'),
    path('book_edit/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
    path('book_delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
]