from sre_constants import BRANCH
from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import redirect
import datetime

# Create your views here.


def Login(request):
    
    if request.method == "POST":
        userID = request.POST.get('username')
        password = request.POST.get("password")
        df = pd.read_csv("data\Student.csv")
        
        user = ((df.username == (userID))& (df.Password == password)).any()
        if user :
            open("session.txt",'w').write(userID+'\n'+password)
            return redirect('student-details')
        else:
            open("session.txt",'w').write("")
            return redirect('login')



    return render(request , 'login.html')

def index(request):
    return render(request,'home.html')

def student_details(request):
    with open('session.txt','r') as f:
        cd= f.readlines()
    if cd != "":
        df = pd.read_csv('data\Lend.csv')
        username = cd[0].strip('\n')
        book_name = df[df.Username == username ].Bookname.values
        issued_date = df[df.Username == username ].IssueDate.values
        return_date = df[df.Username == username ].returnDate.values
        context = {
            'username':username,
            'book_list':zip(book_name,issued_date,return_date)
        }
        return render(request,'student_detials.html',context=context)
    return redirect('login')

def lend_book(request):
    df = pd.read_csv("data\Book.csv")
    book_list = df.Title.values
    
    category = df.Category.values
    author = df.Author.values
    
    context = {
        'lists': zip(book_list,category,author)
    }
    return render(request,'lend_book.html',context=context)

def add_book(request,bookname):
    with open('session.txt','r') as f:
        creditals = f.readlines()
    userid = creditals[0].strip('\n')
    df1 = pd.read_csv("data\Book.csv")
    isbn = df1[(df1.Title==bookname )].ISBN.values[0]
    issue_date = datetime.datetime.now().date()
    return_date = issue_date+datetime.timedelta(days=30)
    df = pd.read_csv("data\Lend.csv")
    
    df.loc[len(df)] = [userid,isbn,bookname,return_date,issue_date]
    df.to_csv("data\Lend.csv",index=False)
    return redirect('book_list')
    
def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('mail')
        user_issue = request.POST.get('issue')
        
        context = {
            'flag': True
        }
        return render(request, 'contact.html', context=context)

    else:
        return render(request, 'contact.html')


def info(request):
     with open('session.txt','r') as f:
        creditals = f.readlines()
     if creditals != "":
        df = pd.read_csv('data\Reader.csv')
        username = creditals[0].strip('\n')
        name = df[df.Username == username].Name.values[0]
        father=df[df.Username == username].Father.values[0]
        email = df[df.Username == username].Email.values[0]
        phone = df[df.Username == username].Phone.values[0]
        branch=df[df.Username == username].Branch.values[0]
        college=df[df.Username == username].College.values[0]
        sem=df[df.Username == username].Sem.values[0]
        context = {
            'name':name,
            'father':father,
            'email':email,
            'phone':phone,
            'username':username,
            'branch':branch,
            'college':college,
            'sem':sem,
           
        }
        return render(request,'info.html',context=context)