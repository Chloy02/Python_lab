from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = FeedbackForm()  
            return render(request, 'feedback/feedback.html', {'form': form, 'success': True})
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form': form})

