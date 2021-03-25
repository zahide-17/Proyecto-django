from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
def index(request):
    """ Vista para atender la petición de la url / """
    # Obteniendo los datos mediantes consultas
    product = Product.objects.all()
    return render(request, "products/index.html", {"product":product})

def login(request):
    """Atiende las peticiones de GET /login/"""
    # Se definen los datos de un usuario válido
    # Si hay datos vía POST se procesan
    if request.method == "POST":
         # Se obtienen los datos del formulario
        usuario_form = (
            request.POST["username"],
            request.POST["password"],
            request.POST["password"],
            request.POST["password"],
            request.POST[""],
            request.POST[""],
            request.POST[""],
            request.POST[""],
            )
        if usuario_form is not None:
            # Se agregan datos al request para mantener activa la sesión
            login(request, acceso)
            # Y redireccionamos a next
            return redirect(next)
        else:
            # Usuario malo
            msg = "Datos incorrectos, intente de nuevo!"
    else:
        # Si no hay datos POST
        msg = "Request invalido"
    return render(request, "registration/checkIn.html")
