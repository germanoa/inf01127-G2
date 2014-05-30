from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from ipalloc.models import Network, IP

from netaddr import IPNetwork, AddrFormatError

@login_required(login_url='/')
def index(request):
    return render(request,'index.html', )

def add_network(request):
    
    if request.method == 'POST':
        name = request.POST.get("netname", "")
        try:
            net = IPNetwork(request.POST.get("addnet", ""))
        except AddrFormatError as e:
            # forma apropriada de manda mensagens.
            messages.add_message(request, messages.INFO, str(e))
            return HttpResponseRedirect("adminmenu")
        else:
            new_network = Network(name = name)
            new_network.save()
            #ip = IP()
            ip = new_network.ips.all()[1] #como modificar o ip default para evitar a duplicacao de dados?
            ip.set_address(unicode(net.ip), 4)
            ip.set_mask(unicode(net.netmask), 4)
            #ip.save()

            #new_network.ips.add(ip)  
            new_network.save()
            return HttpResponseRedirect("adminmenu")
    else:
        return redirect('adminmenu')

def adminmenu(request):
    networks = Network.objects.all()
    if request.user.is_superuser:
        return render(request, "adminmenu.html", {"networks" : networks})
