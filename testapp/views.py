from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

# from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def index(request):
    return render(request,'mysite/index.html')

'''
Check List
'''

class CreateCheckList(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('title',)
    model = models.CheckList
    # success_url = reverse_lazy('testapp:all')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    # pass

class DeleteCheckList(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.CheckList
    # user = models.User
    select_related = ('user',)
    success_url = reverse_lazy('testapp:all') # ???? i need to pass the user Id

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request,'CheckList Deleted')
        return super().delete(*args,**kwargs)

########################

# def CheckListList(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     return render(request, 'testapp/checklist_list.html', {'user': user})

class CheckListList(SelectRelatedMixin, generic.ListView):
    model = models.CheckList
    select_related = ("user",)

    # models.CheckList.objects.all().filter(user__exact=User.pk)
    #
    # def get_queryset(self):
    #     try:
    #         self.checklist_user = User.objects.prefetch_related("checklist").get(
    #             username__iexact=self.kwargs.get("username")
    #         )
    #     except User.DoesNotExist:
    #         raise Http404
    #     else:
    #         return self.checklist_user.checklist.all()
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["checklist_user"] = self.checklist_user
    #     return context

######################

class CheckListDetail(SelectRelatedMixin, generic.DetailView):
    model = models.CheckList
    select_related = ("user",)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

          # return queryset.filter(user__username__iexact=self.kwargs.get("username"))
        # return queryset.filter(user_id=self.request.user.id)

'''
Check List Items
'''
# https://stackoverflow.com/questions/26797979/django-createview-using-primary-key
# https://stackoverflow.com/questions/44128982/how-to-use-createview-for-the-model-that-has-a-primary-key-from-the-first-model
# this # https://stackoverflow.com/questions/59124344/pass-pk-to-createview-form-in-django
class CreateListItem(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ("title", "message","status")
    exclude = ('check_list',)
    model = models.CheckListItem

    def form_valid(self, form):
        check_list = models.CheckList.objects.get(pk=self.kwargs['check_list_pk'])
        # user = self.request.user.id
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.check_list = check_list
        self.object.save()
        return super().form_valid(form)




class DelteListItem(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.CheckListItem
    # user = models.User
    select_related = ('check_list','user')
    # template_name = 'testapp/task_confirm_delete.html'
    success_url = reverse_lazy('testapp:all') # ???? i need to pass the user Id

    # def get_queryset(self):
    #     # search = models.CheckListItem.objects.filter(pk=self.kwargs['pk'])
    #     queryset = super().get_queryset()
    #     return queryset.filter(user_id=self.request.user.id)
    #     return queryset.filter(id=search)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request,'Task Deleted')
        return super().delete(*args,**kwargs)

class CheckListItemList(SelectRelatedMixin, generic.ListView):
    model = models.CheckListItem
    # select_related = ("title", "message","status")
    select_related = ("check_list",)

class CheckListItemDetail(SelectRelatedMixin, generic.DetailView):
    model = models.CheckListItem
    select_related = ("check_list",)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(
    #         user__username__iexact=self.kwargs.get("username")
    #     )

class UpdateListItem(LoginRequiredMixin, SelectRelatedMixin, generic.UpdateView):
    model = models.CheckListItem
    select_related = ('check_list','user')
    # fields = ("title", "message","status")
    fields = ("status",)
    template_name = 'testapp/update_task.html'




##############################
















# class CreateListSubItem(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
#     pass
#
# class DelteListSubItem(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
#     pass
