from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profile_api import serializers


class HelloApiView(APIView):
    '''Test API View'''

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Returns a list of APIView features'''
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Give you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        '''created a hello message with our name'''
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''Handle unpdating an object'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''Handle a partial update of an object'''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        '''Delete an Object'''
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''

    def list(self, request):
        '''Return a hello message'''
        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
