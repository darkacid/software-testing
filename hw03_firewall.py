import ipaddress
from logging import exception
class firewall:
    blockList = []
    enabledServices = []
    supportedServices = ["ssh","http"]
    def block(self,subnet:str):
        if not isinstance(subnet,str):
            return ("Subnet must be a string.")
        if subnet in self.blockList:
            return ("Subnet already blocked.")
        try:
            ipvalidation = ipaddress.ip_network(subnet) #Validate subnet before adding
        except:
            return ("Invalid IP")
        self.blockList.append(subnet)
        return True

    def unblock(self,subnet:str):
        if not isinstance(subnet,str):
            return("Subnet must be a string.")
        if subnet not in self.blockList:
            return("Subnet not blocked.")
        try:
            ipvalidation = ipaddress.ip_network(subnet) #Validate subnet before adding
        except:
            return ("Invalid IP")
        self.blockList.remove(subnet)
        return True

    def enableService(self,serviceName:str):
        if not isinstance(serviceName,str):
            return("Service name must be a string.")
        if serviceName not in self.supportedServices:
            return("Service name not recognized.")
        self.enabledServices.append(serviceName)
        return True

    def disableService(self,serviceName:str):
        if not isinstance(serviceName,str):
            return("Service name must be a string.")
        if serviceName not in self.supportedServices:
            return("Service name not recognized.")
        self.enabledServices.remove(serviceName)
        return True

