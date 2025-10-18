from django.db import models

from research import constants
from .base_model import BaseModel


class TicketStatus(models.TextChoices):
    NOT_STARTED = constants.TICKET_STATUS_NOT_STARTED, "Not Started"
    IN_PROGRESS = constants.TICKET_STATUS_PROGRESS, "In Progress"
    FINISHED = constants.TICKET_STATUS_FINISHED, "Finished"
    
    
class Ticket(BaseModel):
    status = models.CharField(
        max_length=1,
        choices=TicketStatus.choices,
        default=TicketStatus.NOT_STARTED,
    )
    
    estimated_time = models.CharField(max_length=255, blank=True, default="")
    
    
    