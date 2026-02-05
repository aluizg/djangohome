from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import IndexView, LoginView, ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('produtos/', ProdutoListView.as_view(), name='produtos'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_novo'),
    path('produtos/editar/<int:pk>/', ProdutoUpdateView.as_view(), name='produto_editar'),
    path('produtos/deletar/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_deletar'),
    # path('oauth/', include('social_django.urls', namespace='social')),
]