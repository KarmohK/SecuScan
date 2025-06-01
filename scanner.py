import socket
from datetime import datetime

def banner_grab(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return "No banner received"

def scan_ports(ip, ports):
    print(f"Scanning {ip}...")
    open_ports = []

    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((ip, port))
            banner = banner_grab(ip, port)
            print(f"[OPEN] Port {port} | Banner: {banner}")
            open_ports.append((port, banner))
            s.close()
        except:
            pass

    return open_ports

def save_report(ip, results):
    filename = f"{ip.replace('.', '_')}_report.txt"
    with open(filename, "w") as file:
        file.write(f"Scan report for {ip} - {datetime.now()}\n\n")
        for port, banner in results:
            file.write(f"Port {port} - OPEN - {banner}\n")
    print(f"\nReport saved as {filename}")

if __name__ == "__main__":
    target = input("Enter target IP address: ").strip()
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    results = scan_ports(target, ports_to_scan)
    save_report(target, results)
Added main port scanning script
