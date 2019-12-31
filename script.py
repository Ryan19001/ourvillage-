from blog.models import Quest2Check
from blog.forms import CheckIfFromForm
from django.forms import modelformset_factory
ob = Quest2Check.objects.all()
Quest = modelformset_factory(Quest2Check, fields=('answer',), form=CheckIfFromForm('hshwsj'))
for form in Quest():
    print(form.as_p())
