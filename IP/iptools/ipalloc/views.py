from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from ipalloc.models import Network, IP

from netaddr import IPNetwork, AddrFormatError

from django.contrib.auth.models import User

@login_required(login_url='/')
def index(request):
    return render(request,'index.html', )

def select_manager_to_network(request):
    if request.method == 'POST':
        manager = request.POST.get("manager", "")
        # 1.para cada rede marcada
        #    seta var manager

def add_network(request):
    if request.method == 'POST':
        name = request.POST.get("netname", "")
        try:
            net = IPNetwork(request.POST.get("addnet", ""))
        except AddrFormatError as e:
            # forma apropriada de manda mensagens.
            messages.add_message(request, messages.INFO, str(e))
        else:
            new_network = Network(name = name)
            new_network.set_address(unicode(net.ip), 4)
            new_network.set_mask(unicode(net.netmask), 4)
            if new_network.is_net():
                new_network.save()
            else:
                error_message = "Informed address is not in a valid\
                network address format"
                messages.add_message(request, messages.INFO, error_message)
        finally:
            return HttpResponseRedirect("adminmenu") 
    else:
        return redirect('adminmenu')

def adminmenu(request):
    networks = Network.objects.all()
    #networks_dotted = []
    #for n in networks:
    #    networks_dotted.append(n.get_address())        
    users = User.objects.all()
    if request.user.is_superuser:
        return render(request, "adminmenu.html", {"networks" : networks, "users" : users})
