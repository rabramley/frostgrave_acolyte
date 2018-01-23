"""Acolyte utility functions"""

from werkzeug.routing import BaseConverter

class ListConverter(BaseConverter):
    """Utility class to encode and decode a object IDs
    into a list comma-separated list string
    """

    def to_python(self, value):
        """Convert string comma-separated list to python list 
        
        Arguments:
            value {str} -- Comma-separated string of IDs
        
        Returns:
            list -- List of IDs
        """

        return value.split(',')

    def to_url(self, values):
        """Convert python list of IDs to a string containing
        a comma-separated list
        
        Arguments:
            values {list} -- List of object IDs

        Returns:
            str -- Comma-separated string of IDs
        """

        return ','.join(super(ListConverter, self).to_url(value)
                        for value in values)
