from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FoodAndDiet,ShoppingAndGoods,LifestyleAndHabits,WasteManagement,HomeEnergyUsage,Transportation,UserProfile,CarbonOffsetProject

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','date_joined','is_active']

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = ['id', 'user', 'daily_commute', 'fuel_type', 'commute_distance', 'air_travel']
        read_only_fields = ['user']

class HomeEnergyUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeEnergyUsage
        fields = ['id', 'user', 'living_situation', 'household_size', 'energy_source', 'monthly_consumption']
        read_only_fields = ['user']

class FoodAndDietSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodAndDiet
        fields = ['id', 'user', 'diet_type', 'dairy_meat_meal_frequency', 'food_source']
        read_only_fields = ['user']

class ShoppingAndGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingAndGoods
        fields = ['id', 'user', 'clothing_purchase', 'general_purchases', 'recycling']
        read_only_fields = ['user']

class WasteManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteManagement
        fields = ['id', 'user', 'waste_disposal', 'composting']
        read_only_fields = ['user']

class LifestyleAndHabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifestyleAndHabits
        fields = ['id', 'user', 'energy_saving', 'water_usage']
        read_only_fields = ['user']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',                        
            'user',                      
            'daily_carbon_footprint',    
            'yearly_carbon_footprint',   
            'transportation_emissions',  
            'home_energy_emissions',     
            'food_emissions',            
            'shopping_emissions',        
            'waste_emissions',           
            'lifestyle_emissions',       
            'created_at',                
            'modified_at',  
            'goal'             
        ]
        read_only_fields = ['id', 'created_at', 'modified_at','user'] 

class CarbonOffsetProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonOffsetProject
        fields = [
            'id', 'name', 'description', 'location', 'offset_potential_tons', 
            'category', 'benefits', 'activities', 'link', 'image_url'
        ]