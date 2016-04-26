from scapy.all import *
ip='10.10.111.1'
dst_port=53
src_port=RandShort()
dns_query_response=sr1(IP(dst=ip)/UDP(sport=RandShort(),dport=dst_port)/DNS(rd=1, qd=DNSQR(qname="www.google.com")))
if dns_query_response.haslayer(UDP):
	print "The udp port %s of %s is open"%(dst_port,ip)
	if dns_query_response.haslayer(DNS):
		print "%s's DNS service on port %s is running normally"%(ip,dst_port)
	else: 
		print "DNS service is not running on port %s"%dst_port
else:
	print "The port is closed"
 
