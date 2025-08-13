from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .serializers import *
from .models import *

class ExampleAPIView(APIView):
    def get(self, request):
        return Response(
            "Bu DRF'dagi 1-darsda yozildi"
        )


class ActorsAPIView(APIView):
    def get(self,request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            Actor.objects.create(
                name=serializer.data['name'],
                gender=serializer.data['gender'],
                country=serializer.data['country'],
                birth_date=serializer.data['birth_date'],
            )
            return Response(serializer.data)
        return Response(serializer.errors)

class MoviesAPIView(APIView):
    def get(self, reuqest):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "succes":True,
                "data":serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "succes":False,
            "errors":serializer.errors
        }

        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class MovieRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Movie, pk=pk)

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubscriptionAPIView(APIView):
    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "succes":True,
                "data":serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "succes":False,
            "errors":serializer.errors
        }

        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Subscription, pk=pk)

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = SubscriptionSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = SubscriptionSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subscription = get_object_or_404(Subscription, pk=pk)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
