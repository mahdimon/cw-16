from core.http import render_template
from app.models import custom_register

def login(request):
    context={'title':'welcome to the DevConnector',
             'sign':'Sign In',
             'text':'Sign into your account',
             'text2':'Dont have an account ?'
    }
    return render_template('login.html', context)

def post(request):
    context = {
        'title': 'Welcome To The Developer Connector',
        'main_post': {
            'avatar_url': 'image',
            'author': 'name',
            'content': 'Lorem'
        },
        'comments': [
            {
                'avatar_url': 'image',
                'author': 'name',
                'content': 'Lorem'
            }
        ]
    }
    return render_template('post.html', context)

def posts(request):
    context = {
        'title': 'Welcome To The Developer Connector',
        'comments': [
            {
                'avatar_url': 'image',
                'author': 'name',
                'content': 'Lorem'
            }
        ]
    }
    return render_template('posts.html', context)

def register(request):
    data = request.POST

    if request.command=='POST' and custom_register(data):
        posts(request)
    
    elif request.command=='GET':
        context = {
            'title': 'Welcome To The Developer Connector',
            'header' : 'Sign Up',
            'paragrapgh':'Create Your Account',
            'paragraph2':'Already have an account?'

        }
        return render_template('register.html', context)


# def index(request):
#     context = {'title': 'Welcome to the DevConnector',
#                'heading': 'Developer Connector',
#                'description': 'Create developer profile/portfolio, share posts and get help from other developers'
#                }
#     return render_template('index.html', context)

# def add_education(request):
#     context={'title':'welcome to the DevConnector',
#              'text_header':'Add Your Education',
#              'description':' Add any school, bootcamp, etc that you have attended',
#              'date1':'From Date',
#              'date2':'To Date',
#              'paragraph': 'Current School'
#     }
#     return render_template('add-education.html', context)

# def add_experience(request):
#     context={'title':'welcome to the DevConnector',
#              'text_header':'Add An Experience',
#              'description':' Add any developer/programming positions that you have had in the past',
#              'date1':'From Date',
#              'date2':'To Date',
#              'paragraph': 'Current job'
#     }
#     return render_template('add-experience.html', context)

# def create_profile(request):
#     context={'title':'welcome to the DevConnector',
#              'text_header':'Create Your Profile',
#              'description': "Let's get some information to make your profile stand out",
#     }
#     return render_template('create-profile.html', context)

# def dashboard(request):
    
#     context = {
#         'title': 'Dashboard - DevConnector',
#         'dashboard_title': 'Dashboard',
#         'user_name': 'John Doe',
#         'experiences': [
#             {'company': 'Microsoft', 'title': 'Senior Developer', 'years': 'Oct 2011 - Current'},
#             {'company': 'Sun Microsystems', 'title': 'Senior Developer', 'years': 'Oct 2004 - Nov 2010'}
#         ],
#         'educations': [
#             {'school': 'University of Washington', 'degree': 'Masters', 'years': 'Sep 1993 - June 1999'}
#         ]
#     }
#     return render_template('dashboard.html', context)