from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *

from rest_framework import viewsets

def index(request):
    return render(request, 'index.html', {})

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# GET, POST
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# GET, PUT, DELETE
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingView(viewsets.ViewSet):
    def list(self, request):
        bookings = Booking.objects.all()
        serialized_bookings = BookingSerializer(bookings, many=True)
        return Response(serialized_bookings.data)

    def retrieve(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serialized_booking = BookingSerializer(booking)
        return Response(serialized_booking.data)

    def update(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serialized_booking = BookingSerializer(booking, data=request.data, partial=True)
        if serialized_booking.is_valid(raise_exception=True):
            serialized_booking.save()
        return Response({'status':'Booking data updated.', 'data': serialized_booking.data})

    def destroy(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return Response({'status':'Item deleted from database.'})

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status':'New booking created.', 'data': serializer.data})
