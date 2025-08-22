from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import  PageNumberPagination, LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .filters import MovieFilter, ActorFilter, ReviewFilter
from .serializers import *
from .models import *


# class CustomPagination(LimitOffsetPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 100


# class ExampleAPIView(APIView):
#     def get(self, request):
#         return Response(
#             "Bu DRF'dagi 1-darsda yozildi"
#         )


class ActorsAPIView(APIView):
    def get(self,request):
        actors = Actor.objects.all()

        # search = request.GET.get('search')
        # if search:
        #     actors = actors.filter(name__icontains=search)

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

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('user', )
    ordering_fields = ('rate', 'created_at',)
    filterset_fields = ('user', 'movie')
    filterset_class = ReviewFilter

    # pagination_class = CustomPagination
    # page_size = 2
    # page_size_query_param = 'page_size'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReviewSafeSerializer
        return self.serializer_class

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name', )
    ordering_fields = ('name', 'year',)
    filterset_fields = ('name',)
    filterset_class = MovieFilter


    def get_serializer_class(self):
        if self.action == 'add_actor':
            return ActorSerializer
        return self.serializer_class

    @action(detail=True, methods=['get'])
    def actors(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='add-actors')
    def add_actor(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            actor = serializer.instance
            movie.actors.add(actor)
            response = {
                'success':True,
                'data':serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name',)
    ordering_fields = ('birth_date',)
    filterset_fields = ('country','gender')
    filterset_class = ActorFilter
