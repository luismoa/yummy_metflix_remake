from django import forms


class InsertMovieForm(forms.Form):
    title = forms.CharField(label='Title')
    running_time = forms.IntegerField(label='Running time')
