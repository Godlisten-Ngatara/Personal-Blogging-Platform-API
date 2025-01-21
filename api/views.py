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


@api_view(['GET'])
def getPost(request, id):

    # retrieving a single object from the database
    post = Post.objects.get(id=id)

    # serializing the object
    serializer = PostSerializer(post)

    return Response(serializer.data)


@api_view(['POST'])
def savePost(request):

    # serializing data object

    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
