from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path("cart/add/<int:book_id>/", views.add_to_cart, name="add_to_cart"),
    path("mybooks/", views.mybooks, name="mybooks"),
    path("cart/", views.cart_page, name="cart_page"),
    path("cart/remove/<int:book_id>/", views.remove_from_cart, name="remove_from_cart"),
    path('about_us/', views.about_us, name='about_us'),

]

