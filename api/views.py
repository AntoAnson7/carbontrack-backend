from xml.dom import ValidationErr
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer,UserProfileSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from .models import FoodAndDiet,ShoppingAndGoods,LifestyleAndHabits,WasteManagement,HomeEnergyUsage,Transportation,UserProfile,CarbonOffsetProject
from django.shortcuts import get_object_or_404
from .serializers import TransportationSerializer,HomeEnergyUsageSerializer,FoodAndDietSerializer,WasteManagementSerializer,ShoppingAndGoodsSerializer,LifestyleAndHabitsSerializer,CarbonOffsetProjectSerializer
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

#! User test route
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CustomTokenRefreshView(TokenRefreshView):
    """Use refresh token to obtain new refresh and access tokens and then blacklist the old refresh token"""
    def post(self, request, *args, **kwargs):
        old_refresh_token = request.data.get('refresh')
        try:
            token = RefreshToken(old_refresh_token)

            new_access = str(token.access_token)
            new_refresh = str(token)

            token.blacklist()

            return Response({
                'access':new_access,
                'refresh':new_refresh
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error':'Invalid or Blacklisted Token'}, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Register a new user"""
    userdata = request.data
    serializer = UserSerializer(data = userdata)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Registstration successful','user':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'msg':'Registstration Failed','errors':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """Login a user with username and password and get user details and Refresh and Access token for Authorization"""
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username = username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'msg':'Login Successful',
            'user':UserSerializer(user).data,
            'access':str(refresh.access_token),
            'refresh':str(refresh)
        }, status=status.HTTP_200_OK )

    else:
        return Response({'msg':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)

class TransportationViewset(viewsets.ModelViewSet):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        username = self.request.data.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                serializer.save(user=user)
            except User.DoesNotExist:
                raise ValidationError("User with this username does not exist.")

        else:
            raise ValidationError("User ID is required.")


class HomeEnergyUsageViewset(viewsets.ModelViewSet):
    queryset = HomeEnergyUsage.objects.all()
    serializer_class = HomeEnergyUsageSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        username = self.request.data.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                serializer.save(user=user)
            except User.DoesNotExist:
                raise ValidationError("User with this username does not exist.")

        else:
            raise ValidationError("User ID is required.")


class FoodAndDietViewset(viewsets.ModelViewSet):
    queryset = FoodAndDiet.objects.all()
    serializer_class = FoodAndDietSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        username = self.request.data.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                serializer.save(user=user)
            except User.DoesNotExist:
                raise ValidationError("User with this username does not exist.")

        else:
            raise ValidationError("User ID is required.")


class WasteManagementViewset(viewsets.ModelViewSet):
    queryset = WasteManagement.objects.all()
    serializer_class = WasteManagementSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        username = self.request.data.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                serializer.save(user=user)
            except User.DoesNotExist:
                raise ValidationError("User with this username does not exist.")

        else:
            raise ValidationError("User ID is required.")


class ShoppingAndGoodsViewset(viewsets.ModelViewSet):
    queryset = ShoppingAndGoods.objects.all()
    serializer_class = ShoppingAndGoodsSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        username = self.request.data.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                serializer.save(user=user)
            except User.DoesNotExist:
                raise ValidationError("User with this username does not exist.")

        else:
            raise ValidationError("User ID is required.")


class LifestyleAndHabitsViewset(viewsets.ModelViewSet):
    queryset = LifestyleAndHabits.objects.all()
    serializer_class = LifestyleAndHabitsSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        username = self.request.data.get('username')
        if username:
            try:
                user = User.objects.get(username=username)
                serializer.save(user=user)
            except User.DoesNotExist:
                raise ValidationError("User with this username does not exist.")

        else:
            raise ValidationError("User ID is required.")


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserProfile.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            raise ValidationError("User is not authenticated.")

class UserProfileDataView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        user = request.user

        transportation_data = Transportation.objects.filter(user=user).first()  # Adjust if needed
        energy_data = HomeEnergyUsage.objects.filter(user=user).first()
        food_diet_data = FoodAndDiet.objects.filter(user=user).first()
        waste_management_data = WasteManagement.objects.filter(user=user).first()
        lifestyle_data = LifestyleAndHabits.objects.filter(user=user).first()
        shopping_goods_data = ShoppingAndGoods.objects.filter(user=user).first()

        transportation_serializer = TransportationSerializer(transportation_data)
        energy_serializer = HomeEnergyUsageSerializer(energy_data)
        food_diet_serializer = FoodAndDietSerializer(food_diet_data)
        waste_management_serializer = WasteManagementSerializer(waste_management_data)
        lifestyle_serializer = LifestyleAndHabitsSerializer(lifestyle_data)
        shopping_goods_serializer = ShoppingAndGoodsSerializer(shopping_goods_data)

        user_data = {
            'transportation': transportation_serializer.data,
            'homeEnergy': energy_serializer.data,
            'foodDiet': food_diet_serializer.data,
            'wasteManagement': waste_management_serializer.data,
            'lifestyleHabits': lifestyle_serializer.data,
            'shoppingGoods': shopping_goods_serializer.data,
        }

        return Response(user_data)

@api_view(['GET'])
@permission_classes([AllowAny])
def gettokenuser(request):
    user = request.user
    return Response({"user":UserSerializer(user).data},status=status.HTTP_200_OK)


class CarbonOffsetProjectViewSet(viewsets.ModelViewSet):
    queryset = CarbonOffsetProject.objects.all()
    serializer_class = CarbonOffsetProjectSerializer
    permission_classes = [IsAuthenticated]

class SetGoalView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Fetch the user profile for the authenticated user
            profile = UserProfile.objects.get(user=request.user)
            goal = request.data.get('goal')

            if goal is not None:
                profile.goal = goal  # Update the goal field
                profile.save()  # Save changes to the database

                return Response({"message": "Goal updated successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Goal value is required."}, status=status.HTTP_400_BAD_REQUEST)

        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)