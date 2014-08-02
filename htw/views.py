from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import HTW
# Create your views here.

class HTWListView(ListView):
	model = HTW

class HTWCreateView(CreateView):
	model = HTW

class HTWUpdateView(UpdateView):
	model = HTW

class HTWDeleteView(DeletView):
	model = HTW
