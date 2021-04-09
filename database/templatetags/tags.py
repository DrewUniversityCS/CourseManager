from django import template
from django.template.defaultfilters import stringfilter

from database.models.schedule_models import Course

register = template.Library()


@register.filter
@stringfilter
def parse_var(value):
    value = value.replace('_', ' ')
    value = value.capitalize()
    return value


@register.filter
@stringfilter
def obj_to_dynamic_model_name(value):
    if value == 'database | course':
        return 'courses'
    elif value == 'database | student':
        return 'students'
    elif value == 'database | preference':
        return 'preferences'
    return value



@register.simple_tag()
def get_course_stats(form):
    stats_list = []
    courses = Course.objects.filter(sets__set=form.course_set)
    for course in courses:
        stats_list.append({
            'course': course,
            'count': form.entries.filter(courses=course).count()
        })

    return stats_list


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)