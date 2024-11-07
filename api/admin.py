from django.contrib import admin

# Register your models here.
from .models import FoodAndDiet,ShoppingAndGoods,LifestyleAndHabits,WasteManagement,HomeEnergyUsage,Transportation,UserProfile,CarbonOffsetProject

admin.site.register(FoodAndDiet)
admin.site.register(ShoppingAndGoods)
admin.site.register(LifestyleAndHabits)
admin.site.register(WasteManagement)
admin.site.register(HomeEnergyUsage)
admin.site.register(Transportation)
admin.site.register(UserProfile)
admin.site.register(CarbonOffsetProject)