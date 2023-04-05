from rest_framework import views, status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class MyAccount(views.APIView):
    def get(self, *args, **kwargs):
        profile = Profile.objects.get(user_id=self.request.user.id) or None
        if profile:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
