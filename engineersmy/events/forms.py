from django import forms

from core.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'venue', 'link', 'date', 'start_time', 'end_time', 'is_free']
        widgets = {
            'date': forms.SelectDateWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in ['name', 'venue', 'link', 'start_time', 'end_time']:
            self.fields[i].widget.attrs.update({'class': 'uk-input'})
        self.fields['description'].widget.attrs.update({'class': 'uk-textarea'})
        self.fields['is_free'].widget.attrs.update({'class': 'uk-checkbox'})
        self.fields['date'].widget.attrs.update({'class': 'uk-select'})
        print(dir(self.fields['date'].widget))