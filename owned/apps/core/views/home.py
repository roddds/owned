from annoying.decorators import render_to
from book.models import Paragraph


@render_to('base.html')
def home(request):
    p = Paragraph.objects.get(pk=1)
    return {'content': p.text}