
from rest_framework import serializers
from .models import Cliente, Projeto, Atividade

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.ReadOnlyField(source='cliente.nome')

    class Meta:
        model = Projeto
        fields = '__all__'

class AtividadeSerializer(serializers.ModelSerializer):
    projeto_nome = serializers.ReadOnlyField(source='projeto.nome')

    class Meta:
        model = Atividade
        fields = '__all__'
