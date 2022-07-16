from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from free_lesson.models import FreeLessonModel
from free_lesson.api.serializers import FreeLessonSerializer


@api_view(['POST'])
def post_data(request):
    serializer = FreeLessonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

