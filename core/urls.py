from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import IndexView, LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    # path('oauth/', include('social_django.urls', namespace='social')),
]