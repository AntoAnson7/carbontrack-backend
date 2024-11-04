from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views
from rest_framework.routers import DefaultRouter

# JWT Token setup
urlpatterns = [
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',views.CustomTokenRefreshView.as_view(), name='token_refresh')
]

router = DefaultRouter()
router.register(r'users', views.UserViewset,basename='user')
router.register(r'profile', views.UserProfileViewSet, basename='userprofile')

router.register(r'transportation', views.TransportationViewset,basename='transportation')
router.register(r'energy', views.HomeEnergyUsageViewset,basename='energy')
router.register(r'fooddiet', views.FoodAndDietViewset,basename='fooddiet')
router.register(r'wastemanagement', views.WasteManagementViewset,basename='wastemanagement')
router.register(r'lifestylehabits', views.LifestyleAndHabitsViewset,basename='lifestylehabits')
router.register(r'shoppinggoods', views.ShoppingAndGoodsViewset,basename='shoppinggoods')

# Router
urlpatterns += [
    path('', include(router.urls))
]



# Auth Routes
urlpatterns+=[
    path('register/',views.register_user, name='register_user'),
    path('login/',views.login_user, name='login_user')
]