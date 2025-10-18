from rest_framework import serializers

from research import models

class ProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    progress = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = models.Project
        fields = ["id", "title", "description", "created_at", "progress", "status"]
        
    
    def create(self, validated_data):
        validated_data["created_by"] = self.context["user"]
        return super().create(validated_data)