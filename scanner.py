import nmap
import socket
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()

def ping_sweep(network):
    nm = nmap.PortScanner()
    console.print(f"[bold cyan]Performing ping sweep on {network}...[/bold cyan]")
    nm.scan(hosts=network, arguments='-sn')

    live_hosts = []
    for host in nm.all_hosts():
        if nm[host].state() == "up":
            live_hosts.append(host)

    console.print(f"[bold green]Live hosts found: {len(live_hosts)}[/bold green]")
    for h in live_hosts:
        print(f"✔ {h}")

    return live_hosts


def port_scan(target):
    console.print(f"\n[bold cyan]Scanning ports on {target}...[/bold cyan]")
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')

    table = Table(title=f"Open Ports on {target}")
    table.add_column("Port")
    table.add_column("State")
    table.add_column("Service")

    for proto in nm[target].all_protocols():
        ports = nm[target][proto].keys()
        for port in sorted(ports):
            state = nm[target][proto][port]['state']
            service = nm[target][proto][port]['name']
            table.add_row(str(port), state, service)

    console.print(table)


def main():
    console.print("[bold yellow]Network Scanner Tool[/bold yellow]")
    console.print("[bold magenta]1. Ping Sweep[/bold magenta]")
    console.print("[bold magenta]2. Port Scan[/bold magenta]")
    choice = input("Choose an option (1-2): ")

    if choice == "1":
        network = input("Enter network range (e.g., 192.168.1.0/24): ")
        ping_sweep(network)

    elif choice == "2":
        target = input("Enter target IP: ")
        port_scan(target)

    else:
        print("[red]Invalid choice[/red]")


if __name__ == "__main__":
    main()
