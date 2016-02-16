from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from social_todo.forms import NewTaskForm, MyRegistrationForm, LoginForm #,UserForm
from django.contrib.auth import logout, authenticate, login
from social_todo.models import Task, User#, Users2 ,UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    task_list = Task.objects.all()
    context_dict = {'task': task_list}

    # We loop through each category returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    for task in task_list:
        task.url = task.title.replace(' ', '_')

    #Render the response and send it back!
    form = MyRegistrationForm()
    context['form'] = form
    return render(request, 'social_todo/index.html', context)


def task(request, task_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    # Change underscores in the category name back to spaces.
    task_name = task_name_url.replace('_', ' ')

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the category passed by the user.
    context_dict = {'task_title': task_title}

    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        task = Task.objects.get(title=task_title)

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        # pages = Page.objects.filter(category=category)
        #
        # # Adds our results list to the template context under name pages.
        # context_dict['pages'] = pages
        # # We also add the category object from the database to the context dictionary.
        # # We'll use this in the template to verify that the category exists.
        # context_dict['category'] = category
    except Task.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('social_todo/task.html', context_dict, context)

def add_task(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = NewTaskForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('social_todo/add_task.html', {'form': form}, context)

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form populated with data
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/social_todo/')
    else:#if not a POST request, then send back the blank form
        form = MyRegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('social_todo/register_user.html', token)

# def login(request):
#     context = RequestContext(request) #obtain context for user request
#     if request.method == 'POST':
#         #see if email and pw are valid
#         form = loginForm(request.POST)
#         user = request.POST['username'] # Gather the username and pw from login form
#         password = request.POST['password']
#         user = authenticate(user=user, password=password)
#         print (user)
#         print (password)
#         if user is not None: # Is the account active? It could have been disabled.
#             if user.is_active:
#                 print("User is valid, active and authenticated")
#                 # If the account is valid and active, we can log the user in.
#                 # We'll send the user back to the homepage.
#                 login(request, user)
#                 return HttpResponseRedirect('/social_todo/')
#             else:
#                 # An inactive account was used - no logging in!
#                 return HttpResponse("Your Neat account is disabled SUCKA.")
#         else:
#             # Bad login details were provided. So we can't log the user in.
#             print ("Invalid login details: {0}, {1}".format(user, password))
#             return HttpResponseRedirect('/social_todo/')
#
#     else:# This scenario would most likely be a HTTP GET, so display form
#         form = loginForm(request.POST)
#         token = {}
#         token.update(csrf(request))
#         token['form'] = form
#         return render_to_response('social_todo/login.html', token)

def login(request):
    context = RequestContext(request)
    # def errorHandler(error):
    #      return render_to_response('social_todo/index.html', {'error' : error})
    if request.method == 'POST': #if the method is POST
        username = request.POST['username']
        password = request.POST['password'] #Check that username and pw are valid
        user = authenticate(username = username, password = password)
        print (user)
        if user:
            if user.is_active:
                login(request, user)
                print ('user is active')
                return HttpResponseRedirect('social_todo/index.html')
            else:
                # error = 'Account disabled.'
                print ('Account disabled.')
                # return errorHandler(error)
        else:
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
    return HttpResponseRedirect('/social_todo/')
