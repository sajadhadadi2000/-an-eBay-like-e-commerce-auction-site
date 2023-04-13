from django import forms 

categories = (
        ('E', 'Electronics'),
        ('F', 'Fashion'),
        ('T', 'Toys'),
        ('H', 'Home'),
        ('S', 'Sport'),
        ('O', 'Other'),
    )

class ListForm(forms.Form):
    title = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField( widget=forms.Textarea(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices = categories, widget=forms.Select(attrs={'class': 'form-select'}))
    start_bid = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_image = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control'}))

