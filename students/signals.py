# -*- coding: utf-8 -*-
import logging

from django.db.models.signals import post_save,post_delete
from django.core.signals import request_started, request_finished
from django.dispatch import receiver

from .models import Student
count_request = 0

@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated student into log file"""

    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    if kwargs['created']:
        logger.info("Student added: %s %s (ID: %d)", student.first_name,
            student.last_name, student.id)
    else:
        logger.info("Student updated: %s %s (ID: %d)", student.first_name,
            student.last_name, student.id)

@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
    """Writes information about deleted student into log file"""

    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    logger.info("Student deleted: %s %s (ID: %d)", student.first_name,
        student.last_name, student.id)

#Homework
#@receiver(request_finished)
#def finish_callback(sender, **kwargs):
#    global count_request
#    count_request = count_request + 1

    