from scapy.all import *
ip = "10.10.111.1"
closed_ports =[]
open_ports = []
filtered_ports =[]
def tcp_scan(dst_ip,port):
	src_port=RandShort()
	tcp_packet=IP(dst=dst_ip)/TCP(sport=src_port, dport=port, flags="S")
	tcp_scan_response = sr1(tcp_packet, inter=0.5, retry=2,timeout=10)
	if str(type(tcp_scan_response)) == "<type 'NoneType'>":	
		filtered_ports.append(port)
	elif tcp_scan_response.haslayer(TCP):
		if tcp_scan_response.getlayer(TCP).flags == 0x12:
			send_rst = sr(IP(dst=ip)/TCP(sport=src_port, dport=port, flags="R"), timeout=2)	
			open_ports.append(port)
		elif tcp_scan_response.getlayer(TCP).flags == 0x14:
			closed_ports.append(port)
		elif tcp_scan_response.haslayer(ICMP):
			if (int(tcp_scan_response.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
				filtered_ports.append(port) 
if __name__ == '__main__':
	ports = range(1,101)
	print "Starting tcp port scanning on IP %s"%ip
	for port in ports:
		tcp_scan(ip,port)
	print "TCP port scanning completed for IP %s"%ip
	if len(open_ports)!=0 and len(closed_ports)!=0:
		print "Opened ports: ",open_ports,
		print "\n"
		print "Closed port: ",closed_ports,
	if len(filtered_ports)!=0:
		print "\n"
		print "Filtered ports: ",filtered_ports,
 
