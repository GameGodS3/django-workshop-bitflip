from django import forms

class EventCreator(forms.Form):
    eventtitle = forms.CharField(widget=forms.TextInput(attrs={'class':'formfields make-event-title', 'placeholder': 'Title Name'}))
    eventdesc = forms.CharField(widget=forms.TextInput(attrs={'class':'formfields make-event-desc', 'placeholder': 'Description'}))
