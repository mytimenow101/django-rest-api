from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from . import permissions

# # Create your views here.
#
# class HelloApiView(APIView):
#     """Test API View"""
#
#     def get(self, request, format=None):
#         """Returns a list of APIView features"""
#
#         an_apiview = [
#         'Uses HTTP methods as function (get, post, patch, put, delete)',
#         'Is similiar to a traditional Django View',
#         'is mapped manually to URLS '
#         ]
#
#         return Response({'message' : 'hello!', 'an_apiview' : an_apiview})
#
#     def post(self, request):
#         """Create a message name"""
#         serializer = HelloSerializer(data=request.data)
#
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello {name}'
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#     def put(self, request, pk=None):
#         """Handle updating an object"""
#         return Response({'method': 'PUT'})
#
#     def patch(self, request, pkk=None):
#         """Updates the object"""
#         return Response({'method':'PATCH'})
#
#     def delete(self, request, pk=None):
#         """Delete the object"""
#         return Response({'method':'Delete'})




class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
        ]
        return Response({'message':'Hello','a_viewset': a_viewset})

    def create(self, request):
        """Creates item add to dbase"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        """Updates this item """

        return Response({})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    athentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
