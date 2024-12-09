from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .utils import get_processes

class ProcessListView(APIView):
    """
    API view to retrieve system processes.
    
    This view handles GET requests and returns the system's process information
    as a JSON response. It uses the `get_processes` utility function to gather
    the necessary data.
    """

    def get(self, request):
        """
        Handles GET requests to fetch system processes.
        
        Fetches the list of processes from the system and returns it as a JSON response.
        
        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A JSON response containing the list of system processes.
        """
        processes = get_processes()
        return Response({"processes": processes})
    

def process_page(request):
    """
    Renders the process list page.This view renders the `process_list.html` template, which contains a table of system processes and a UI forzinteracting with them. The view doesn't involve fetching data but simply serves the page.
    
    Args:
        request (Request): The HTTP request object.

    Returns:
        HttpResponse: A rendered template with the process page.
    """
    return render(request, 'process_list.html')
