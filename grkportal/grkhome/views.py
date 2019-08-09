from django.shortcuts import render
from .forms import MemberRegisterForm


def home(request):
    form = MemberRegisterForm(request.POST or None)
    return render(request, 'home.html', {'form': form})

#     return render(request, 'home.html')

# def add_new_member(request):
#     form = MemberRegisterForm()
#     if request.method == 'POST':
#         form = MemberRegisterForm(request.POST)
#         if form.is_valid():
#             applicant_first_name = form.cleaned_data['applicant_first_name']
#             applicant_last_name = form.cleaned_data['applicant_last_name']
#             # All set, now enter Data iin DB
#     return render(request, 'home.html', {'form': form})


def add_new_member(request):
    form = MemberRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'membersaved.html', context)

# def members(request):
#     # return HttpResponse("Hello world")
#     return render(request, 'membersaved.html', {'name': 'members'})
