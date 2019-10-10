from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Student
from .form import StudentForm


# def index(request):
#     students = Student.get_all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             # 因为构建form用的model form 所以省去手动构建student对象
#             form.save()
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         form = StudentForm()
#     return render(request, 'index.html', context={'students': students, 'form': form})


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {'students': students}
        return context

    def get(self, request):
        context = self.get_context()
        context.update({
            'form': StudentForm()
        })
        return render(request, 'index.html', context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            # 因为构建form用的model form 所以省去手动构建student对象
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            context = self.get_context()
            context.update({
                'form': StudentForm()
            })
            return render(request, 'index.html', context)
