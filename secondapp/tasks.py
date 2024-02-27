from celery import shared_task


from celery.utils.log import get_task_logger
from .email import send_feedback_email

logger = get_task_logger(__name__)

@shared_task(name='send_feedback_email_task')

def send_feedback_email_task(name, email, feedback):
    logger.info("sent Feedback email")    
    return send_feedback_email(name, email, feedback)