from navbar.models import nav

def navbar(request):
    nav_bar = nav.objects.all()
    return {"nav_bar":nav_bar}