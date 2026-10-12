PROFILE = {
    "name": "Barbosa",
    "title": "DevOps / Software Engineer",
    "location": "Portugal",
    "summary": (
        "I build and run infrastructure: containers, Kubernetes, CI/CD and "
        "automation. This site runs on my own homelab and deploys itself with GitOps."
    ),
    "links": {
        "github": "https://github.com/GustaBarbosa",
        "linkedin": "https://www.linkedin.com/in/gustavobmorais/",
        "email": "mailto:gustavo.moras@atlar.com",
    },
}

SKILLS = [
    {"group": "Containers", "items": ["Docker", "Kubernetes (k3s)", "Helm / Kustomize"]},
    {"group": "Delivery", "items": ["GitHub Actions", "Argo CD", "GitOps"]},
    {"group": "Automation", "items": ["Ansible", "Terraform", "Bash"]},
    {"group": "Languages", "items": ["Python", "Java"]},
    {"group": "Operations", "items": ["Linux", "Prometheus", "Grafana"]},
]

EXPERIENCE = [
    {
        "company": "ATLAR Innovation",
        "role": "Software Developer / IT Infrastructure (Internship)",
        "period": "Aug 2026 – now",
        "highlights": [
            "Helped build the company data centre: rack layout, power distribution and structured cabling (copper and fibre)",
            "Run OPNsense firewalls with VLAN segmentation and default-deny policies",
            "Set up site-to-site VPNs with NetBird / WireGuard",
            "Evaluated Wazuh (SIEM/XDR) for log centralisation and threat detection",
            "Document infrastructure and assets in a DCIM (NetBox)",
        ],
    },
    {
        "company": "ATLAR Innovation",
        "role": "Software Developer (Extracurricular)",
        "period": "Feb 2026 – Jul 2026",
        "highlights": [
            "Built and maintained internal web apps with Python and React, including the AgilityHR platform",
            "Designed REST APIs on PostgreSQL, running in Docker on Linux",
            "Hardened endpoints against IDOR and added input validation",
        ],
    },
]

PROJECTS = [
    {
        "name": "Homelab platform",
        "description": "This website: FastAPI in Docker on k3s, deployed by Argo CD from GitHub.",
        "tags": ["k3s", "Argo CD", "Docker", "Ansible"],
        "url": "https://github.com/GustaBarbosa?tab=repositories",
    },
    {
        "name": "Minecraft server",
        "description": "Self-hosted game server running alongside the cluster on the same laptop.",
        "tags": ["Linux", "systemd"],
        "url": None,
    },
]
