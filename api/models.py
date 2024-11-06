from statistics import mode
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User

class Transportation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='transportation')
    # Choices
    commute_choices = (('CAR','Car'),('PUBLIC_TRANSPORT','Public Transport'),('BICYCLE','Bicycle'),('WALKING','Walking'),('CARPOOL','Carpool'))    
    fuel_choices = (('PETROL','Petrol'),('DIESEL','Diesel'),('ELECTRIC','Electric'))
    
    # Fields
    daily_commute = models.CharField(max_length=25, choices=commute_choices)
    fuel_type = models.CharField(max_length=25, choices=fuel_choices,blank=True,null=True)
    commute_distance = models.PositiveIntegerField(default=0)
    air_travel = models.PositiveIntegerField(default=0)

class HomeEnergyUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='home_energy_use')
    # Choices
    living_choices = (('APARTMENT','Apartment'),('DETATCHED_HOUSE','Detatched House'),('SHARED_HOUSING','Shared Housing'))
    energy_choices = (('GRID','Grid'),('SOLAR','Solar'),('NATURAL_GAS','Natural Gas'),('OTHER','Other'),('HYDROELECTRIC','Hydroelectric'))

    # Fields
    living_situation = models.CharField(max_length=50,choices=living_choices)
    household_size = models.PositiveIntegerField(default=1)
    energy_source = models.CharField(max_length=25,choices=energy_choices)
    monthly_consumption = models.PositiveIntegerField(default=0)

class FoodAndDiet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='food_and_diet')
    # Choices
    diet_choices = (('VEGAN','Vegan'),('VEGETARIAN','Vegetarian'),('PESCATARIAN','Pescatarian'),('OMNIVORE','Omnivore'),('MEAT_HEAVY','Meat-Heavy'))
    source_choices = (('ALWAYS','Always'),('OFTEN','Often'),('SOMETIMES','Sometimes'),('RARELY','Rarely'),('NEVER','Never'))    

    # Fields
    diet_type = models.CharField(max_length=25,choices=diet_choices)
    dairy_meat_meal_frequency = models.PositiveIntegerField(default=0)
    food_source = models.CharField(max_length=25,choices=source_choices)

class ShoppingAndGoods(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='shopping_and_goods')
    # Choices
    shopping_choices = (('WEEKLY','Weekly'),('MONTHLY','Monthly'),('QUARTERLY','Quarterly'),('YEARLY','Yearly'))
    recycle_choices = (('MOST','Most'),('ABOUT_HALF','About Half'),('SOME','Some'),('NONE','None'))

    # Fields
    clothing_purchase = models.CharField(max_length=25,choices=shopping_choices)
    general_purchases = models.CharField(max_length=25,choices=shopping_choices)
    recycling = models.CharField(max_length=25,choices=recycle_choices)

class WasteManagement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='waste_management')
    # Choices
    disposal_choices = (('DAILY','Daily'),('EVERY_FEW','Every Few Days'),('WEEKLY','Weekly'))
    composting_choices = (('YES','Yes'),('NO','No'),('PLANNING_TO','Planning To'))

    # Fields
    waste_disposal = models.CharField(max_length=25,choices=disposal_choices)
    composting = models.CharField(max_length=25,choices=composting_choices)

class LifestyleAndHabits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='lifestyle_and_habits')
    # Choices
    energy_saving_choices = (('ALWAYS','Always'),('OFTEN','Often'),('SOMETIMES','Sometimes'),('RARELY','Rarely'),('NEVER','Never'))    
    water_usage_choices = (('CONSCIOUS','Conscious'),('SOMETIMES','Sometimes'),('RARELY','Rarely'),('NEVER','Never'))    

    # Fields
    energy_saving = models.CharField(max_length=25,choices=energy_saving_choices)
    water_usage = models.CharField(max_length=25,choices=water_usage_choices)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_carbon_footprint = models.FloatField(default=0.0)
    yearly_carbon_footprint = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Daily emissions from individual activities
    transportation_emissions = models.FloatField(default=0.0)
    home_energy_emissions = models.FloatField(default=0.0)
    food_emissions = models.FloatField(default=0.0)
    shopping_emissions = models.FloatField(default=0.0)
    waste_emissions = models.FloatField(default=0.0)
    lifestyle_emissions = models.FloatField(default=0.0)
    
    def save(self, *args, **kwargs):
        self.calculate_daily_carbon_footprint()
        super().save(*args, **kwargs)

    def calculate_daily_carbon_footprint(self):
        user = self.user
        if user is None:
            raise ValueError("User instance is None. Cannot calculate carbon footprint.")

        # Fetch user data
        transportation = Transportation.objects.filter(user=user).first()
        home_energy = HomeEnergyUsage.objects.filter(user=user).first()
        food_and_diet = FoodAndDiet.objects.filter(user=user).first()
        shopping_and_goods = ShoppingAndGoods.objects.filter(user=user).first()
        waste_management = WasteManagement.objects.filter(user=user).first()
        lifestyle_and_habits = LifestyleAndHabits.objects.filter(user=user).first()

        # 1. Transportation Emissions
        commute_emissions = 0
        if transportation.daily_commute == 'CAR':
            commute_emissions = transportation.commute_distance * 0.251  # kg CO₂/km
        elif transportation.daily_commute == 'PUBLIC_TRANSPORT':
            commute_emissions = transportation.commute_distance * 0.065  # kg CO₂/km
        elif transportation.daily_commute == 'BICYCLE' or transportation.daily_commute == 'WALKING':
            commute_emissions = 0  # No emissions
        elif transportation.daily_commute == 'CARPOOL':
            commute_emissions = transportation.commute_distance * 0.126  # kg CO₂/km

        # Air Travel Emissions
        air_travel_emissions = 0
        if transportation.air_travel < 1500:
            air_travel_emissions = 250 / 365
        elif 1500 <= transportation.air_travel <= 4000:
            air_travel_emissions = 500 / 365
        else:
            air_travel_emissions = 1000 / 365

        total_transportation_emissions = commute_emissions + air_travel_emissions

        # 2. Home Energy Usage Emissions
        energy_source_emission_factor = {
            'GRID_ELECTRICITY': 0.92,
            'SOLAR': 0,
            'HYDROELECTRIC': 0,
            'NATURAL_GAS': 5.3,
            'OTHER': 4
        }.get(home_energy.energy_source, 0)

        total_home_energy_emissions = (home_energy.monthly_consumption * energy_source_emission_factor) / 30

        # 3. Food and Diet Emissions
        diet_emissions = {
            'VEGAN': 2.5,
            'VEGETARIAN': 3.5,
            'PESCATARIAN': 4.0,
            'OMNIVORE': 5.0,
            'MEAT_HEAVY': 7.0
        }.get(food_and_diet.diet_type, 5.0)

        # Adjust based on food sourcing sustainability
        food_source_adjustment = {
            'ALWAYS': -0.5,
            'OFTEN': -0.3,
            'SOMETIMES': 0,
            'RARELY': 0.3,
            'NEVER': 0.5
        }.get(food_and_diet.food_source, 0)

        total_food_emissions = diet_emissions + food_source_adjustment

        # 4. Shopping and Goods Emissions
        clothing_emissions = {
            'WEEKLY': 0.5,
            'MONTHLY': 0.2,
            'QUARTERLY': 0.1,
            'YEARLY': 0.05
        }.get(shopping_and_goods.clothing_purchase, 0)

        general_purchases_emissions = {
            'WEEKLY': 0.5,
            'MONTHLY': 0.2,
            'QUARTERLY': 0.1,
            'YEARLY': 0.05
        }.get(shopping_and_goods.general_purchases, 0)

        # Adjust based on recycling habits
        recycling_adjustment = {
            'MOST': -0.3,
            'ABOUT_HALF': -0.15,
            'SOME': 0.15,
            'NONE': 0.3
        }.get(shopping_and_goods.recycling, 0)

        total_shopping_emissions = clothing_emissions + general_purchases_emissions + recycling_adjustment

        # 5. Waste Management Emissions
        waste_emission_values = {
            'DAILY': 1.0,
            'EVERY_FEW_DAYS': 0.5,
            'WEEKLY': 0.2
        }

        waste_emissions = waste_emission_values.get(waste_management.waste_disposal, 0)

        # Adjust for composting
        composting_adjustment = {
            'YES': -0.3,
            'PLANNING_TO': -0.15,
            'NO': 0
        }.get(waste_management.composting, 0)

        total_waste_emissions = waste_emissions + composting_adjustment

        # 6. Lifestyle and Habits Emissions
        energy_saving_emissions = {
            'ALWAYS': -1.0,
            'OFTEN': -0.5,
            'SOMETIMES': 0,
            'RARELY': 0.5,
            'NEVER': 1.0
        }.get(lifestyle_and_habits.energy_saving, 0)

        water_usage_emissions = {
            'CONSCIOUS': -0.5,
            'SOMETIMES': 0,
            'RARELY': 0.5,
            'NEVER': 1.0
        }.get(lifestyle_and_habits.water_usage, 0)

        total_lifestyle_emissions = energy_saving_emissions + water_usage_emissions

        # Total Daily Carbon Footprint
        total_daily_footprint = (
            total_transportation_emissions +
            total_home_energy_emissions +
            total_food_emissions +
            total_shopping_emissions +
            total_waste_emissions +
            total_lifestyle_emissions
        )



        self.daily_carbon_footprint = total_daily_footprint
        self.yearly_carbon_footprint = self.daily_carbon_footprint*365
        self.transportation_emissions = total_transportation_emissions
        self.home_energy_emissions = total_home_energy_emissions
        self.food_emissions = total_food_emissions
        self.shopping_emissions = total_shopping_emissions
        self.waste_emissions = total_waste_emissions
        self.lifestyle_emissions = total_lifestyle_emissions

