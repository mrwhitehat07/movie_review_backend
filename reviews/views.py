from http import server
from django.http.response import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework import generics
from django.utils.decorators import method_decorator
from movie.models import Movie
from moviereviews.decorators import check_token
from user.serializers import ProfileSeriL
from .models import Review
from user.models import Profile, UserProfile
from .serializers import ReviewSerializer, UpdateReviewSerializer

def movie_reviews(self, pk):
    movies = Review.objects.filter(movie=pk)
    serialized_data = ReviewSerializer(movies, many=True)
    return JsonResponse(serialized_data.data, safe=False)

def reviews(self, rid):
    review = Review.objects.get(id=rid)
    serialized_data = ReviewSerializer(review, many=False)
    return JsonResponse(serialized_data.data, safe=False)

@method_decorator(check_token, name='dispatch')
class Reviews(APIView):
    def post(self, request, pk, *args, **kwargs):
        data = request.data
        data["user"] = UserProfile.objects.get(username=self.kwargs["user"]).id
        data["movie"] = Movie.objects.get(id=pk).id
        data["rating"] = request.data.get("rating")
        data["review"] = request.data.get("review")
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status": "done"})
        else:
            return JsonResponse({ "error": serializer.errors })

@method_decorator(check_token, name='dispatch')
class UpdateReview(APIView):
    def put(self, request, pk, rid, *args, **kwargs):
        data = request.data
        data["user"] = UserProfile.objects.get(username=self.kwargs["user"]).id
        data["movie"] = Movie.objects.get(id=pk).id
        data["rating"] = request.data.get("rating")
        data["review"] = request.data.get("review")
        review = Review.objects.get(id=rid)
        if review.user.id == data["user"]:
            serializer = UpdateReviewSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({ "message": "updated" })
            else:
                return JsonResponse({ "error": serializer.errors })
        else:
            return JsonResponse({ "error": "u r not real author" })
