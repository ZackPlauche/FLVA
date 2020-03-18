from django import forms
from .models import Contact, FAQ

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('question', )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('answer', )
