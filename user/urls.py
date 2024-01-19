
from django.urls import path
from .views import UserLogout,signup,ProfileView,WishlistView
from .views import  UserLoginView
from .views import activate
 
urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogout, name='logout'),
    # path('profile/',profile, name='profile'),
    path('activate/<uidb64>/<token>/',  
        activate, name='activate'),  
    path('profile/', ProfileView.as_view(), name='profile' ),
    path('wishlist/', WishlistView.as_view(), name='wishlist' ),
]