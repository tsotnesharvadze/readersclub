from django.shortcuts import render #, redirect, get_object_or_404 ,render_to_response
# from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import get_language

from .forms import BookModelForm 
# from .models import ProjectModel, ProblemModel,Comment,CommentAnswerModel,FileModel

# from registration.models import Account
# from .helpers import get_index, slug_to_id,send_email

def index(request):
	form = BookModelForm()
	return render(request ,'sacdeli.html' ,{'form':form})
