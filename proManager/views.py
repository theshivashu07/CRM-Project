from django.shortcuts import render,redirect
from django.http import HttpResponse
from theGuest.models import WorksOnLanguage,RecruitDeveloper,RecruitHr,RecruitDeveloperAsProjectManager,AddClientsAndProjectsByMyadmin
from theGuest.models import AssignProjectToProjectManagerByMyadmin,AssignProjectToDeveloperByProjectManager
from theGuest.models import ActiveAdmin,ReportStatuses,Reports


def index(request):
	data=ActiveAdmin.objects.get(pk=int(request.GET["var"]));
	return render(request,"proManager/index.html",{"activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});





def AssignProjectToDeveloperByProjectManagerMethod(request):
	if request.method=="POST":
		projectid=request.POST["txtprojectcategory"]
		devsid=request.POST["txtdevscategory"]
		hidden=request.POST["txthidden"]
		val=AssignProjectToProjectManagerByMyadmin.objects.all()
		for data in val:
			if(data.ProManagerId==hidden and data.ProjectId==projectid):
				break;
		devs=RecruitDeveloper.objects.get(pk=request.POST["txtdevscategory"]);
		values=AssignProjectToDeveloperByProjectManager(ProManagerName=data.ProManagerName,ProjectName=data.ProjectName,DevsName=devs.FullName,DevsId=devs.id,ProManagerId=data.ProManagerId,ProjectId=data.ProjectId)
		values.save()
		data=ActiveAdmin.objects.get(pk=int(request.POST["var"]));
		return render(request,"promanager/Collections/AssignProjectToDeveloperByProjectManager.html",{"result":"_____ProManager '"+values.ProManagerName+"' assigned project '"+values.ProjectName+"', to developer '"+values.DevsName+"'._____","activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});
	data=ActiveAdmin.objects.get(pk=int(request.GET["var"]));
	pmvalue=RecruitDeveloperAsProjectManager.objects.all();
	devsvalue=RecruitDeveloper.objects.all();
	lst1=[]
	for i in devsvalue:
		for j in pmvalue:
			if(i.id==int(j.DevsId)):
				break;
		else:
			lst1.append(i)
	assignedproPromanager=AssignProjectToDeveloperByProjectManager.objects.all();
	assignedproMyadmin=AssignProjectToProjectManagerByMyadmin.objects.all();
	projectsdetalis=AddClientsAndProjectsByMyadmin.objects.all();
	lst2=[];
	for i in assignedproMyadmin:
		if(i.ProManagerId==data.ProManagerId):
			for j in assignedproPromanager:
				if(i.ProjectId==j.ProjectId):
					break;
			else:
				for k in projectsdetalis:
					if(int(i.ProjectId)==k.id):
						lst2.append(k);				
	return render(request,"promanager/Collections/AssignProjectToDeveloperByProjectManager.html",{"projectvalues":lst2,"devsvalues":lst1,"activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});





def ShowAllReportsSendByDevsMethod(request):
	if request.method=="POST":
		pass
	data=ActiveAdmin.objects.get(pk=int(request.GET["var"]));
	reports=Reports.objects.all();
	lst=[]
	for i in reports:
		if(i.ReportToId==data.ProManagerId):
			ReportByName=RecruitDeveloper.objects.get(pk=i.ReportById)
			ReportByName=ReportByName.FullName;
			lst.append({"ReportTitle":i.ReportTitle,"ReportStatus":i.ReportStatus,"ReportDiscription":i.ReportDiscription,"ReportDate":i.ReportDate,"ReportBy":ReportByName});
	return render(request,"promanager/Collections/ShowAllReportsSendByDevs.html",{"result":lst,"activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});






def SendReportToAdminMethod(request):
	data=ActiveAdmin.objects.get(pk=int(request.GET["var1"]));
	have=request.GET["var2"];
	if(have=="Nothing"):
		reports=Reports.objects.all();
		lst=[]
		for i in reports:
			if(i.ReportToId==data.ProManagerId):
				ReportByName=RecruitDeveloper.objects.get(pk=i.ReportById)
				ReportByName=ReportByName.FullName;
				lst.append({"ReportsID":str(i.id),"ReportTitle":i.ReportTitle,"ReportStatus":i.ReportStatus,"ReportDiscription":i.ReportDiscription,"ReportDate":i.ReportDate,"ReportBy":ReportByName});
		return render(request,"promanager/Collections/SendReportToAdmin.html",{"result":lst,"activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});
	else:
		lock=Reports.objects.get(pk=request.GET["var2"]);
		lock.ReportById=lock.ReportToId;
		lock.ReportToId="Admin";
		lock.save()
		reports=Reports.objects.all();
		lst=[]
		for i in reports:
			if(i.ReportToId==data.ProManagerId):
				ReportByName=RecruitDeveloper.objects.get(pk=i.ReportById)
				ReportByName=ReportByName.FullName;
				lst.append({"ReportsID":str(i.id),"ReportTitle":i.ReportTitle,"ReportStatus":i.ReportStatus,"ReportDiscription":i.ReportDiscription,"ReportDate":i.ReportDate,"ReportBy":ReportByName});	
		return render(request,"promanager/Collections/SendReportToAdmin.html",{"message":"_____Your Report is Successfully Submitted_____","result":lst,"activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});
	









'''

def SendReportToAdminMethod(request):
	data=ActiveAdmin.objects.get(pk=int(request.GET["var1"]));
	have=request.GET["var2"];
	if(have=="Nothing"):
		reports=Reports.objects.all();
		lst=[]
		for i in reports:
			if(int(i.ReportToId)==int(data.ProManagerId)):
				ReportByName=RecruitDeveloper.objects.get(pk=i.ReportById)
				ReportByName=ReportByName.FullName;
				lst.append({"ReportsID":str(i.id),"ReportTitle":i.ReportTitle,"ReportStatus":i.ReportStatus,"ReportDiscription":i.ReportDiscription,"ReportDate":i.ReportDate,"ReportBy":ReportByName});
		return render(request,"promanager/Collections/SendReportToAdmin.html",{"result":lst,"activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});
	else:
		lock=Reports.objects.get(pk=request.GET["var2"]);
		lock.ReportById=lock.ReportToId;
		lock.ReportToId="Admin";
		lock.save()
		return render(request,"promanager/Collections/SendReportToAdmin.html",{"result":"_____Your Report is Successfully Submitted_____","activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});
	





def SendReportToAdmin1Method(request):
	data=ActiveAdmin.objects.get(pk=int(request.GET["var"]));
	reports=Reports.objects.all();
	lst=[]
	for i in reports:
		if(int(i.ReportToId)==int(data.ProManagerId)):
			ReportByName=RecruitDeveloper.objects.get(pk=i.ReportById)
			ReportByName=ReportByName.FullName;
			lst.append({"ReportsID":str(i.id),"ReportTitle":i.ReportTitle,"ReportStatus":i.ReportStatus,"ReportDiscription":i.ReportDiscription,"ReportDate":i.ReportDate,"ReportBy":ReportByName});
	return render(request,"promanager/Collections/SendReportToAdmin.html",{"result":lst,"activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});


def SendReportToAdmin2Method(request):
		data=ActiveAdmin.objects.get(pk=request.POST["var1"]);
		lock=Reports.objects.get(pk=request.POST["var2"]);
		#return render(request,"promanager/Collections/SendReportToAdmin.html",{"result":str(data)+"--"+str(lock),"activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});
		lock.ReportById=lock.ReportToId;
		lock.ReportToId="Admin";
		lock.save()
		return render(request,"promanager/Collections/SendReportToAdmin.html",{"result":lst,"activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});



'''





















  #<td><center><a href="/myadmin/deletes/?var1={{data.id}}&var2=AllDeveloper" style="color:red">SEND REPORT's TO ADMIN</a></center></td>
                

'''
		projectmains=RecruitDeveloperAsProjectManager.objects.get(pk=request.POST["txtprojectcategory"]);
		devsall
		#return render(request,"promanager/Collections/AssignProjectToDeveloperByProjectManager.html",{"result":str(projectid)+" - "+str(devsid)});
		assignprotopm=AssignProjectToProjectManagerByMyadmin.objects.all();
		for i in assignprotopm:
			if(int(i.DevsId)==devsid):
				data=i;
				break;
		datas=RecruitDeveloper.objects.get(pk=request.POST["txthidden"]);
		values=AssignProjectToProjectManagerByMyadmin(ProManagerName=data.FullName,ProjectName=data.ProjectName,DevsName=datas.FullName,DevsId=data.DevsId,ProManagerId=data.id,ProjectId=data.id)
		values.save()
		data=ActiveAdmin.objects.get(pk=request.POST["txtactivePMID"]);
		return render(request,"promanager/Collections/AssignProjectToDeveloperByProjectManager.html",{"result":"ProManager '"+values.ProManagerName+"' assigned project '"+values.ProjectName+"', to developer '"+values.DevsName+"'.","activePMID":data.id,"pmName":data.ProManagerName,"pmID":data.ProManagerId});
'''


'''
def AssignProjectToProjectManagerByMyadminMethod(request):
	if request.method=="POST":
		projectid=int(request.POST["txtprojectcategory"])
		pmid=int(request.POST["txtpmcategory"])
		projectvalue=AddClientsAndProjectsByMyadmin.objects.all();
		pmvalue=RecruitDeveloperAsProjectManager.objects.all();
		myData=[FindData0(projectid,projectvalue,1),FindData0(pmid,pmvalue,1)];
		values=AssignProjectToProjectManagerByMyadmin(ProManagerName=myData[1].FullName,ProjectName=myData[0].ProjectName,DevsId=myData[1].DevsId,ProManagerId=myData[1].id,ProjectId=myData[0].id)
		values.save()
		return render(request,"myAdmin/Collections/AssignProjectToProjectManagerByMyadmin.html",{"result":"_____We assigned project '"+myData[0].ProjectName+"', to project manager '"+myData[1].FullName+"'._____","more":[]});
	assignproject=AssignProjectToProjectManagerByMyadmin.objects.all();
	allprojects=AddClientsAndProjectsByMyadmin.objects.all();
	pmvalue=RecruitDeveloperAsProjectManager.objects.all();
	projectvalue=[];
	for data in allprojects:
		if(checkOnIt(data.id,assignproject,"showDevelopers")):
			projectvalue.append(data)
	return render(request,"myAdmin/Collections/AssignProjectToProjectManagerByMyadmin.html",{"projectvalues":projectvalue,"pmvalues":pmvalue});
'''



'''for i in assignedproMyadmin:
		if(int(i.ProManagerId)==int(data.ProManagerId)):
			lst2.append(i);'''

