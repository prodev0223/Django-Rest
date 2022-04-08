from datetime import datetime

from apps.utils.exceptions import IncorrectDateValueError

 
def validate_date(date_text):
    """
    This function is for validating the date text weather it is valid date or not
    """
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise IncorrectDateValueError(date_text)
