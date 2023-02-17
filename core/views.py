# coding: utf-8
import json
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from commons.django_views_utils import ajax_login_required
from django.views.decorators.http import require_POST
from core.service import log_svc
from django.views.decorators.csrf import csrf_exempt
from core.models import Filme


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')

@require_POST
def cadastro(request):
    username=request.POST['username']
    email=request.POST['email']
    senha=request.POST['senha']
    novo_usuario = User.objects.create_user(username=username, email=email, password=senha)
    novo_usuario.save()
    return JsonResponse({})

def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)

def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d


@csrf_exempt
@ajax_login_required
def filmes(request):
  filmes = Filme.objects.all()
  dict_filmes = []
  for filme in filmes:
    dict_filmes.append(filme.to_dict())
  return JsonResponse({'filmes' : dict_filmes})

@csrf_exempt
def adicionar_filmes(request):
  params = json.loads(request.body)
  Filme.objects.create(titulo=params["titulo"], descricao=params["descricao"], status=params["status"], categoria=params["categoria"], imagem=params["imagem"])
  return JsonResponse({"msg": "Filme salvo com sucesso"})

@csrf_exempt
def pegar_filme(request, id):
  filme = Filme.objects.get(id=id)
  return JsonResponse({"filme": filme.to_dict()})

def editar_filme(request, id):
  edit_filme = json.loads(request.body)
  filme = Filme.objects.filter(id=id)
  filme.update(**edit_filme)
  return JsonResponse({"filme_editado": filme[0].to_dict()})
  
def excluir_filme(request, id):
  filme = Filme.objects.get(id=id)
  filme.delete()
  return JsonResponse({"msg": "Filme excluido com sucesso"})