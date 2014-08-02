import datetime
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import HTW
# Create your views here.

class HTWListView(ListView):
	model = HTW

class HTWCreateView(CreateView):
	model = HTW
	
	def get_initial(self):
		return {'record_datetime': datetime.datetime.utcnow()}

class HTWUpdateView(UpdateView):
	model = HTW

class HTWDeleteView(DeleteView):
	model = HTW
