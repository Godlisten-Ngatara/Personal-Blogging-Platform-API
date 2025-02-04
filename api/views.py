from os import stat
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


@api_view(['PUT'])
def updatePost(request, post_id):

    # retrieving a single object from the database
    post = Post.objects.get(id=post_id)  # this is instance

    # here need instance for update data
    serializer = PostSerializer(post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Complete Data Updated'})
    return Response({'message: Something is wrong'})
