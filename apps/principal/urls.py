from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('faqs', views.faqs, name='faqs'),
    path('contato', views.contato, name='contato'),
    path('analise-empresa', views.analise_empresa, name='analise_empresa'),
    path('gestao-trafego', views.gestao_trafego, name='gestao_trafego'),
    path('identidade-visual', views.identidade_visual, name='identidade_visual'),
    path('criativos', views.criativos, name='criativos'),
    path('desenvolvimento-web', views.desenvolvimento_web, name='desenvolvimento_web'),
    path('otimizacao-seo', views.otimizacao_seo, name='otimizacao_seo'),
    path('google-meu-negocio', views.google_meunegocio, name='google_meunegocio'),
    path('posts', views.posts, name='posts'),
    path('politica-de-privacidade', views.politica_privacidade, name='politica_privacidade'),
    path('termos-de-uso', views.termos_uso, name='termos_uso'),
    path('mensagem/', views.mensagem, name='mensagem'),
    path('email_newsletter/', views.emailNewsletter, name='email_newsletter'),
    path('mensagem_contato/', views.mensagemContato, name='mensagem_contato'),
]