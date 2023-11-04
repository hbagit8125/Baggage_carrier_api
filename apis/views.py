from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import carrier
from .serializers import CarrierSerializer

@api_view(['GET', 'POST'])
def carrier_data(request):
    if request.method == 'GET':
        carriers = carrier.objects.all()
        if carriers:
            serializer = CarrierSerializer(carriers, many=True)
        else:
            serializer = CarrierSerializer()
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarrierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

