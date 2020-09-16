from django.forms import ModelForm, DateTimeInput
from .models import Listen

class DateTimeInput(DateTimeInput):
    input_type = 'datetime-local'

class ListenForm(ModelForm):
    class Meta:
        model = Listen
        fields = ['date', 'method']
        widgets = {'date': DateTimeInput()}

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['date'].widget.attrs.update({'type': 'datetime-local'})
