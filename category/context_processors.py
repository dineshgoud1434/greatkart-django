from .models import Category


def menu_links(request0):
    links = Category.objects.all()
    return dict(links=links)