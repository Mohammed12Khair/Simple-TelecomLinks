from django.shortcuts import render

from .models import *

# Create your views here.
def default_map(request):
	A=[]
	B=[]
	C=[]
	status=site_map.objects.all()
	info_two=site_links.objects.all().order_by('site_A')
	info=site_map.objects.all().order_by('site_weight')
	for x in status:
		#print(x.site_id)
		links=site_links.objects.filter(site_A=str(x.site_id))
		for y in links:
			siteBxy=site_map.objects.filter(site_id=str(y.site_B)).get()
			A.append(str(x.site_lat) + "," + str(x.site_long))
			B.append(str(siteBxy.site_lat) + "," + str(siteBxy.site_long))
			if str(x.site_status) == "up":
				C.append(str("green"))
			else:
				C.append(str("red"))


	
	for x in range(len(A)):
		print(str(C[x]) + " : " + str(A[x]) + " --> " + str(B[x]))
	max_=len(A)
	d=zip(A,B,C)
	# return render(request,'home.html',{})
	return render(request,'view2.html',{'center':'15.2409,32.499','data':status,'max_':max_,'A':A,'B':B,'C':C,'Z':d,'info':info,'info_two':info_two})