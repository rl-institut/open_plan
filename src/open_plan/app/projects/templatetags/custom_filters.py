from math import floor

from django import template

register = template.Library()


@register.filter(name='beautiful_seconds')
def convert_seconds_to_intuitive_string(value):
    try:
        convert = lambda divisor, mod : floor(value / divisor % mod)
        days = convert(86400, 1)
        hours = convert(3600, 24)
        mins = convert(60, 60)
        secs = convert(1, 60)

        return f'{days}d {hours}h {mins}m {secs}s'

    except Exception as e:
        return str(e)

@register.filter(name='scenario_list')
def get_scenario_list_from_project(project):
    return project.scenario_set.all()

@register.filter
def pdb(element):
    import pdb; pdb.set_trace()
    return element

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)