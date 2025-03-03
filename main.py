import argparse
import scapy.all as scapy

class ARPping:

    def __init__(self):
        print("ARPping başlatıldı...")

    def user_input(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--ipaddress', type=str, help="IP adresinizi girmelisiniz")
        args = parser.parse_args()

        if args.ipaddress is not None:
            return args
        else:
            print("IP adresini -i argümanı ile giriniz...")
            exit()

    def arp_istegi(self, ip):
        arp_request_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet / arp_request_packet

        answered_list, unanswered_list = scapy.srp(combined_packet, timeout=2, verbose=False)

        if answered_list:
            answered_list.summary()
        else:
            print("Cevap alınamadı!")

if __name__ == "__main__":
    arp_ping = ARPping()
    kullanıcı_girdisi = arp_ping.user_input()
    arp_ping.arp_istegi(kullanıcı_girdisi.ipaddress)
