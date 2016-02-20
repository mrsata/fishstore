from Fishes import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'fishes', view.FishViewSet)
router.register(r'stores', view.StoreViewSet)
