from rest_framework import serializers
from .models import Local, Totem, Superv_local, Proveedor

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ('id_local', 'nombre_local', 'fono_local', 'direccion_local')
        
class TotemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Totem
        fields = ('mac_totem', 'num_totem', 'local_asignado')

class Superv_localSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superv_local
        fields = ('usuario', 'contrasena', 'local_asignado')

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id_proveedor', 'nombre_prove', 'num_prove', 'ingredientes_prove')
