from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>/", views.article_page, name="article_page"),
    path("search", views.search_form, name="search"),
    path("newpage", views.add_new_page, name="newpage"),
    path("wiki/<str:name>/editpage/", views.edit_page, name="editpage"),
    path("random", views.random_page, name="random_page"),
]
