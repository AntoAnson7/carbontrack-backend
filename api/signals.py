from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transportation,HomeEnergyUsage,FoodAndDiet,WasteManagement,LifestyleAndHabits,ShoppingAndGoods,UserProfile


@receiver(post_save, sender=Transportation)
@receiver(post_save, sender=HomeEnergyUsage)
@receiver(post_save, sender=ShoppingAndGoods)
@receiver(post_save, sender=FoodAndDiet)
@receiver(post_save, sender=WasteManagement)
@receiver(post_save, sender=LifestyleAndHabits)
def update_user_profile_carbon_footprint(sender,instance,created,**kwargs):
     if not created:
        user_profile = UserProfile.objects.filter(user=instance.user).first()
        if user_profile:
            user_profile.calculate_daily_carbon_footprint()
            user_profile.save()
