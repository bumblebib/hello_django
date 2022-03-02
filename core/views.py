from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1> Hello, {} sua idade é {} :D'.format(nome,idade))

def calculo(request,conta,num1,num2):
    if conta == "soma":
        conta = num1 + num2
        simbolo = "+"
    if conta == "sub":
        conta = num1 - num2
        simbolo = "-"
    if conta == "div":
        conta = num1 / num2
        simbolo = "/"
    if conta == "mult":
        conta = num1 * num2
        simbolo = "*"

    return HttpResponse('<h1> Hello, a sua soma é {} {} {} = {} </h1>'.format(num1,simbolo, num2, conta))
