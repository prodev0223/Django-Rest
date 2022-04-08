# Create your views here.

from django.views.generic import TemplateView
from apps.main.api_calls import get_invoices_from_robolab_api
from apps.main.constants import DEFAULT_END_DATE, DEFAULT_START_DATE
from apps.main.forms import FilterForm
from django.template.response import TemplateResponse
from apps.main.models import Invoice

 
class InvoiceTableView(TemplateView):
    template_name = "main/table.html"

    def get(self, request, *args, **kwargs):
        """
        This method will render the invoice list to the user based on default start date and default end date.
        """
        ctx = self.get_context_data(**kwargs)
        from_date = DEFAULT_START_DATE
        to_date = DEFAULT_END_DATE
        get_invoices_from_robolab_api(from_date, to_date)
        records = Invoice.get_invoices_for_dates(from_date, to_date)
        form = FilterForm(initial={
            'from_date': from_date,
            'to_date': to_date
        })
        ctx.update(
            {
                'records': records,
                'form': form,
                'from_date': from_date,
                'to_date': to_date,
                'records_count': len(records)
            }
        )
        return TemplateResponse(request, 'main/table.html', context=ctx)

    def post(self, request, *args, **kwargs):
        """
        This method will render the filter data to the user based on from date and to date submitted by the user
        from the form
        """
        ctx = self.get_context_data(**kwargs)
        form = FilterForm(data=request.POST)
        from_date = DEFAULT_START_DATE
        to_date = DEFAULT_END_DATE
        group_by = None
        if form.is_valid():
            from_date = self.request.POST.get('from_date')
            to_date = self.request.POST.get('to_date')
            group_by = self.request.POST.get('group_by')
            get_invoices_from_robolab_api(from_date, to_date)
            records = Invoice.get_invoices_for_dates(from_date, to_date, group_by_field_name=group_by)
        else:
            records = []
        ctx.update(
            {
                'records': records,
                'form': form,
                'from_date': from_date,
                'to_date': to_date,
                'records_count': len(records),
                'group_by': group_by
            }
        )
        return TemplateResponse(request, 'main/table.html', context=ctx)
