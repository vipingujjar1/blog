from django.shortcuts import render,redirect
from .models import Post,Comment
from.forms import Signup
from django.views.generic import DetailView
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect
from.forms import CommentForm,Createuser,Updateuser
#from .forms import CommentForm



# Create your views here.blog_posts
#for list


def post_list(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')

    try:
        post_list=paginator.page(page_number)

    except PageNotAnInteger:
        post_list=paginator.page(1)

    except EmptyPage:
        post_list=paginator.page(paginator.num_page)

    return render(request,'blogapp/post_list.html',{'post_list':post_list})
# class view for detail view
class detail_view(DetailView):
    model=Post
    template_name='blogapp/detail.html'


    def get_context_data(self,**kwargs):

        context=super(detail_view,self).get_context_data(**kwargs)
        context['form']=CommentForm
        context['comments']=Comment.objects.filter(post=self.get_object())
        return context

    def post(self,request,*args,**kwargs):
        form=CommentForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.post = self.get_object()
            instance.user = request.user
            instance.save()
            redir_url="/detail/{}".format(self.get_object().id)
            return redirect(redir_url)


def logout_page(request):
    return render(request,'blogapp/logout.html')

def signup_page(request):
    form=Signup()
    if request.method=='POST':
        form=Signup(request.POST)
        if form.is_valid():
            form.save()
            user=form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'blogapp/signup.html',{'form':form})


def update_view(request,pk):
    update = Post.objects.get(id=pk)
    if request.method == 'POST':
        print('ok')
        form = Updateuser(request.POST, instance=update)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'blogapp/update.html',{'update':update})

def create_view(request):
    form=Createuser()
    if request.method == 'POST':
        form = Createuser(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            return redirect('/')
    return render(request ,'blogapp/create.html',{'form':form})

def delete_view(request,pk):
    delete=Post.objects.get(id=pk).delete()
    return redirect('/')

def dashboard(request):
    login_user=request.user
    posts=Post.objects.filter(author=login_user)
    return render(request,'blogapp/dashboard.html',{'posts':posts})
