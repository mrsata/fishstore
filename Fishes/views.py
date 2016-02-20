from django.shortcuts import render, get_object_or_404
from Fishes.models import Fish, Store
# Create your views here.

from rest_framework.viewsets import ModelViewSet
from Fishes.serializers import FishSerializer, StoreSerializer

def index(request):
    fishes = Fish.objects.all()
    stores = Store.objects.order_by("-location").reverse()
    return render(request, 'Fishes/index.html', {"fishes": fishes, "stores": stores})

def details(request, store_id):
    stores = get_object_or_404(Store, pk = store_id)
    return render(request, "Fishes/detial.html", {"stores": stores})

class FishViewSet(ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
