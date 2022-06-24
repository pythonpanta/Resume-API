from .models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProfileSerializer
class ResumeClass(APIView):
    def post(self,request,format=None):
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved successfully','status':'success','data':serializer.data},status=status.HTTP_201_CREATED)
        return Response({'msg':'data is not saved','status':'error',},status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,format=None):
        data=Profile.objects.all()
        serializer=ProfileSerializer(data,many=True)
        return Response({'msg':'data sending','status':'success','data':serializer.data},status=status.HTTP_200_OK)

