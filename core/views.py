from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Produto
from .forms import ProdutoForm

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto_list.html'
    # Nome do objeto no contexto que será usado no template html
    context_object_name = 'produtos'
    # Boa prática: Definir a ordenação diretamente na View
    # para garantir que os itens mais novos apareçam primeiro.
    ordering = ['-id']
    # Não é necessário definir queryset = Produto.objects.all()
    # pois o 'model = Produto' já faz isso automaticamente por baixo dos panos.
    # Melhoria: Otimiza a busca se houver relacionamentos (ex: Categoria)
    # Se não houver relacionamentos, pode remover a linha abaixo (o default já é .all())
    # queryset = Produto.objects.select_related('categoria').all()

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produto_delete.html'
    success_url = reverse_lazy('produtos')