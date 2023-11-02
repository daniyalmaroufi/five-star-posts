from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Score
from .serializers import ScoreSerializer



class ScoreView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        serializer=ScoreSerializer(data=request.data)
        if(serializer.is_valid()):
            print(serializer.data)
            the_post=Post.objects.get(id=serializer.data['post'])
            score=serializer.data['score']

            the_score=Score.objects.filter(user=request.user,post=the_post)
            if the_score.exists():
                the_score=the_score.first()
                the_score.score=score
                the_score.save()
            else:
                the_score=Score(user=request.user,post=Post.objects.get(id=the_post),score=score)
                the_score.save()

            the_post.score=(the_post.score*the_post.scores_count+score)/(the_post.scores_count+1)
            the_post.scores_count+=1
            the_post.save()
            
            return Response({'ok':True,'detail':'set'},status=status.HTTP_200_OK)
        else:
            return Response({'ok':False},status=status.HTTP_403_FORBIDDEN)
        
    def get(self,request):
        return Response({'ok':True},status=status.HTTP_200_OK)
