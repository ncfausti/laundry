from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from forms import UserProfileForm


# Create your views here.
@login_required
def user_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('loggedin')
	else:
		user = request.user
		profile = user.profile
		form = UserProfileForm(instance=profile)

		args = {}
		args.update(csrf(request))

		args['form'] = form

		return render_to_response('profile.html', args)