from django.shortcuts import render
from .models import Mymodel
from django.core.mail import send_mail
from django.http import HttpResponse
from datetime import datetime,timedelta


def submit_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile=request.POST.get('mobile')
        email = request.POST.get('email')
        message=request.POST.get('message') 

        last_submission = (
                Mymodel.objects.filter(email=email).order_by("-submitted_at").first()
        )

        if last_submission and datetime.now() - last_submission.submitted_at.replace(
            tzinfo=None
        ) < timedelta(hours=24):

            # Send an email to notify that a submission was already made within 24 hours you will send after 24 hrs.
            send_mail(
                "Enquiry Form Submission",
                f"""
                You have received a new enquiry submission.

                Name: {name}
                Email: {email}
                Mobile: {mobile}
                Message: {message}

                Please respond to the enquiry accordingly.
                """,
                "shaikhfaiz9554@gmail.com",  
                [email],  
                fail_silently=False,
            )
            return HttpResponse(" Once you fill the from you will not allowed to recorrect untill 24hrs.")
        new_entry = Mymodel(name=name,mobile=mobile,email=email,message=message)
        new_entry.save()
        
        return HttpResponse("data added successfully")

    return render(request, 'index.html')
