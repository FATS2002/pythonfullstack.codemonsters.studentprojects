from django.shortcuts import render 
from django.http import HttpResponse   


def display(request):
    s = '''
    <html>
    <head>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .blink {
                animation: blink 1s linear infinite;
                color: pink;
                font-size: 28px;
                font-weight: bold;
            }
            @keyframes blink {
                50% {
                    opacity: 0;
                }
            }
        </style>
    </head>
    <body>
        <div class="blink">
            Hello Students welcome to Sagar Sir Django classes!!!
        </div>
    </body>
    </html>
    '''
    return HttpResponse(s)