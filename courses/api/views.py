from rest_framework.response import Response
from rest_framework.decorators import api_view

from courses.api.serializers import CourseSerializer
from courses.models import CoursesModels


@api_view(['GET', ])
def course_view(request):
    user = request.user
    if request.method == 'GET':
        about = CoursesModels.objects.all()
        serializer = CourseSerializer(about, many=True)
        return Response(serializer.data)

    # if not user.is_superuser:
    #     return Response("Only an admin can create !")
    # elif request.method == 'POST':
    #     serializer = CourseSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)


