from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from api.models import Person, Company
from api.serializers import PersonSerializer, CompanySerializer, MinimalPersonSerializer


class CompanyView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class PersonView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CommonFriendsView(APIView):

    def get(self, request, user_id, comparison_user_id):
        user_one = get_object_or_404(Person, pk=user_id)
        user_two = get_object_or_404(Person, pk=comparison_user_id)
        common_friends = set(
            user_one.friends.filter(eye_color="brown", deceased=False).values_list('name', flat=True)
        ).intersection(
            user_two.friends.filter(eye_color="brown", deceased=False).values_list('name', flat=True)
        )
        output = {
            "user_one": MinimalPersonSerializer(user_one).data,
            "user_two": MinimalPersonSerializer(user_two).data,
            "common_friends": list(common_friends)
        }

        return Response(output)
