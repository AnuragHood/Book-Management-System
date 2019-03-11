from django.urls import path

from . import views

urlpatterns = [
    path('', views.PenList.as_view(), name='pen_list'),
   
    path('book_new', views.PenCreate.as_view(), name='book_new'),
    path('book_view/<int:pk>', views.PenView.as_view(), name='book_view'),
    path('book_edit/<int:pk>', views.PenUpdate.as_view(), name='book_edit'),
    path('book_delete/<int:pk>', views.PenDelete.as_view(), name='book_delete'),
]