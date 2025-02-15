from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

class AuthView(APIView):
    authentication_classes = [TokenAuthentication]
    pass