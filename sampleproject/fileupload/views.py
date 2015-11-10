from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.core.urlresolvers import reverse
from models import Document
from django import forms
# Create your views here.

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')


def list(request):
    #File upload part
    if request.method == 'POST':
        #print request.FILES['docfile'].size
        #print request.FILES['docfile'].content_type
        #print
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            #redirect to document list after POST
            #print reverse('sampleproject.fileupload.views.list')
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() #handles empty form
        #load documents for the list page
        documents = Document.objects.all()
        # Render the list page with document and form
        return render(request, 'list.html', {'documents': documents, 'form': form})