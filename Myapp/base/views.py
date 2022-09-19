
from distutils import config
from email import message
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views import View 
from django.core.mail import send_mail
from django.conf import settings
from .models import product
from bs4 import BeautifulSoup 
import requests
from .forms import AddForm
from .models import product
from django.views.generic import DeleteView
from django.contrib import messages
# Create your views here.
class Home(View):
     def get(self,request):
        return render(request, 'Home.html', {})
      

def contact(request):
   if request.method == 'POST':
      name= request.POST.get('name')
      email=request.POST.get('email')
      subject=request.POST.get('subject')
      message=request.POST.get('message')
          
      message='''
       There is the message: 
          {}

       From: {}
          '''.format(message,name)
      
      send_mail(
      subject,
      message,
      settings.EMAIL_HOST_USER,
      [email],
   
   )
   messages.success(request, "The email sent with succesful")
   return render(request, 'Contact.html', {})











       
def data_view(request):
   no_discount =0
   error=None

   form=AddForm(request.POST or None)

   if request.method== 'POST':
      try:
         if form.is_valid():
            form.save()
      except AttributeError:
         error='ooops.....'
      except:
         error= 'opps wait'
   form =AddForm()
   qs= product.objects.all()
   items_no=qs.count()
   

   if items_no>0:
      discount_list=[]
      for item in qs:
         if item.old_product_price>item.current_price:
            discount_list.append(item)
         no_discount = len(discount_list)
      

   context ={
      'qs':qs,
      'no_discount':no_discount,
      'item_no': items_no,
      'form':form,
      'error': error



   }
   return render(request,'data.html',context)


class DeleteProduct(DeleteView):
   model=product
   template_name='delete_confirmation.html'
   #success_url= reverse_lazy('data')
   success_url= reverse_lazy('data')



def update(request):
   qs=product.objects.all()
   for prod in qs:
      prod.save()
   return redirect("data")