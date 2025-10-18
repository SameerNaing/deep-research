from django.db import models

from research import constants
from .base_model import BaseModel


class ProjectStatus(models.TextChoices):
    IN_PROGRESS = constants.PROJECT_STATUS_IN_PROGRESS, "In Progress"
    ARCHIVED = constants.PROJECT_STATUS_ARCHIVED, "Archived"
    COMPLETE = constants.PROJECT_STATUS_COMPLETE, "Complete"
    ON_HOLD = constants.PROJECT_STATUS_HOLD, "On Hold"

class Project(BaseModel):
    progress = models.SmallIntegerField(default=0)
    status = models.CharField(max_length=1, choices=ProjectStatus.choices, default=ProjectStatus.IN_PROGRESS)
    