from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . forms import TodoForm
from . models import task

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import   UpdateView, DeleteView

# Create your views here.
class TaskListView(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'Task'

class TaskDetailView(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self) :
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
    

















def add(request):
    
    if request.method == "POST":
        name = request.POST.get("task",'')
        priority = request.POST.get("priority",'')
        date = request.POST.get("date",'')
        Task = task(name=name, priority=priority, date=date)
        Task.save()

    Task1 = task.objects.all()
    return render(request,'home.html',{'Task':Task1})

# def details(request):
#     return render(request,'details.html')

def delete(request,taskid):
    Task = task.objects.get(id = taskid)
    if request.method == 'POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    Task = task.objects.get(id = id)
    f = TodoForm(request.POST or None, instance = Task)
    if f. is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'Task':Task})


