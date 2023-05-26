import os
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .utils import get_config
from .forms import ConfigForm
from django.contrib import messages

def dashboard(request):
    config = get_config()
    return render(request, 'dashboard.html', {'config': config})

def config(request):
    config = get_config()
    config_path = os.path.join(settings.BASE_DIR, 'psych', 'config.json')
    
    if request.method == 'POST':
        form = ConfigForm(request.POST, site_themes=get_config().get('siteThemes', []))
        if form.is_valid():
            config_data = form.cleaned_data
            config_data['siteThemes'] = get_config().get('siteThemes', [])
            with open(config_path, 'w') as file:
                json.dump(config_data, file)
            return redirect('config')

    else:
        with open(config_path) as file:
            config_data = json.load(file)
        form = ConfigForm(initial=config_data, site_themes=get_config().get('siteThemes', []))
    
    return render(request, 'config.html', {'form': form, 'config': config})
