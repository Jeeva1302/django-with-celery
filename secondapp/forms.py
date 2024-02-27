from django import forms

from secondapp.tasks import send_feedback_email_task

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Fullname', min_length=4,max_length=25,
                           widget=forms.TextInput(attrs={'class':'form-control mb-3'
                         , 'placeholder':'Fullname', 'id':'form.firstname'}))
    
    email = forms.EmailField(label='Email',max_length=200,
                           widget=forms.TextInput(attrs={'class':'form-control mb-3'
                         , 'placeholder':'Email', 'id':'form.email'}))
    
    feedback = forms.CharField(label='feedback', widget=forms.TextInput(attrs={'class':'form-control mb-3'
                         , 'placeholder':'Feedback', 'id':'form.feedback'}))
    
    def send_email(self):
        send_feedback_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'],self.cleaned_data['feedback']
        )
        