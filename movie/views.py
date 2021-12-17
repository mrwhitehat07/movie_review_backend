from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from movie.models import Movie

class MovieView(APIView):

    def get(self, request):
        return HttpResponse("get request")

    def post(self, request):
        return HttpResponse("post request")

    def put(self, request):
        return HttpResponse("update request")

    def delete(self, request):
        return HttpResponse("delete request")