from .api_serializers import storeJSONSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def sample_poster(request):
    serializer = storeJSONSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.save()
        return Response(storeJSONSerializer(data).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
