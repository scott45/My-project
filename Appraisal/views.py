from django.views import generic
from .models import Department
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "departments"

    def get_queryset(self):
        return Department.objects.all()


class DetailView(generic.DetailView):
    model = Department
    template_name = "detail.html"


class DepartmentCreate(CreateView):
    model = Department
    fields = ['Name', 'Leader', 'Department_logo', 'is_favorite']
    template_name = 'department_form.html'


class DepartmentUpdate(CreateView):
    model = Department
    fields = ['Name', 'Leader', 'Department_logo', 'is_favorite']


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        global username, password
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('index.html')

        return render(request, self.template_name, {'form': form})
