from django.urls import path
from . import views 


urlpatterns = [
    path("",views.index),
    path("<str:slug>",views.book, name="book_details")
]
