from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('createlist', views.createlist, name="createlist"),
    path('list/<str:id>', views.listpage, name="listpage"),
    path('<int:listid>/comment', views.comment, name="comment"),
    path('addwl/<int:listid>', views.addwatchlist, name="addwatchlist"),
    path('watchlist', views.watchlist, name="watchlist"),
    path('category', views.category, name="category")
]
