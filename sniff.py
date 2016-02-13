from scapy.all import *
import json

def main(pkt):
	if pkt[Raw]:
		with open("requests.json", "w+") as f:
			print pkt[Raw]
			f.write(pkt[Raw])

pkt = sniff(filter= 'dst port 6660', prn=main)
