from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.core.mail import send_mail
from .models import Contato, EmailNewsletter, MensagemContato

def index(request):
    dados = {
        'titulo': 'Página Inicial',
        'descricao': 'Consultoria estratégica de Marketing para empresas de turismo e intercâmbio',
        'endereco': 'https://simpliglobal.com.br',
        'robots': 'index,nofollow'
    }
    return render(request, 'index.html', context=dados)
    
def sobre(request):
    dados = {
        'titulo': 'Quem Somos',
        'descricao': 'Uma empresa que tem como objetivo trazer resultados tangíveis para nossos clientes do setor de Turismo e Intercâmbio por meio de estratégias e soluções de marketing digital',
        'endereco': 'https://simpliglobal.com.br/sobre',
        'robots': 'index,nofollow'
    }
    return render(request, 'sobre.html', context=dados)

def faqs(request):
    dados = {
        'titulo': 'FAQs',
        'descricao': 'Respondemos todas suas duvidas',
        'endereco': 'https://simpliglobal.com.br/faqs',
        'robots': 'noindex,nofollow'
    }
    return render(request, 'faqs.html', context=dados)

def contato(request):
    dados = {
        'titulo': 'Contato',
        'descricao': 'Entre em contato conosco e saiba o que podemos fazer pela sua empresa',
        'endereco': 'https://simpliglobal.com.br/contato',
        'robots': 'index,nofollow'
    }
    return render(request, 'contato.html', context=dados)

def analise_empresa(request):
    dados = {
        'titulo': 'Análise do cenário da empresa',
        'descricao': 'Analisamos o cenário da empresa de nossos clientes como um todo, focando no aumento de lucratividade, utilizando ferramentas de marketing digital atuais que possam auxiliar na realização dessas metas',
        'endereco': 'https://simpliglobal.com.br/analise-empresa',
        'robots': 'index,nofollow'
    }
    return render(request, 'analise_empresa.html', context=dados)

def gestao_trafego(request):
    dados = {
        'titulo': 'Gestão de Tráfego',
        'descricao': '',
        'endereco': 'https://simpliglobal.com.br/gestao-trafego',
        'robots': 'index,nofollow'
    }
    return render(request, 'gestao_trafego.html', context=dados)

def identidade_visual(request):
    dados = {
        'titulo': 'Identidade Visual & Logomarca',
        'descricao': '',
        'endereco': 'https://simpliglobal.com.br/identidade-visual',
        'robots': 'index,nofollow'
    }
    return render(request, 'identidade_visual.html', context=dados)

def criativos(request):
    dados = {
        'titulo': 'Criativos',
        'descricao': '',
        'endereco': 'https://simpliglobal.com.br/criativos',
        'robots': 'index,nofollow'
    }
    return render(request, 'criativos.html', context=dados)

def desenvolvimento_web(request):
    dados = {
        'titulo': 'Criação de Website',
        'descricao': '',
        'endereco': 'https://simpliglobal.com.br/desenvolvimento-web',
        'robots': 'index,nofollow'
    }
    return render(request, 'desenvolvimento_web.html', context=dados)


def otimizacao_seo(request):
    dados = {
        'titulo': 'Otimização de SEO',
        'descricao': '',
        'endereco': 'https://simpliglobal.com.br/otimizacao-seo',
        'robots': 'index,nofollow'
    }
    return render(request, 'otimizacao_seo.html', context=dados)


def google_meunegocio(request):
    dados = {
        'titulo': 'Google Meu Negócio',
        'descricao': '',
        'endereco': 'https://simpliglobal.com.br/google-meu-negocio',
        'robots': 'index,nofollow'
    }
    return render(request, 'google_meunegocio.html', context=dados)

def posts(request):
    dados = {
        'titulo': 'POSTS',
        'descricao': '',
        'endereco': 'https://simpliglobal.com.br/posts',
        'robots': 'index,nofollow'
    }
    return render(request, 'posts.html', context=dados)


def politica_privacidade(request):
    dados = {
        'titulo': 'Política de Privacidade',
        'descricao': 'Como tratamos seus dados',
        'endereco': 'https://simpliglobal.com.br/politica-de-privacidade',
        'robots': 'noindex,nofollow'
    }
    return render(request, 'politica_privacidade.html', context=dados)


def termos_uso(request):
    dados = {
        'titulo': 'Termos de Uso',
        'descricao': 'Termos de uso do nosso site',
        'endereco': 'https://simpliglobal.com.br/termos-de-uso',
        'robots': 'noindex,nofollow'
    }
    return render(request, 'termos_uso.html', context=dados)




def mensagem(request):
    """Recebe nova mensagem"""
    if request.method == 'POST':
        novo_contato = Contato()
        novo_contato.nome = request.POST['nome']
        novo_contato.email = request.POST['email']
        novo_contato.empresa = request.POST['empresa']
        novo_contato.save()
        #send_mail('Novo email no site!', 'Novo email de ' + novo_contato.nome + ' no site', 'fodase@fodase.com', ['guibaaa@gmail.com'], fail_silently=False)
        return HttpResponse('Aguarde nosso contato!')
    else:
        return HttpResponse('Erro ao enviar mensagem!')

def emailNewsletter(request):
    """Recebe cadastro na newsletter"""
    if request.method == 'POST':
        novo_email = EmailNewsletter()
        novo_email.email = request.POST['email']
        novo_email.save()
        return HttpResponse('Cadastrado com sucesso!')
    else:
        return HttpResponse('Erro ao cadastrar!')

def mensagemContato(request):
    """Recebe formulario da pagina contato"""
    if request.method == 'POST':
        nova_mensagem = MensagemContato()
        nova_mensagem.nome = request.POST['nome']
        nova_mensagem.email = request.POST['email']
        nova_mensagem.empresa = request.POST['empresa']
        nova_mensagem.telefone = request.POST['telefone']
        nova_mensagem.interesse = request.POST['interesse']
        nova_mensagem.forma_contato = request.POST['forma']
        nova_mensagem.mensagem = request.POST['mensagem']
        nova_mensagem.save()
        return HttpResponse('Mensagem enviada com sucesso!')
    else:
        return HttpResponse('Erro ao enviar mensagem')




def error_404(request, exception):
    dados = {
        'titulo': 'ERRO 404',
        'descricao': 'Página não encontrada',
        'endereco': 'https://simpliglobal.com.br/404',
        'robots': 'noindex,nofollow'
    }
    return render(request, '404.html', context=dados)

def error_403(request, exception):
    dados = {
        'titulo': 'ERRO 403',
        'descricao': 'Acesso negado',
        'endereco': 'https://simpliglobal.com.br/403',
        'robots': 'noindex,nofollow'
    }
    return render(request, '403.html', context=dados)

def error_500(request, exception=None):
    return HttpResponseServerError('Erro no servidor', status=500)