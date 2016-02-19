from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from social_todo.forms import NewTaskForm, MyRegistrationForm, LoginForm #,UserForm
from django.contrib.auth import logout, authenticate, login as auth_login
from social_todo.models import Task, User#, Users2 ,UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib import messages


def index(request):
    context = RequestContext(request)

    task_list = Task.objects.all()
    context_dict = {'tasks': task_list}

    return render_to_response('social_todo/index.html', context_dict, context)

def task(request, task_name_url):
    context = RequestContext(request)

    # Change underscores in the category name back to spaces.
    task_name = task_name_url.replace('_', ' ')

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the category passed by the user.
    context_dict = {'task_title': task_title}

    try:
        task = Task.objects.get(title=task_title)
    except Task.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('social_todo/task.html', context_dict, context)

def add_task(request):
    context = RequestContext(request) # Get the context from the request.
    if request.method == 'POST':# A HTTP POST?
        form = NewTaskForm(request.POST)
        if form.is_valid(): # Have we been provided with a valid form?
            form.save(commit=True) # Save the new task to the database.
            print ('task saved')
            return HttpResponseRedirect('/')
        else:
            print ('form errors')
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = NewTaskForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('social_todo/index.html', {'form': form}, context)

def register_user(request):
    context = RequestContext(request)

    if request.method == 'POST':
        request.POST['username'] = request.POST['email']
        request.POST['first_name'] = request.POST['fl_name']
        form = MyRegistrationForm(request.POST)

        if len(request.POST['email']) < 1 or len(request.POST['email']) > 50:
            messages.error(request,'Invalid email address')
            return HttpResponseRedirect('/')
        if len(request.POST['fl_name']) < 1 or len(request.POST['fl_name']) > 50:
            messages.error(request,'Invalid email address')
            return HttpResponseRedirect('/')
        if len(request.POST['password']) < 1 or len(request.POST['password']) > 50:
            messages.error(request,'Invalid password')
            return HttpResponseRedirect('/')

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            auth_login(request, user)
            print ("user registered")
            return HttpResponseRedirect('/')
        else:
             messages.error(request, 'Account with this email already exists!')
             return HttpResponseRedirect('/')

    else:#if not a POST request, then send back the blank form
        form = MyRegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('social_todo/index.html', token)

def login(request):
    context = RequestContext(request)
    # def errorHandler(error):
    #      return render_to_response('social_todo/index.html', {'error' : error})
    if request.method == 'POST': #if the method is POST
        username = request.POST['email'] #Check that email and pw are valid
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        print (user)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                print ('user is active')
                return HttpResponseRedirect('/')
            else:
                # error = 'Account disabled.'
                print ('Account disabled.')
                # return errorHandler(error)
        else:
            messages.error(request, 'Invalid email address')
            print ('user is = None')
    else:
        # error = 'Invalid details entered.'
        # return errorHandler(error)
        print ('invalid details')
    return render_to_response('social_todo/index.html', {}, context)

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

def delete_task(request,task_id):
    context = RequestContext(request)
    """
    Deletes a task from the system. This view is designed to be called by AJAX.
    For the purposes of this demo, we assume it will always work.

    Inputs:
    :request:   django request object
    :task_id:   integer value of the task id

    Returns:
    true
    """
    task = Task.objects.get(id=task_id)
    print(task)
    task.delete()
    # return HttpResponse("true")
    return HttpResponseRedirect('/')

def complete_task(request,task_id):
    context = RequestContext(request)

    task = Task.objects.get(id=task_id)
    print(task)
    if task.isComplete == 1:
        task.isComplete == 0
        print (task.title, "bool changed to 0")
        task.save()
    else:
        task.isComplete == 1
        print ("bool changed to 1")
        task.save()

    return HttpResponseRedirect('/')
