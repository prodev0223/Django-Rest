class RouteDetailNotFoundError(Exception):
    """Raised when the route detail in not present in the defined constant"""

    def __init__(self, route_name, message='Route detail not available', ):
        self.route_name = route_name
        self.message = message
        super().__init__(self.message)

 
class RouteDetailNotDefinedProperlyError(Exception):
    """Raised when the route detail does not contain all the required fields"""

    def __init__(self, route_name, message='Some of the fields are missing', ):
        self.route_name = route_name
        self.message = message
        super().__init__(self.message)


class InSufficientDataProvidedError(Exception):
    """Raised when there isn't sufficient data provided while constructing the payload """

    def __init__(self, variable_name, message='Some of the fields are missing', ):
        self.variable_name = variable_name
        self.message = message
        super().__init__(self.message)


class PayloadConstructionNotImplementedError(Exception):
    """Raised when payload construction logic is not implemented for given route """

    def __init__(self, route_name, message=None):
        self.route_name = route_name
        self.message = message or f'Payload construction not implemented for {route_name}'
        super().__init__(self.message)

class IncorrectDateValueError(Exception):
    """Raised when given date text is not a valid date """

    def __init__(self, date_text, message=None):
        self.date_text = date_text
        self.message = message or f'{date_text} is in incorrect date format, should be YYYY-MM-DD'
        super().__init__(self.message)
