import os
import socket

from crewai import LLM, Agent, Task
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


# Create an Agent and tool is handover to it
security_analyst = Agent(
    role="Senior Security Analyst",
    goal="Examining servers to identify open ports and ensure security.",
    backstory="You are a skilled Cybersecurity expert who tests the security of servers and provides information.",
    verbose=True,
    tools=[run_port_scanner],  # Agent use tis tool
    allow_delegation=False,
    llm=llm,
)

# Create a task for agent
scan_task = Task(
    description="Check which ports are open on the website scanme.nmap.org. Then, write a brief report in detailing your findings and the potential implications of these ports being open.",
    expected_output="A list of the scanned ports and a brief security report regarding them.",
    agent=security_analyst,
)
