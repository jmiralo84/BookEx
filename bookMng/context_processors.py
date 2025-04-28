from .models import MainMenu
from django.utils import timezone

def navigation_items(request):
    """
    Provides the main navigation menu items (from MainMenu model)
    and makes them available to all templates.
    """

    # Fetch all objects from the MainMenu model (This is so we don't need to keep on calling "main_menu_items = MainMenu.objects.all()"
    main_menu_items = MainMenu.objects.all()

    # Return a dictionary. The key ('item_list') will be the variable name
    return {'item_list': main_menu_items}

def time_based_greeting(request):
    """
    Adds a time-based greeting to the template context.
    """
    # Default
    greeting = "Hello"
    try:
        # Use Django's timezone utilities
        now = timezone.localtime(timezone.now())
        current_hour = now.hour

        if 5 <= current_hour < 12:
            greeting = "Good morning"
        elif 12 <= current_hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
    except Exception:
        # Log the error if needed
        pass


    # Return a dictionary with the key you want in the template
    return {'greeting': greeting}