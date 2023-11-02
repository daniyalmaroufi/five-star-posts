from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Score
from .serializers import ScoreSerializer



class ScoreView(APIView):

    def post(self,request):
        serializer=ScoreSerializer(data=request.data)
        if(serializer.is_valid()):
            print(serializer.data)
            return Response({'ok':True,'detail':'set'},status=status.HTTP_200_OK)
        else:
            return Response({'ok':False},status=status.HTTP_403_FORBIDDEN)
        
    def get(self,request):
        return Response({'ok':True,'detail':'set'},status=status.HTTP_200_OK)
