from django import forms
from .models import Contact, FAQ

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')

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
