from django import template

register = template.Library()


@register.simple_tag
def dg_item(imgurl, data, title, cost):
    for i, d, t, c in zip(imgurl, data, title, cost):
        im_da_ti_co = [i, d, t, c]
        del imgurl[0]
        del data[0]
        del title[0]
        del cost[0]
        return im_da_ti_co


@register.simple_tag
def h_item(imgurl, data, title, cost):
    for i, d, t, c in zip(imgurl, data, title, cost):
        im_da_ti_co = [i, d, t, c]
        del imgurl[0]
        del data[0]
        del title[0]
        del cost[0]
        return im_da_ti_co


@register.simple_tag
def s_item(imgurl, data, title, cost):
    for i, d, t, c in zip(imgurl, data, title, cost):
        im_da_ti_co = [i, d, t, c]
        del imgurl[0]
        del data[0]
        del title[0]
        del cost[0]
        return im_da_ti_co
