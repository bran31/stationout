import django_filters

from django_filters import CharFilter, DateFilter
from .models import *

class OutFilter(django_filters.FilterSet):
#   status = CharFilter(field_name="status", lookup_expr="icontains")
    start_date = DateFilter(field_name="last_bhs", lookup_expr="gte")
#    next_date = DateFilter(field_name="next_bhs", lookup_expr="gte")
    last_date = DateFilter(field_name="full_duty", lookup_expr="gte")
    
    class Meta:
        model = Quarintine
        fields = ['last_name', 'status',]
        