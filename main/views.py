from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406351453',
        'name': 'Rivaldy Putra Rivly',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)