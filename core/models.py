from django.db import models
from django.contrib.auth.models import User

CATEGORIAS = [
        ('terror', 'Terror'),
        ('comedia', 'Comédia'),
        ('acao', 'Ação'),
        ('drama', 'Drama'),
        ('outros', 'Outros')
    ]

STATUS = [
        ('visto', 'Visto'),
        ('nao visto', 'Não Visto'),
        ('sem interesse', 'Sem Interesse')
    ]

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.CASCADE)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )

class Filme(models.Model):
  titulo = models.TextField()
  descricao = models.TextField()
  status = models.TextField(choices=STATUS, null=True)
  categoria = models.TextField(choices=CATEGORIAS, null=True)
  imagem = models.URLField(default='https://example.com/filmes/default.jpg')

  def to_dict(self):
    return {
      "id": self.id,
      "titulo": self.titulo, 
      "descricao": self.descricao,
      "status": self.status,
      "categoria": self.categoria,
      "imagem": self.imagem

    }