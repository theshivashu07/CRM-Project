from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),
		#path('ActiveAdmin/',views.ActiveAdminMethod,name='ActiveAdmin'),
		path('AssignProjectToDeveloperByProjectManager/',views.AssignProjectToDeveloperByProjectManagerMethod,name='AssignProjectToDeveloperByProjectManager'),
		path('ShowAllReportsSendByDevs/',views.ShowAllReportsSendByDevsMethod,name='ShowAllReportsSendByDevs'),
		path('SendReportToAdmin/',views.SendReportToAdminMethod,name='SendReportToAdmin'),
		#path('SendReportToAdmin1/',views.SendReportToAdmin1Method,name='SendReportToAdmin1'),
		#path('SendReportToAdmin2/',views.SendReportToAdmin2Method,name='SendReportToAdmin2'),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		
]




