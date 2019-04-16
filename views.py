##Views.py File
def signup(request):
    if request.method=='POST':
        username=request.POST.get('use','')
        email=request.POST.get('em','')
        password=request.POST.get('pass',)

        user=Signup(username=username,email=email,password=password)
        user.save()
        if user:
            return redirect('/shop')
    return render(request,'shop/signup.html')

def authenticate(username,password):
    print(password)
    print("hello")
    with connection.cursor() as cursor:
        try:
            print("helllo2")
            cursor.execute("SELECT * FROM Signup WHERE username='{}'".format(username))
            for row in cursor.fetchall():
                a=list(row)
            print(a[2])
            pwd=a[2]
            print(row,)
        except:
            pwd=0
            pass


    if pwd==password:

         print("verified")

         return True
    return False
def login(request):

    if request.method=='POST':
        username=request.POST.get('use','')
        password=request.POST.get('pass','')
        print(username)
        print(password)
        if authenticate(username,password):
            return redirect('/shop')

    return render(request,'shop/login.html')
