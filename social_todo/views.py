from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from social_todo.forms import UserForm, NewTaskForm, MyRegistrationForm
from django.contrib.auth import logout, authenticate, login
from social_todo.models import Tasks, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth


def index(request):
    # # Request the context of the request.
    # # The context contains information such as the client's machine details, for example.
    # context = RequestContext(request)
    #
    # # Query the database for a list of ALL categories currently stored.
    # # Order the categories by no. likes in descending order.
    # # Retrieve the top 5 only - or all if less than 5.
    # # Place the list in our context_dict dictionary which will be passed to the template engine.
    # task_list = Tasks.objects.all()
    # context_dict = {'tasks': task_list}
    #
    # # We loop through each category returned, and create a URL attribute.
    # # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    # for task in task_list:
    #     task.url = task.title.replace(' ', '_')

    # Render the response and send it back!
    return render(request, 'social_todo/index.html')#, context_dict, context)


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
        task = Tasks.objects.get(title=task_title)

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
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/social_todo/')
    else:
        form = MyRegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('social_todo/register_user.html', token)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/social_todo/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Neat account is disabled SUCKA.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('social_todo/login.html', {}, context)

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/social_todo/')
