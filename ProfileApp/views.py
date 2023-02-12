from django.shortcuts import render, HttpResponse, redirect


#
# def showProduct(request):
#     product = Product()

# Create your views here.
from ProfileApp.forms import ProductForm
from ProfileApp.models import Product


def test(request):
    return HttpResponse("<H1>Hello World <br> This is My World Wide Web </H1>")

def home(request):
    return render(request, 'home.html')

def history(request):
    return render(request, 'history.html')

def firstweb(request):
    return render(request, 'firstweb.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def thirdpage(request):
    return render(request, 'thirdpage.html')

def person(request):
    return render(request, 'person.html')

def product(request):
    return render(request, 'product.html')

def showMyData(request):
    IdNumber = "65342310151-1"
    fullName = "ศุภรักษ์ สะเดา"
    age = 20
    birthday = "02/08/2545"
    sex = 'ชาย'
    bloodType = "เอ"
    like = "เล่นเกม"
    hate = "งานสังสรรค์"
    status = "นักเรียน"
    futurecareer = "นักแคสเตอร์"

    pd1 = ["protien",400.00,'images/pro1.png']
    pd2 = ["protien", 400.00,'images/pro2.png']
    pd3 = ["protien", 400.00,'images/pro3.png']
    pd4 = ["protien", 400.00,'images/pro4.png']
    pd5 = ["protien", 400.00,'images/pro5.png']
    pd6 = ["protien", 400.00,'images/pro6.png']
    pd7 = ["protien", 400.00,'images/pro7.png']
    pd8 = ["protien", 400.51,'images/pro8.png']
    pd9 = ["protien", 400.00,'images/pro9.png']
    pd10 = ["protien", 400.00,'images/pro10.png']
    myproduct = [pd1,pd2,pd3,pd4,pd5,pd6,pd7,pd8,pd9,pd10,]
    mydata = {'IdNumber': IdNumber, 'fullName': fullName, 'age': age, 'birthday': birthday, 'sex': sex,
              'bloodType': bloodType, 'like': like, 'hate': hate, 'status': status, 'futurecareer': futurecareer,
              'myproduct':myproduct}
    return  render(request,'showMyData.html',mydata)

lstOurProduct = []
def listProduct(requset):
    print(lstOurProduct)
    context = {'products':lstOurProduct}
    return render(requset,"listProduct.html",context)
def inputProduct(requset) :
    if requset.method == "POST":
        form = ProductForm(requset.POST)
        if form.is_valid() :
            form = form.cleaned_data
            pdNumber = form.get('pdNumber')
            pdName = form.get('pdName')
            pdPrice = float(form.get('pdPrice'))
            pdProfit = form.get('pdProfit')
            pdAmount = form.get('pdAmount')
            pdVat = form.get('pdVat')
            product= Product(pdNumber,pdName,pdPrice,pdProfit,pdAmount,pdVat)
            lstOurProduct.append(product)
            return redirect('listProduct')

        else:
            form =ProductForm(form)
    else:
        form = ProductForm()
    context = {'form':form,"CHECK":requset.method}
    return render(requset,'inputProduct.html',context)
# def cat_create(request):
#     if request.method == 'POST':
#         from = CategoryForm(request.POST)
#         if from.is_valid():
#             form.save()
#             return redirect('cat_retrieve_all')
#         else:
#             from = CatagoryFrom()
#             context = {
#                 'from':form
#             }
#             return render(request,'category/cat_create.html',context)
# def cat_retrieve_all(request):
#     cat_list = Category.objects.all()
#     return render(request, 'category/ca_retrieve_all.html', {'categories': cat_list})
#
#     def cat_retrieve_one(request, id):
#         context = {}
#
#     context["category"] = Category.objects.get(id=id)
#     return render(request, "category/cat_retrieve_one.html", context)
