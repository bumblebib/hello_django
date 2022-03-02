from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1> Hello, {} sua idade é {} :D'.format(nome,idade))

def calculo(request,conta,num1,num2):
    if conta == "soma":
        conta = num1 + num2
        simbolo = ["+","soma"]
    if conta == "sub":
        conta = num1 - num2
        simbolo = ["-","subtração"]
    if conta == "div":
        conta = num1 / num2
        simbolo = ["/","divisão"]
    if conta == "mult":
        conta = num1 * num2
        simbolo = ["*","multiplicação"]

    return HttpResponse('<h1> Hello, a sua {} é {} {} {} = {} </h1>'.format(simbolo[1],num1,simbolo[0], num2, conta))
