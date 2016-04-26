from scapy.all import *
conf.checkIPaddr=False
fam,hw=get_if_raw_hwaddr(conf.iface)
dhcp_dicover= Ether(dst='ff:ff:ff:ff:ff:ff')/IP(src='0.0.0.0',dst='255.255.255.255')/UDP(sport=68,dport=67)/BOOTP(chaddr=hw)/DHCP(options=[("message-type","discover"),"end"])
ans,unans=srp(dhcp_dicover, multi=True)
ans.summary()
