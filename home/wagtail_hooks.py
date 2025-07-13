from wagtail import hooks
from django.utils.html import format_html


@hooks.register('insert_global_admin_css')
def custom_admin_css():
    return format_html('<link rel="stylesheet" href="/static/css/admin-custom.css">')
