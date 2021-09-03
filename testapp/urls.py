from django.urls import path, re_path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('all/',views.CheckListList.as_view(),name='all'),
    # path('all/<int:user_id>/',views.CheckListList,name='all'),
    # path('all/<int:user_id>/',views.CheckListList.as_view(),name='all'),

    # path('',views.CheckListList.as_view(),name='all'),
    path('create/',views.CreateCheckList.as_view(),name='create'),

    # re_path(r"delete/(?P<pk>\d+)/$",views.DeleteCheckList.as_view(),name="delete"),
    path('delete/<int:pk>/',views.DeleteCheckList.as_view(), name='delete'),

    # re_path(r"by/(?P<username>[-\w]+)/$",views.CheckListList.as_view(),name="all"),
    # path("by/<username>/",views.CheckListList.as_view(),name="all"),

    ##########
    path('details/<int:pk>/',views.CheckListDetail.as_view(),name='details'),
    # path('checklistcontent/',views.CheckListItemList.as_view(),name='checklistcontent'),
    # path('checklistcontent/<int:pk>/',views.CheckListItemDetail.as_view(),name='checklistcontent'),
    path('addTask/<int:check_list_pk>/',views.CreateListItem.as_view(),name='createitem'),
    path('updatetask/<int:pk>/',views.UpdateListItem.as_view(), name='updatetask'),
    path('deletetask/<int:pk>/',views.DelteListItem.as_view(), name='deletetask'),
]
