from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similiar to a traditional Django View',
        'is mapped manually to URLS '
        ]

        return Response({'message' : 'hello!', 'an_apiview' : an_apiview})
