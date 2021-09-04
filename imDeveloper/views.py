from django.shortcuts import render,redirect
from django.http import HttpResponse
from theGuest.models import WorksOnLanguage,RecruitDeveloper,RecruitHr,RecruitDeveloperAsProjectManager,AddClientsAndProjectsByMyadmin
from theGuest.models import AssignProjectToProjectManagerByMyadmin,AssignProjectToDeveloperByProjectManager
from theGuest.models import ActiveAdmin,ReportStatuses,Reports


def index(request):
	return render(request,"imDeveloper/index.html");


def SendReportToPMMethod(request):
	if request.method=="POST":
		ProjectId=(request.POST["txtreporttitle"]);
		ReportById=(request.POST["txtreportbycategory"]);
		ReportToId=(request.POST["txtreporttocategory"]);   #report to but devs id
		isassigned=RecruitDeveloperAsProjectManager.objects.all();
		for i in isassigned:
			if(i.DevsId==ReportToId):
				ReportToId=i.id;							#reports to and now actual promanager id
				break;
		isassigned=AssignProjectToDeveloperByProjectManager.objects.all();
		for i in isassigned:
			if(int(i.ProjectId)==int(ProjectId) and int(i.DevsId)==int(ReportById) and int(i.ProManagerId)==int(ReportToId)): #ProManagerId 
				projectname=AddClientsAndProjectsByMyadmin.objects.get(pk=request.POST["txtreporttitle"]);
				hold=Reports(ReportTitle=projectname.ProjectName,ReportStatus=request.POST["txtreportstatus"],ReportDiscription=request.POST["txtreportdiscription"],ReportDate=request.POST["txtreportdate"],ReportById=request.POST["txtreportbycategory"],ReportToId=ReportToId,DevsId=request.POST["txtreportbycategory"],PMId=ReportToId);
				hold.save()
				return render(request,"imDeveloper/SendReportToPM.html",{"result":"_____Your project "+str(i.ProjectName)+"'s Report Successfully Submitted to proManager '"+str(i.ProManagerName)+"'._____"});
		else:
			return render(request,"imDeveloper/SendReportToPM.html",{"result":"_____Select only Correct Data's_____"});
	ReportS=ReportStatuses.objects.all();
	DevsWhosAssignProjects=AssignProjectToDeveloperByProjectManager.objects.all();
	pmvalue=RecruitDeveloperAsProjectManager.objects.all();
	devsvalue=RecruitDeveloper.objects.all();
	pmvalues=[];
	devswhosnotpm=[]
	for i in devsvalue:
		for j in pmvalue:
			if(int(i.id)==int(j.DevsId)):
				pmvalues.append(i)
				break;
		else:
			devswhosnotpm.append(i)
	return render(request,"imDeveloper/SendReportToPM.html",{"ReportStatus":ReportS,"DWAP":DevsWhosAssignProjects,"PMs":pmvalues,"DevsNotPM":devswhosnotpm});




