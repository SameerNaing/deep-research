from rest_framework import serializers

from research import models

class TicketSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    estimated_time = serializers.CharField(max_length=255)
    
    class Meta: 
        model = models.Project
        fields = ["id", "title", "description", "created_at", "status", "estimated_time"]
    
    def create(self, validated_data):
        validated_data["created_by"] = self.context["user"]
        return super().create(validated_data)