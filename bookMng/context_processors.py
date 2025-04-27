from .models import MainMenu

def navigation_items(request):
    """
    Provides the main navigation menu items (from MainMenu model)
    and makes them available to all templates.
    """

    # Fetch all objects from the MainMenu model (This is so we dont need to keep on calling "main_menu_items = MainMenu.objects.all()"
    main_menu_items = MainMenu.objects.all()

    # Return a dictionary. The key ('item_list') will be the variable name
    # available in your templates. The value is the QuerySet of menu items.
    return {'item_list': main_menu_items}