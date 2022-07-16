from rest_framework.response import Response
from rest_framework.decorators import api_view

from comments.api.serializers import CommentsSerializer
from comments.models import CommentsModel


@api_view(['GET', ])
def comments_view(request):
    if request.method == 'GET':
        about = CommentsModel.objects.all()
        serializer = CommentsSerializer(about, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = CommentsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)
    #

