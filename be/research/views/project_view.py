from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, pagination

from research import serializers, models

@extend_schema(tags=['Projects'])
class ProjectViewSet(ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.LimitOffsetPagination
    
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        
        return context