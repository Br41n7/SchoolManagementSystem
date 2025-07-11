from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
# from weasyprint.fonts import FontConfiguration

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    # font_config = FontConfiguration()
    pdf = HTML(string=html).write_pdf(font_config=font_config)

    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    return None
