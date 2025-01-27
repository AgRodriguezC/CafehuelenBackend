from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Local, Totem, Superv_local, Proveedor
from .serializers import LocalSerializer, TotemSerializer, Superv_localSerializer, ProveedorSerializer
# bloque productos = Local, Totem, Supervisores_local, Proveedor
# Create your views here.

#GET, POST PUT DELETE LOCAL-------------------------------------------------------------------------
@api_view(['GET','POST','DELETE'])
def local_list(request):
    if request.method == 'GET':
        locales = Local.objects.all()
        local_serializer = LocalSerializer(locales,many=True)
        return Response(local_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        local_data = JSONParser().parse(request)
        local_serializer = LocalSerializer(data=local_data)
        if local_serializer.is_valid():
            local_serializer.save()
            return Response(local_serializer.data,status=status.HTTP_201_CREATED)
        return Response(local_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Local.objects.all().delete()
        return Response({'message:','{} Locales han sido eliminados de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def local_detail(request,id_local):
    try:
        local = Local.objects.get(id_local=id_local)
    except Local.DoesNotExist:
        return Response({'messaje':'El local buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        local_serializer = LocalSerializer(local)
        return Response(local_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        local_data = JSONParser().parse(request)
        local_serializer = LocalSerializer(data=local_data)
        if local_serializer.is_valid():
            local_serializer.save()
            return Response(local_serializer.data,status=status.HTTP_200_OK)
        return Response(local_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        local.delete()
        return Response({'message':'Local eliminado correctamente'}, status=status.HTTP_200_OK)

#GET, POST PUT DELETE TOTEM-------------------------------------------------------------------------
@api_view(['GET','POST','DELETE'])
def totem_list(request):
    if request.method == 'GET':
        totems = Totem.objects.all()
        totem_serializer = TotemSerializer(totems,many=True)
        return Response(totem_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        totem_data = JSONParser().parse(request)
        totem_serializer = TotemSerializer(data=totem_data)
        if totem_serializer.is_valid():
            totem_serializer.save()
            return Response(totem_serializer.data,status=status.HTTP_201_CREATED)
        return Response(totem_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Totem.objects.all().delete()
        return Response({'message:','{} Totems han sido eliminados de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def totem_detail(request,num_totem):
    try:
        totem = Totem.objects.get(num_totem=num_totem)
    except Totem.DoesNotExist:
        return Response({'messaje':'El totem buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        totem_serializer = TotemSerializer(totem)
        return Response(totem_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        totem_data = JSONParser().parse(request)
        totem_serializer = TotemSerializer(data=totem_data)
        if totem_serializer.is_valid():
            totem_serializer.save()
            return Response(totem_serializer.data,status=status.HTTP_200_OK)
        return Response(totem_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        totem.delete()
        return Response({'message':'Totem eliminado correctamente'}, status=status.HTTP_200_OK)
    
#GET, POST PUT DELETE SUPERV_LOCAL-------------------------------------------------------------------------
@api_view(['GET','POST','DELETE'])
def superv_local_list(request):
    if request.method == 'GET':
        supervs_local = Superv_local.objects.all()
        superv_local_serializer = Superv_localSerializer(supervs_local,many=True)
        return Response(superv_local_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        superv_local_data = JSONParser().parse(request)
        superv_local_serializer = Superv_localSerializer(data=superv_local_data)
        if superv_local_serializer.is_valid():
            superv_local_serializer.save()
            return Response(superv_local_serializer.data,status=status.HTTP_201_CREATED)
        return Response(superv_local_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Superv_local.objects.all().delete()
        return Response({'message:','{} Supervisores han sido eliminados de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def superv_local_detail(request,usuario):
    try:
        superv_local = Superv_local.objects.get(usuario=usuario)
    except Totem.DoesNotExist:
        return Response({'messaje':'El supervisor buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        superv_local_serializer = Superv_localSerializer(superv_local)
        return Response(superv_local_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        superv_local_data = JSONParser().parse(request)
        superv_local_serializer = Superv_localSerializer(data=superv_local_data)
        if superv_local_serializer.is_valid():
            superv_local_serializer.save()
            return Response(superv_local_serializer.data,status=status.HTTP_200_OK)
        return Response(superv_local_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        superv_local.delete()
        return Response({'message':'Supervisor eliminado correctamente'}, status=status.HTTP_200_OK)
    
#GET, POST PUT DELETE PROVEEDOR-------------------------------------------------------------------------
@api_view(['GET','POST','DELETE'])
def proveedor_list(request):
    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
        proveedor_serializer = ProveedorSerializer(proveedores,many=True)
        return Response(proveedor_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        proveedor_data = JSONParser().parse(request)
        proveedor_serializer = ProveedorSerializer(data=proveedor_data)
        if proveedor_serializer.is_valid():
            proveedor_serializer.save()
            return Response(proveedor_serializer.data,status=status.HTTP_201_CREATED)
        return Response(proveedor_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Proveedor.objects.all().delete()
        return Response({'message:','{} Proveedores han sido eliminados de la base de datos'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def proveedor_detail(request,id_proveedor):
    try:
        proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    except Proveedor.DoesNotExist:
        return Response({'messaje':'El proveedor buscado no existe en nuestros registros'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        proveedor_serializer = ProveedorSerializer(proveedor)
        return Response(proveedor_serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        proveedor_data = JSONParser().parse(request)
        proveedor_serializer = ProveedorSerializer(data=proveedor_data)
        if proveedor_serializer.is_valid():
            proveedor_serializer.save()
            return Response(proveedor_serializer.data,status=status.HTTP_200_OK)
        return Response(proveedor_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        proveedor.delete()
        return Response({'message':'Proveedor eliminado correctamente'}, status=status.HTTP_200_OK)