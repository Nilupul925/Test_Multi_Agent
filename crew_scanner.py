import os
import socket

from crewai import LLM
from crewai.tools import tool
from dotenv import load_dotenv

# Getting API keys
load_dotenv()
llm = LLM(model="gemini-3.5-flash-lite", api_key=os.getenv("GEMINI_API_KEY"))


# Create port scanner tool
@tool("Port Scanner Tool")
def run_port_scanner(target_ip_or_domain: str) -> str:
    """
    Use this tool to check for open ports on the provided target IP address or domain.
    """
    print(f"\n[🚀 Security Tool activated: Scanning {target_ip_or_domain}...]")

    ports_to_scan = [21, 22, 80, 443, 8080]
    open_ports = []

    try:
        target_ip = socket.gethostbyname(target_ip_or_domain)
    except socket.gaierror:
        return f"Error: The domain '{target_ip_or_domain}' could not be found."

    for port in ports_to_scan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        if sock.connect_ex((target_ip, port)) == 0:
            open_ports.append(str(port))

        sock.close()

    if open_ports:
        return f"Success! Open ports on {target_ip_or_domain}: {','.join(open_ports)}"
    else:
        return f"None of the ports checked on {target_ip_or_domain} are open."
