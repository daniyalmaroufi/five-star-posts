from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Score
from .serializers import ScoreSerializer


class ScoreView(APIView):
    """
    A logged in user rates a post by calling this method.
    If the user has never rated the post before, a new rating
    would be submitted and otherwise their previous rating would get updated.

    Sample Response:

    ```json
    {
        "ok": true,
        "detail": "set"
    }
    ```
    """
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
                the_score=Score(user=request.user,post=the_post,score=score)
                the_score.save()
                the_post.scores_count+=1

            the_post.score=(the_post.score*(the_post.scores_count-1)+score)/(the_post.scores_count)
            the_post.save()
            
            return Response({'ok':True,'detail':'set'},status=status.HTTP_200_OK)
        else:
            return Response({'ok':False},status=status.HTTP_403_FORBIDDEN)


class PostsView(APIView):
    """
    Shows the list of posts ordered by id descending with the title of each post,
    the number of users rated that post and its rating. If the logged in user has
    rated a post before, their rating would be shown.
    
    Sample Response:
    
    ```json
    {
        "ok": true,
        "posts": [
            {
                "title": "Post Three",
                "scores_count": 0,
                "score": 0.0
            },
            {
                "title": "Second Post",
                "scores_count": 1,
                "score": 4.0
            },
            {
                "title": "Post 1",
                "scores_count": 2,
                "score": 4
            }
        ]
    }
    ```

    """
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        posts=[]
        for post in Post.objects.all().order_by('-id'):
            a_post={'title':post.title,'scores_count':post.scores_count}
            the_score=Score.objects.filter(user=request.user,post=post)
            if the_score.exists():
                a_post['score']=the_score.first().score
            else:
                a_post['score']=post.score
            posts.append(a_post)

        if len(posts):
            return Response({'ok':True,'posts':posts},status=status.HTTP_200_OK)
        
        return Response({'ok':False,'detail':'No posts exist'},status=status.HTTP_404_NOT_FOUND)

