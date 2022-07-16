from rest_framework.decorators import api_view
from rest_framework.response import Response

from partners.api.serializers import PartnersSerializer
from partners.models import PartnersModel


@api_view(['GET', ])
def partners_view(request):
    if request.method == 'GET':
        about = PartnersModel.objects.all()
        serializer = PartnersSerializer(about, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = PartnersSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)


