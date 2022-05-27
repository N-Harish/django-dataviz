from django import forms

pie_drop = [
    ("Nothing", "Select A Option Below"),
    ("Pie_buc", "Pie Chart Of Bucket"),
    ("Pie_div", "Pie Chart Of Division")
]


class SelectionForm(forms.Form):
    select = forms.ChoiceField(choices=pie_drop, required=True)
    # setting the below att would enable id for select tag
    select.widget.attrs.update({'id': 'sel'})
