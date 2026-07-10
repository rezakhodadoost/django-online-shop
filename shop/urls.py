from django.urls import path
from . import views
'''This is the urls.py file for the shop app. It defines the URL patterns
 for the app and maps them to the corresponding views.'''

urlpatterns = [
    path("" , views.HomePageListView.as_view() , name='home' ),
    path("signup/" , views.SignupPageView.as_view() , name='signup' ),
    path("login/" , views.LoginPageView.as_view() , name='login'),
    path("logout/", views.LogoutPageView.as_view(), name='logout'),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart/add/<int:pk>/", views.AddToCartView.as_view(), name="add_to_cart"),
    path("cart/remove/<int:pk>/", views.RemoveFromCartView.as_view(), name="remove_from_cart"),
    path("like/<int:pk>/",views.LikeProductView.as_view(),name="like_product"),
    path("likes/",views.MyLikesView.as_view(),name="likes"),
    path("product/<int:pk>/comment/", views.AddCommentView.as_view(), name="add_comment"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),

]

