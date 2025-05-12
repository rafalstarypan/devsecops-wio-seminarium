# DevSecOps Demo Project

This repository demonstrates a simple DevSecOps pipeline integrating security checks directly into the CI/CD workflow using GitHub Actions. It shows how to catch common security issues early in the development lifecycle using static analysis (SAST) and dependency scanning.

## 📁 Project Structure

## ⚙️ What the Pipeline Does

This GitHub Actions workflow (`.github/workflows/security.yml`) performs the following steps automatically on every push or pull request to the `main` branch:

1. **Checks out the repository code**
2. **Installs dependencies** listed in `requirements.txt`
3. **Runs static application security testing (SAST)** using [Semgrep](https://semgrep.dev)
4. **Scans dependencies for known vulnerabilities** using [pip-audit](https://pypi.org/project/pip-audit/)

## 🔍 Security Features Demonstrated

- **Vulnerable code snippet**: `app.py` contains an example of command injection (`os.system(f"...")`).
- **Semgrep rule**: A custom rule is defined to detect unsafe usage of `os.system`.
- **Dependency scanning**: `pip-audit` identifies known vulnerabilities in installed packages without requiring authentication or API keys.

## 🚀 Getting Started

To run this project:

1. Clone this repository or upload it to a new GitHub repo.
2. Make sure GitHub Actions are enabled.
3. Push to the `main` branch or open a pull request — the pipeline will run automatically.
