# pulsecheck

Pulsecheck is a Python automation tool that checks the health of your services from a simple YAML config. It verifies HTTP status and latency, TLS certificate expiry, DNS resolution and open ports, then reports results with clear exit codes for CI/CD and scheduled jobs. Built as a production-style project, it grows step by step into a full automation platform with Terraform, Ansible, Kubernetes and observability.

## Development setup

Requires Python 3.11+.

```bash
git clone git@github.com:sasho500/pulsecheck.git
cd pulsecheck
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

## Project layout

```
pulsecheck/
├── src/pulsecheck/      # Python package
├── tests/               # pytest suite
├── examples/targets.yaml
├── pyproject.toml
└── README.md
```
