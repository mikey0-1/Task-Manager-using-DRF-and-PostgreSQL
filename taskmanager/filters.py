import django_filters
from .models import Task
from datetime import date
from django import forms

class TaskFilter(django_filters.FilterSet):
    due_date = django_filters.DateFilter(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    overdue = django_filters.BooleanFilter(
        method="filter_overdue",
        widget=forms.CheckboxInput(),
        label='Overdue'
    )

    today = django_filters.BooleanFilter(
        method="filter_today",
        widget=forms.CheckboxInput(),
        label='Today'
    )

    upcoming = django_filters.BooleanFilter(
        method="filter_upcoming",
        widget=forms.CheckboxInput(),
        label='Upcoming'
    )

    class Meta:
        model = Task
        fields = ['status', 'due_date']

    def filter_overdue(self, queryset, name, value):
        if value:
            return queryset.filter(
                due_date__lt=date.today(),
                status__in=['pending']
            )
        return queryset

    def filter_today(self, queryset, name, value):
        if value:
            return queryset.filter(due_date=date.today())
        return queryset

    def filter_upcoming(self, queryset, name, value):
        if value:
            return queryset.filter(due_date__gt=date.today())
        return queryset