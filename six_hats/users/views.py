from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from users.models import User
from users.serializers import AddUserSerializer, UpdateUserSerializer, DeleteUserSerializer, UserSerializer


@api_view(['POST'])
def add_user(request):
    data = request.data
    serializer = AddUserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        name = data.get('name')
        email = data.get('email')
        address = data.get('address')
        obj, created = User.objects.get_or_create(name=name,
                                                  email=email,
                                                  username=email,
                                                  address=address)

        resp_data = {'user_id': obj.id, 'name': obj.name, 'email': obj.email}
        response_data = {"status": status.HTTP_200_OK, "message": 'User added successfully', "data": resp_data}
        return Response(response_data)
    else:
        response_data = {"status": status.HTTP_200_OK, "message": 'User not added'}
        return Response(response_data)


@api_view(['POST'])
def edit_user(request):
    data = request.data
    serializer = UpdateUserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        user_id = data.get('user_id')
        name = data.get('name')
        email = data.get('email')
        address = data.get('address')
        obj = User.objects.get(id=user_id)
        obj.name = name
        obj.email = email
        obj.address = address
        obj.save()
        new_obj = obj
        resp_data = {'user_id': new_obj.id, 'name': new_obj.name, 'email': new_obj.email}
        response_data = {"status": status.HTTP_200_OK, "message": 'User updated successfully', "data": resp_data}
        return Response(response_data)
    else:
        response_data = {"status": status.HTTP_200_OK, "message": 'User not updated'}
        return Response(response_data)


@api_view(['DELETE'])
def delete_user(request):
    data = request.data
    serializer = DeleteUserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        user_id = data.get('user_id')
        User.objects.get(id=user_id).delete()
        response_data = {"status": status.HTTP_200_OK, "message": 'User deleted successfully'}
        return Response(response_data)
    else:
        response_data = {"status": status.HTTP_200_OK, "message": 'User not deleted'}
        return Response(response_data)


@api_view()
def list_user(request):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    user_obj = User.objects.all()
    res_page = paginator.paginate_queryset(user_obj, request)
    serializer = UserSerializer(res_page, many=True)
    return paginator.get_paginated_response(serializer.data)