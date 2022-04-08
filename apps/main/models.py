from django.db import models
from django.db.models import QuerySet, Sum

from apps.main.constants import FILTER_FIELDS_MAPPING

{'amount_total_cost': 0.0,
 'amount_total_gross_profit': 0.0,
 'date_due': '2022-03-31',
 'amount_total_company_currency': 0.07,
 'partner_code': '1234',
 'partner_name': 'test123515234',
 'number': 'MIB266',
 'date_invoice': '2022-03-31',
 'currency': 'EUR',
 'state': 'Apmokėta',
 'amount_untaxed_company_currency': 0.06,
 'amount_tax_company_currency': 0.01,
 'amount_residual_company_currency': 0.0, 'type': 'Client Invoice'}

 
class Invoice(models.Model):
    """
    This model will store the invoice details received from the API

    I chose using database over running loop to evaluate records because loops are slow
    and it's always faster to work with query then using loop in the code.
    """
    amount_total_cost = models.DecimalField(decimal_places=2, max_digits=10)
    amount_total_gross_profit = models.DecimalField(decimal_places=2, max_digits=10)
    date_due = models.DateField()
    amount_total_company_currency = models.DecimalField(decimal_places=2, max_digits=10)
    partner_code = models.CharField(max_length=50)
    partner_name = models.CharField(max_length=150)
    number = models.CharField(max_length=20)
    currency = models.CharField(max_length=5)
    state = models.CharField(max_length=5)
    type = models.CharField(max_length=5)
    date_invoice = models.DateField()
    amount_untaxed_company_currency = models.DecimalField(decimal_places=2, max_digits=10)
    amount_tax_company_currency = models.DecimalField(decimal_places=2, max_digits=10)
    amount_residual_company_currency = models.DecimalField(decimal_places=2, max_digits=10)

    @classmethod
    def populate_from_api_data(cls, records):
        """
        This method will populate the db table with the data received from the API.
        If the invoice number is already there, the values are updated, if not then
        new records are added to the table.
        """
        for record in records:
            # these two keys contained list values So I removed them just for the simplicity of the task
            # otherwise there are several ways to handle this like using M2M relation to other model created to store
            # the object present in those list. Or there Postgresql provides ListField that can store list of objects
            # directly. Also, there are many third party libraries that helps to provide this functionality of storing
            # list of objects in the db field
            record.pop('invoice_lines')
            record.pop('payments')
            cls.objects.update_or_create(
                number=record.get('number'),
                defaults=record
            )

    @classmethod
    def get_invoices_for_dates(cls, from_date, to_date, group_by_field_name=None):
        """
        This method return the list/queryset of all the invoice for the given date range.
        This function also handles group by company name feature.

        For the group by functionality it is better to use direct query as
        cls.objects.filter(
            date_due__gte=from_date,
            date_due__lte=to_date
        ).order_by('partner_name').distinct('partner_name')

        but as described in https://code.djangoproject.com/ticket/22696 sqlite doesn't support distinct
        functionality. So I've used the best possible work around to make the work done.

        I could have used postgresql database and would have done the task by only query but since this is a test
        task and setting up a database just to run a code would be so tedious for the one who checks the code. So I
        have done this in following manner.
        """
        qs = cls.objects.filter(
            date_due__gte=from_date,
            date_due__lte=to_date
        )
        if group_by_field_name:
            field_name = FILTER_FIELDS_MAPPING.get(group_by_field_name)
            list_of_unique_partner_names = qs.values_list(field_name, flat=True).distinct()
            unique_record_list = []
            for partner_name in list_of_unique_partner_names:
                unique_record_list.append(
                    dict(
                        partner_name=partner_name,
                        date_due=qs.filter(partner_name=partner_name).latest('date_due').date_due,
                        number=qs.filter(partner_name=partner_name).latest('date_due').number,
                        currency=qs.filter(partner_name=partner_name).latest('date_due').currency,
                        amount_residual_company_currency =qs.filter(partner_name=partner_name).aggregate(total_sum=Sum('amount_residual_company_currency')).get('total_sum') or 0
                    )
                )
            return unique_record_list
        return qs
