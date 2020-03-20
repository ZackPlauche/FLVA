from django.shortcuts import render
from .models import Post, Contact, FAQ, AboutSection, Event
from .forms import ContactForm, QuestionForm, AnswerForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    events = Event.objects.all()
    context = {
    'posts': posts,
    'events':events,
    }
    return render(request, 'base/index.html', context)

def about(request):
    about_sections = AboutSection.objects.all()
    context = {'about_sections': about_sections}
    return render(request, 'base/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
        return HttpResponseRedirect('../thank-you/')
    else:
        form = ContactForm
        context = {'form': form}
        return render(request, 'base/contact.html', context)

def faq(request):
    faqs = FAQ.objects.all()
    form = AnswerForm()
    context = {
        'faqs':  faq,
        'form': form,
    }
    return render(request, 'base/faq.html', context)

def thank_you(request):
    return render(request, 'base/thankyou.html')
