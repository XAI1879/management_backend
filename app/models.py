
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, related_name='projetos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    projeto = models.ForeignKey(Projeto, related_name='atividades', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('concluida', 'Concluída')])

    def __str__(self):
        return self.nome
