from secondapp.forms import FeedbackForm
from django.views.generic.edit import FormView
from django.http import HttpResponse

class FeedbackEmail(FormView):
    template_name = 'feedback.html'
    form_class = FeedbackForm
    
    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the Feedback!"
        return HttpResponse(msg)