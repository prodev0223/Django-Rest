from decouple import config

API_BASE_URL = config('API_BASE_URL')
API_SECRET = config('API_SECRET')

DEFAULT_START_DATE = '2022-03-01'
DEFAULT_END_DATE = '2022-04-30'

GROUP_BY_NONE = ''
GROUP_BY_COMPANY_NAME = 'Company name'
FILTER_FIELDS_MAPPING = {
    GROUP_BY_COMPANY_NAME: 'partner_name'
}
GROUP_BY_CHOICES = [(None, 'Select group by')] + [(c, c) for c in [GROUP_BY_COMPANY_NAME]]
 