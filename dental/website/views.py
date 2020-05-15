from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    context = {}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        message_name  = request.POST['message-name']
        message_email = request.POST['message-email']
        message       = request.POST['message']

        send_mail(
            'message_name',          #subject
            'message',               #message
            'message_email',          #from_email
            ['nimayonten@gmail.com'] #receiever
        )
        context = {
            'message_name': message_name,

        }
        return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html', context)



def about(request):
    context = {}
    return render(request, 'about.html', context)



def pricing(request):
    context = {}
    return render(request, 'pricing.html', context)

    
def service(request):
    context = {}
    return render(request, 'service.html', context)



def appointment(request):
    if request.method == 'POST':
        your_name     = request.POST['your-name']
        your_phone    = request.POST['your-phone']
        your_email    = request.POST['your-email']
        your_address  = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date     = request.POST['your-date']
        your_message  = request.POST['your-message']


        appointment = "Name: " + your_name + "Your Phone: " + your_phone + "Email: " + your_email + "Addess: " + your_address + "Schedule: " + your_schedule + "Date: " + your_date + "Your Message: " + your_message
        send_mail(
            'Appointment Request',   #subject
            appointment,             #appointment
            your_email,              #message
            ['nimayonten@gmail.com'] #receiever
        )

        context = {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message
        }
        return render(request, 'appointment.html', context)
    else:
        return render(request, 'home.html', context)