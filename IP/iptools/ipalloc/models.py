from django.db import models
from django.contrib.auth.models import User
from django import forms

class IP(models.Model):
    address = models.IntegerField(default=0)
    mask = models.IntegerField(default=0)
    version = models.IntegerField(default=4)

    def _int_to_dottedIP(self, intip):
        octet = ''
        for exp in [3,2,1,0]:
            octet = octet + str(intip / ( 256 ** exp )) + "." 
            intip = intip % ( 256 ** exp )
        return(octet.rstrip('.'))

    def _dotted_to_intIP(self, dottedip):
        octets = dottedip.split('.')
        intip=0
        for i in [3,2,1,0]:
            intip = intip + int(octets[3-i]) * 256 ** i
        return(intip)
    
    def _ip_to_net(self,ip,mask):
        ipoctets = ip.split('.')
        maskoctets = mask.split('.')
        netip=0
        for i in [3,2,1,0]:
            ipoctet = (int(ipoctets[3-i]) * 256 ** i)
            maskoctet = (int(maskoctets[3-i]) * 256 ** i)
            netip = netip + (ipoctet & maskoctet)
        return netip
    
    def set_address(self,dottedIP,version):
        if version==4:
            self.address = self._dotted_to_intIP(dottedIP)

    def get_address(self):
        return self._int_to_dottedIP(self.address)

    def set_mask(self,dottedMASK,version):
        if version==4:
            self.mask = self._dotted_to_intIP(dottedMASK)

    def get_mask(self):
        return self._int_to_dottedIP(self.mask)

    # t: {"int", "dotted"}
    def get_net(self,t):
        ip= self.get_address()
        mask= self.get_mask()
        if t=="int":
            return self._ip_to_net(ip,mask)
        elif t=="dotted":
            return self._int_to_dottedIP(self._ip_to_net(ip,mask))
        else:
            return -1
    
    def is_net(self):
        return self.get_address() == self.get_net("dotted")

class Network(IP):
    name = models.CharField(max_length=256)
    administrator = models.ForeignKey(User, null=True)
    subnets = models.ManyToManyField('self', null=True)
    ips = models.ManyToManyField(IP, related_name="ips")
    
    def __unicode__(self):
        return self.name

class ManagerToNetwork(forms.Form):
    manager = forms.ChoiceField()
        

