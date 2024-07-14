from django.shortcuts import render, get_object_or_404, redirect
from .models import Hospital
from .forms import HospitalSearchForm
from Hospitals import models
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .forms import FeedbackForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'Hospitals/hospital_list.html', {'hospitals': hospitals})

def hospital_detail(request, pk=25):
    hospital = get_object_or_404(Hospital, pk=pk)
    return render(request, 'Hospitals/hospital_detail.html', {'hospital': hospital})


def search_hospitals(request):
    form = HospitalSearchForm()
    hospitals = []
    message = ''
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            hospitals = Hospital.objects.filter(
                Q(Name__icontains=query) |
                Q(Address__icontains=query) |
                Q(Specialties__icontains=query) |
                Q(contactnumber__icontains=query)
            )
            if not hospitals:
                message = 'No hospitals found matching your query.'
        else:
            message = 'Please enter a search query.'

    return render(request, 'Hospitals/search.html', {'form': form, 'hospitals': hospitals, 'message': message})



class HospitalListView(ListView):
    model = Hospital
    template_name = 'hospital_list.html'
    context_object_name = 'hospitals'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Hospital.objects.filter(Name__icontains=query)
        return Hospital.objects.all()

class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'Hospitals/hospital_detail.html'


   

def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = FeedbackForm()
    return render(request, 'Hospitals/home.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

