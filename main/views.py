from django.shortcuts import render, redirect
from .forms import NewsletterSubscriptionForm

def index(request):
    return render(request, 'index.html')


def subscribe_to_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_success')  
    else:
        form = NewsletterSubscriptionForm()

    return render(request, 'subscribe.html', {'form': form})
