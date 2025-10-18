from django.urls import path, include

from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from research import views

router = routers.DefaultRouter()
router.register(prefix="projects", viewset=views.ProjectViewSet)

ticket_router = nested_routers.NestedSimpleRouter(
    router, 
    'projects',
    lookup='project'
)
ticket_router.register("tickets", viewset=views.TicketViewSet, basename='project-tickets')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(ticket_router.urls))
]