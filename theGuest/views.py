from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import WorksOnLanguage,RecruitDeveloper,RecruitHr,RecruitDeveloperAsProjectManager,AddClientsAndProjectsByMyadmin
from .models import AssignProjectToProjectManagerByMyadmin,AssignProjectToDeveloperByProjectManager
from .models import ActiveAdmin,ReportStatuses,Reports


def index(request):
	return render(request,"theGuest/index.html");

def workprocess(request):
	return render(request,"theGuest/workprocess.html");

def aboutus(request):
	return render(request,"theGuest/aboutus.html");

def contactus(request):
	return render(request,"theGuest/contactus.html");



def ActiveAdminToDeactivates():
	alls=ActiveAdmin.objects.all();
	for data in alls:
		if(data.Status=="Active"):
			data.Status="Deactivate";
			data.save()
def checkOnIt(SearchId,InSearch):
	for data in InSearch:
		if(SearchId==data.id):
			return data;
def loginMethod(request):
	if request.method=="POST":
		haved=str(request.POST["fromwhere"])
		UsernameorEmail=request.POST["txtname"];
		Password=request.POST["txtpassword"]
		if(haved=="MyAdmin"):
			if((UsernameorEmail=="shishu07@gmail.com" or UsernameorEmail=="shishu07") and Password=="shishu07"):
				return redirect("/myadmin");
		elif(haved=="ProjectManager"):
			ActiveAdminToDeactivates();
			pmvalue=RecruitDeveloperAsProjectManager.objects.all();
			devsvalue=RecruitDeveloper.objects.all();
			lst=[];
			ids=[];
			for data in pmvalue:
				lst.append(checkOnIt(int(data.DevsId),devsvalue));
				ids.append([data.id,data.FullName])
			k=-1;
			for data in lst:
				k+=1
				if((UsernameorEmail==data.EmailId or UsernameorEmail==data.UserId) and Password==data.Password):
					values=ActiveAdmin(ProManagerId=ids[k][0],ProManagerName=ids[k][1],Status="Active")
					values.save()
					return render(request,"promanager/index.html",{"activePMID":values.id,"pmName":values.ProManagerName,"pmID":values.ProManagerId});
		return render(request,"theGuest/login.html",{"fromwhere":haved,"passmsg":"_____Invalied Data_____"});
	fromwhere=request.GET["have"]; 
	return render(request,"theGuest/login.html",{"fromwhere":fromwhere});


def logoutMethod(request):
	data=ActiveAdmin.objects.get(pk=int(request.GET["var"]));
	data.Status="Deactivate";
	data.save()
	return redirect("/index/");
