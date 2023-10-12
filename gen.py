import random
from rich.console import Console
from rich.progress import track
from rich.prompt import IntPrompt
from rich.panel import Panel
from rich.text import Text

console = Console()

def generate_ipv4(existing_ips):
    """Generate a valid IPv4 address ensuring it's unique."""
    while True:
        ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        if ip not in existing_ips and not ip.startswith("0.") and not ip.endswith("255.255.255.255"):
            return "https://" + ip

def display_branding():
    """Display branding message."""
    branding_text = Text("CREATED BY VORTEX IP GENERATOR", style="bold blue")
    console.print(Panel(branding_text, expand=False))

def main():
    # Display branding
    display_branding()

    # Display a welcome message
    console.print("[bold magenta]Welcome to the Ultimate IP Generator![/bold magenta]\n")

    # Ask the user for the number of IP addresses
    num_ips = IntPrompt.ask("How many IP addresses do you want to generate?")

    generated_ips = set()
    for _ in track(range(num_ips), description="[cyan]Generating unique IPs..."):
        ip = generate_ipv4(generated_ips)
        generated_ips.add(ip)

    # Write to ip.txt
    with open("ip.txt", "w") as file:
        for ip in generated_ips:
            file.write(ip + "\n")

    console.print(f"[green]{num_ips} unique IP addresses have been written to ip.txt[/green]")

if __name__ == "__main__":
    main()
