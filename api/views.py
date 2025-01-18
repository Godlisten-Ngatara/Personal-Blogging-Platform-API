from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def getPosts(request):

    # retrieving all the objects from the database
    posts = Post.objects.all()

    # serializing post objects
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)
