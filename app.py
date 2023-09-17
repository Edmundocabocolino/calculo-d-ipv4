from classes.calcipv4 import Calcipv4

calc_ipv4 = Calcipv4(ip='192.168.0.1',mascara='255.255.255.0',prefixo= 24)


print(calc_ipv4.ip)
print(calc_ipv4.mascara)
print(calc_ipv4.rede)
print(calc_ipv4.broadcast)
print(calc_ipv4.prefixo)
print(calc_ipv4.numero_ips)
