from scapy.all import *
ip = "10.10.111.1"
closed_ports =[]
open_ports = []

def udp_scan(dst_ip, port):
	src_port=RandShort()
	udp_packet=IP(dst=dst_ip)/UDP(sport=RandShort(),dport=port)/DNS(rd=1, qd=DNSQR(qname="www.google.com"))
	udp_packet_response = sr1(udp_packet, inter=0.5, retry=-2, timeout=15)
	if str(type(udp_packet_response)) == "<type 'NoneType'>":
		open_ports.append(port) 
	elif udp_packet_response.haslayer(UDP):
		open_ports.append(port)
	elif udp_packet_response.haslayer(ICMP):
		if (int(udp_packet_response.getlayer(ICMP).type)==3 and int(udp_packet_response.getlayer(ICMP).code) == 3):
			closed_ports.append(port)
if __name__ == "__main__":
	ports = range(1,101)
	print "Starting udp port scanning on IP %s"%ip
	for port in ports:
		udp_scan(ip,port)	
	print "Udp port scanning completed for IP %s"%ip
	if len(closed_ports)!=0 and len(open_ports)!=0:
		print "Opened ports: ",open_ports,
		print "\n"
                print "Closed: ",closed_ports,
 
