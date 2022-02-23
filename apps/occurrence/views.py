from django.views.generic.list import ListView
from .models import TaxonOccurrence

class OccurrenceListView(ListView):
    model = TaxonOccurrence
    paginate_by = 25
    template_name = 'occurrence/index.html'

    def get_queryset(self):
        return TaxonOccurrence.objects.order_by('-changed_date')
