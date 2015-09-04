from django import template
from endless_pagination import settings
from endless_pagination.templatetags.endless import show_more

register = template.Library()

@register.inclusion_tag('students/show_more_table.html', takes_context=True)
def show_more_table(context, label=None, loading=settings.LOADING):

    """Show the link to get the next page in a Twitter-like pagination in a
    template for table.

    Usage::

        {% show_more_table %}

    Alternatively you can override the label passed to the default template::

        {% show_more_table "even more" %}

    You can override the loading text too::

        {% show_more_table "even more" "working" %}

    Must be called after ``{% paginate objects %}``.
    """
    # This template tag could raise a PaginationError: you have to call
    # *paginate* or *lazy_paginate* before including the showmore template.
    return show_more(context, label, loading)
