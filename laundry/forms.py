from django import forms
from laundry.models import UserProfile

class UserProfileForm(forms.ModelForm):
	states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA","HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
	state = forms.ChoiceField(choices=[x for x in enumerate(states)])

	#country = forms.ChoiceField(choices=[(x, x) for x in enumerate(states)]

	class Meta:
		model = UserProfile
		fields = ('will_pickup','dropoff', 'street_address','city','state','zipcode','country')