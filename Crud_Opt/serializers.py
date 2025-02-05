from rest_framework import serializers
from django.utils import timezone
from .models import Plan

class PlanSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    update_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Plan
        fields = ['id', 'name', 'place', 'phone', 'email', 'created_at', 'update_at']

    def get_created_at(self, obj): 
        local_time = timezone.localtime(obj.created_at)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")
    
    def get_update_at(self, obj): 
        local_time = timezone.localtime(obj.update_at)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")