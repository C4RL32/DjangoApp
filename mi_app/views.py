from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Bienvenidos a Mi Proyecto Django</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 600px;
            }
            h1 {
                color: #4CAF50;
            }
            p {
                font-size: 18px;
                color: #555;
            }
            .author {
                margin-top: 20px;
                font-weight: bold;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenidos a Mi Proyecto Django</h1>
            <p>
                Django es un framework web de alto nivel que te permite crear aplicaciones web de forma rápida y eficiente. 
                Fue creado en Python y su objetivo es hacer el desarrollo web más simple y limpio, usando el principio de "No te repitas" (DRY - Don't Repeat Yourself).
            </p>
            <p>
                Con Django, puedes crear desde aplicaciones sencillas hasta sistemas web complejos, utilizando herramientas integradas para manejo de bases de datos, 
                autenticación, plantillas HTML, seguridad y más.
            </p>
            <p class="author">
                Página elaborada por: <strong>Carlos Hernández</strong>
            </p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
