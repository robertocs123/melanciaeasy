from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import PedidoForm
from django.contrib import messages
import datetime

from .models import Pedido

@login_required
def pedidoList(request):
    
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    pedidosDoneRecently = Pedido.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    pedidosDone = Pedido.objects.filter(done='done', user=request.user).count()
    pedidosDoing = Pedido.objects.filter(done='doing', user=request.user).count()

    if search:
        pedidos = Pedido.objects.filter(title__icontains=search, user=request.user)
    elif filter:
        pedidos = Pedido.objects.filter(done=filter, user=request.user)
    else:
        pedidos_list = Pedido.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(pedidos_list, 3)

        page = request.GET.get('page')
        pedidos = paginator.get_page(page)

    return render(request, 'cliente/list.html', 
        {'pedidos':pedidos, 'pedidosrecently': pedidosDoneRecently, 'pedidosdone': pedidosDone, 'pedidosdoing': pedidosDoing })

@login_required
def pedidoView(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    return render(request, 'cliente/pedido.html', {'pedido': pedido})

@login_required
def newPedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.done = 'doing'
            pedido.user = request.user
            pedido.save()
            return redirect('/')
    else:
        form = PedidoForm()
        return render(request, 'cliente/addpedido.html', {'form': form})

@login_required
def editPedido(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    form = PedidoForm(instance=pedido)

    if(request.method == 'POST'):
        form = PedidoForm(request.POST, instance=pedido)

        if(form.is_valid()):
            pedido.save()
            return redirect('/')
        else:
            return render(reuquest, 'cliente/editpedido.html', {'form': form, 'pedido': pedido})
    else:
        return render(request, 'cliente/editpedido.html', {'form': form, 'pedido': pedido})

@login_required
def deletePedido(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    pedido.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')

@login_required
def changeStatus(request, id):
    pedido = get_object_or_404(Pedido, pk=id)

    if(pedido.done == 'doing'):
        pedido.done = 'done'
    else:
        pedido.done = 'doing'

    pedido.save()

    return redirect('/')

@login_required
def helloWorld(request):
    return HttpResponse('Hello World!')
    
@login_required
def yourName(request, name):
    return render(request, 'cliente/yourname.html', {'name':name})


def sobre(request):
    return render(request, 'cliente/sobre.html')


@login_required
def precos(request):
    return render(request, 'cliente/precos.html')

@login_required
def fotos(request):
    return render(request, 'cliente/fotos.html')