from django.db import models





class WorksOnLanguage(models.Model):
	Language = models.CharField(max_length=30);
	def __str__(self):
		return "We Added new Language "+self.Language+".";


class RecruitDeveloper(models.Model): 
	FullName = models.CharField(max_length=20);
	Age = models.CharField(max_length=2);
	MobileNo = models.CharField(max_length=10);
	EmailId = models.CharField(max_length=30);
	WorkExperience = models.CharField(max_length=2);
	Specialization = models.CharField(max_length=25);
	Address = models.CharField(max_length=50);
	UserId = models.CharField(max_length=25);
	Password = models.CharField(max_length=25);
	def __str__(self):
		return "We hiring "+self.FullName+", as Developer.";


class RecruitHr(models.Model): 
	FullName = models.CharField(max_length=20);
	Age = models.CharField(max_length=2);
	MobileNo = models.CharField(max_length=10);
	EmailId = models.CharField(max_length=30);
	WorkExperience = models.CharField(max_length=2);
	Specialization = models.CharField(max_length=25);
	Address = models.CharField(max_length=50);
	UserId = models.CharField(max_length=25);
	Password = models.CharField(max_length=25);
	def __str__(self):
		return "We hiring "+self.FullName+", as HR.";


class RecruitDeveloperAsProjectManager(models.Model): 
	FullName = models.CharField(max_length=20);
	UserId = models.CharField(max_length=20);
	DevsId = models.CharField(max_length=10); 
	def __str__(self):
		return "We promote developer "+self.FullName+", as Project Manager.";


class AddClientsAndProjectsByMyadmin(models.Model):
	ClientsFullName = models.CharField(max_length=20);
	ClientsEmailId = models.CharField(max_length=30);
	ClientsMobileNo = models.CharField(max_length=10);
	ProjectName = models.CharField(max_length=30);
	ProjectLanguage = models.CharField(max_length=30);
	ProjectStartDate = models.CharField(max_length=10);
	ProjectLastDate = models.CharField(max_length=10);
	ProjectBudget = models.CharField(max_length=6);
	ClientsUserId = models.CharField(max_length=25);
	ClientsPassword = models.CharField(max_length=25);
	def __str__(self):
		return "We added "+self.ClientsFullName+", as Client. And Its Project Name is '"+self.ProjectName+"'.";


class AssignProjectToProjectManagerByMyadmin(models.Model):
	ProManagerName = models.CharField(max_length=20); 
	ProjectName = models.CharField(max_length=30);
	DevsId = models.CharField(max_length=10);		#project manager's devs Id
	ProManagerId = models.CharField(max_length=10); 
	ProjectId = models.CharField(max_length=10);
	def __str__(self):
		return "We assigned project '"+self.ProjectName+"', to project manager '"+self.ProManagerName+"'.";


class AssignProjectToDeveloperByProjectManager(models.Model):
	ProManagerName = models.CharField(max_length=20); 
	ProjectName = models.CharField(max_length=30);
	DevsName = models.CharField(max_length=20);
	DevsId = models.CharField(max_length=10);		#actual devs Id who's we assigned
	ProManagerId = models.CharField(max_length=10); 
	ProjectId = models.CharField(max_length=10); 
	def __str__(self):
		return "ProManager '"+self.ProManagerName+"' assigned project '"+self.ProjectName+"', to developer '"+self.DevsName+"'.";


class ActiveAdmin(models.Model):
	ProManagerId= models.CharField(max_length=10); 
	ProManagerName= models.CharField(max_length=20); 
	Status = models.CharField(max_length=10); 
	def __str__(self):
		return "ProManager '"+self.ProManagerName+"' "+self.Status+" now.";


class ReportStatuses(models.Model):
	Status=models.CharField(max_length=15);
	def __str__(self):
		return "We added new status '"+self.Status+"'.";


class Reports(models.Model):
	ReportId = id;
	ReportTitle = models.CharField(max_length=30);
	ReportStatus = models.CharField(max_length=15);
	ReportDiscription = models.CharField(max_length=100);
	ReportDate = models.CharField(max_length=10);
	ReportById =  models.CharField(max_length=20);
	ReportToId = models.CharField(max_length=20);
	DevsId = models.CharField(max_length=10);
	PMId = models.CharField(max_length=10);

