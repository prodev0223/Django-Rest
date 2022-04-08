from .constants import *
from ..utils.exceptions import RouteDetailNotFoundError, RouteDetailNotDefinedProperlyError

REQUIRED_FIELDS_IN_ROUTE_DETAIL = ['api_url', 'headers']


# We need to keep details about the routes in this constant
API_ROUTES_DETAIL = {
    'invoice_list_api': {
        'api_url': API_BASE_URL + '/api/get_invoice_list/',
        'headers': {
            'Content-Type': 'application/json',
        }
    }
}
 

def get_route_detail_for(route_name):
    """

    This method return the route detail for given route name
    raises RouteDetailNotFoundError if given route name if not defined in the constant
    raises RouteDetailNotDefinedProperlyError if all the required parameters are not defined for given route name

    """
    if route_name not in API_ROUTES_DETAIL:
        raise RouteDetailNotFoundError(route_name, message=f'{route_name} not found in route detail')
    for required_fields in REQUIRED_FIELDS_IN_ROUTE_DETAIL:
        if required_fields not in API_ROUTES_DETAIL.get(route_name):
            raise RouteDetailNotDefinedProperlyError(route_name,
                                                     message=f'{required_fields} not found in {route_name} route detail')
    return API_ROUTES_DETAIL.get(route_name)
