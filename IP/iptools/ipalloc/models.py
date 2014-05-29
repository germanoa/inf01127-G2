from django.db import models
from django.contrib.auth.models import User

class IP(models.Model):
    address = models.IntegerField(default=0)
    mask = models.IntegerField(default=0)
    version = models.IntegerField(default=4)

    def __int_to_dottedIP(self, intip):
        octet = ''
        for exp in [3,2,1,0]:
            octet = octet + str(intip / ( 256 ** exp )) + "." 
            intip = intip % ( 256 ** exp )
        return(octet.rstrip('.'))

    def __dotted_to_intIP(self, dottedip):
        octets = dottedip.split('.')
        intip=0
        for i in [3,2,1,0]:
            intip = intip + int(octets[3-i]) * 256 ** i
        return(intip)
    
    def __ip_to_net(self, ip,mask):
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
            self.address = self.__dotted_to_intIP(dottedIP)

    def get_address(self):
        return self.__int_to_dottedIP(self.address)

    def set_mask(self,dottedMASK,version):
        if version==4:
            self.mask = self.__dotted_to_intIP(dottedMASK)

    def get_mask(self):
        return self.__int_to_dottedIP(self.mask)

    # t: {"int", "dotted"}
    def get_net(self,t):
        ip= self.get_address()
        mask= self.get_mask()
        if t=="int":
            return self.__ip_to_net(ip,mask)
        elif t=="dotted":
            return self.__int_to_dotted(__ip_to_net(ip,mask))
        else:
            return -1

class Network(IP):
    name = models.CharField(max_length=256)
    administrator = models.ForeignKey(User, null=True)
    subnets = models.ManyToManyField('self', null=True)
    ips = models.ManyToManyField(IP, related_name="ips")
    
    def __unicode__(self):
        return self.name

