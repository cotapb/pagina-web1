from django.shortcuts import render, HttpResponse
from .models import Covid

def index(request):
    context = {'hola':['cota','nana']
                }
    return render(request, 'index.html', context)

#pregunta= diag1
def pregunta(request):
    return render(request, 'pregunta.html')
    
            
def informacion(request):
     return render(request, 'informacion.html')

#estadistica resultado bien
def estadistica(request):
    if request.method == 'POST':
        contacto = request.POST.get('contacto', '')
        edad = request.POST.get('edad', '')
        sexo = request.POST.get('sexo', '')
        region = request.POST.get('region', '')
        total = request.POST.get('total', '')

        nuevo_resultado = Resultado()
        nuevo_resultado.contacto = contacto
        nuevo_resultado.edad = edad
        nuevo_resultado.sexo = sexo
        nuevo_resultado.region = region
        nuevo_resultado.total = total
        nuevo_resultado.save()

        return render(request, 'estadistica.html')
    else:
        sexo = request.GET.get('sexo','')
        edad = request.GET.get('edad', '')
        region = request.GET.get('region', '')
        contacto = request.GET.get('contacto', '')
        fiebre = request.GET.get('Fiebre', '')
        tos = request.GET.get('Tos seca', '')
        debilidad = request.GET.get('Debilidad y fatiga','')
        expectoracion = request.GET.get('Expectoracion', '')
        dismea = request.GET.get('Dismea', '')
        dolor = request.GET.get('Dolor de garganta', '')
        cefalea = request.GET.get('Cefalea', '')
        mialgia = request.GET.get('Mialgia o artralgia', '')
        escalofrios = request.GET.get('Escalofrios', '')
        nausea = request.GET.get('Nauseas o vomitos', '')
        congestion = request.GET.get('Congestion nasal', '')
        diarrea = request.GET.get('Diarrea', '')
        homoptisis = request.GET.get('Homoptisis', '')
        conjuntival = request.GET.get('Conjustion conjustival', '')
        total = int(fiebre) + int(tos) + int(debilidad) + int(expectoracion) + int(dismea) + int(cefalea) + int(mialgia) + int(dolor) + int(escalofrios) + int(nausea) + int(congestion) + int(diarrea) + int(homoptisis) + int(conjuntival)

        lista_sintomas = sintoma.objects.all()
        context = { 'edad': edad,
                    'sexo':sexo,
                    'contacto':contacto,
                    'total': total}
        return render(request, 'estadistica.html', context)

#diag 3
def preguntas(request):
    sexo= request.GET.get('sexo','')
    edad= request.GET.get('edad','')
    region= request.GET.get('region','')
    contacto= request.GET.get('contacto','')
    lista_sintomas= Sintoma.objects.all()

    context ={"edad": edad,
              "sexo": sexo,
              "region": region,
              "contacto": contacto,
              "numero_sintomas": len(lista_sintomas),
              "sintomas": lista_sintomas}
    return render(request, 'preguntas.html', context)

#diag2
def pregunta1(request):
    sexo= request.GET.get('sexo','')
    edad= request.GET.get('edad','')
    region= request.GET.get('region','')

    context ={"edad":edad,
              "sexo":sexo,
              "region":region}
    return render(request, 'pregunta1.html', context)





    
