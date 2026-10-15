PROFILE = {
    "name": "Barbosa",
    "title": "Junior Infrastructure / DevOps Engineer",
    "location": "Portugal",
    "summary": (
        "Hands-on infrastructure and software intern who has configured production "
        "firewalls and VPNs, helped build a company data centre, and builds internal "
        "web apps in Python and React. I run a personal homelab (Ubuntu Server, "
        "Kubernetes with k3s) to practise DevOps: containers, CI/CD and GitOps."
    ),
    "links": {
        "github": "https://github.com/GustaBarbosa",
        "linkedin": "https://www.linkedin.com/in/gustavobmorais",
        "email": "mailto:gustavo.b.live@hotmail.com",
    },
}

SKILLS = [
    {
        "group": "Networking & Security",
        "items": ["OPNsense", "VLANs", "Firewall rules", "WireGuard / NetBird", "Tailscale", "Structured cabling", "Wazuh"],
    },
    {"group": "Systems", "items": ["Linux (Ubuntu Server)", "Kubernetes (k3s)", "Docker", "NetBox"]},
    {"group": "Development", "items": ["Python (FastAPI)", "React", "REST APIs", "PostgreSQL", "pytest"]},
    {"group": "Tooling", "items": ["Git", "GitHub", "GitLab CI/CD"]},
    {"group": "Languages", "items": ["Portuguese (native)", "English (C1)", "Spanish (B1)", "French (A1)"]},
]

EXPERIENCE = [
    {
        "company": "ATLAR Innovation",
        "role": "IT Infrastructure Intern",
        "period": "Aug 2026 – Present",
        "highlights": [
            "Configured the company's OPNsense firewall, segmenting the network into 10 VLANs "
            "by function and risk level, with default-deny rules between them.",
            "Set up site-to-site VPNs with NetBird (WireGuard) to connect sites securely.",
            "Helped build the company data centre: rack layout, power distribution and "
            "structured cabling (copper and fibre).",
            "Tested Wazuh (SIEM/XDR) for central log collection and threat detection.",
            "Documented network and hardware assets in NetBox.",
            "Developed internal web apps with Python (FastAPI) and React.",
        ],
    },
    {
        "company": "ATLAR Innovation",
        "role": "Software Developer (part-time, alongside studies)",
        "period": "Feb 2026 – Jul 2026",
        "highlights": [
            "Built internal web apps with Python and React.",
            "Designed REST APIs on PostgreSQL, running in Docker on Linux, with GitLab CI/CD.",
            "Fixed access-control flaws (IDOR) and added input validation to API endpoints.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Homelab Portfolio",
        "description": (
            "This website: a FastAPI app with automated tests (pytest), self-hosted on a "
            "home Ubuntu Server running Kubernetes (k3s) with Traefik. Remote administration "
            "over a mesh VPN (Tailscale / NetBird) with no ports opened on the home router."
        ),
        "tags": ["Python", "FastAPI", "pytest", "k3s", "Traefik", "Tailscale"],
        "url": "https://github.com/GustaBarbosa/portfolio",
    },
]
