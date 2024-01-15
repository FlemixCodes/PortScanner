import socket
from threading import Thread


class Scanner:
    ports = {
        21: "FTP",
        22: "SSH",
        23: "TELNET",
        25: "SMTP",
        43: "WHOIS",
        53: "DNS",
        68: "DHCP",
        80: "HTTP",
        110: "POP3",
        115: "SFTP",
        119: "NNTP",
        123: "NTP",
        139: "NETBIOS",
        143: "IMAP",
        161: "SNMP",
        179: "BGP",
        220: "IMAP3",
        389: "IDAP",
        443: "HTTPS",
        993: "IMAPS",
    }

    def __init__(self, target: str, hostname: bool = False) -> None:
        self.target = target
        self.hostname = hostname

        if self.hostname:
            self.ip = socket.gethostbyname(self.target)
        else:
            self.ip = self.target

    def scan_run(self) -> None:
        print("Scanning...")
        for port, name in self.ports.items():
            Thread(target=self._scan_port, args=(port, name,)).start()

    def _scan_port(self, port: int, name: str) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if not sock.connect_ex((self.ip, port)):
                print(f"Port {port}({name}) [+]")
            else:
                print(f"Port {port}({name}) [-]")
