# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

## Reporting a Vulnerability

We take the security of Promethium seriously. If you discover a security vulnerability, please do **not** disclose it publicly until we have had a chance to address it.

### Process

1. **Private Reporting**: Please report vulnerabilities by emailing the project maintainers directly (placeholder: security@example.com) or by opening a GitHub Issue with the "Security" label (if no private channel is available).
2. **Triage**: The team will acknowledge receipt of your report within 48 hours.
3. **Resolution**: We will provide an estimated timeline for a fix.
4. **Disclosure**: Public disclosure will occur only after the patch has been released.

### Scope

We are particularly interested in:
- Unauthenticated access to API endpoints.
- Injection vulnerabilities (SQL, Command) via Dataset metadata or filenames.
- Exposure of sensitive configuration (database credentials) via logging.
- Cross-Site Scripting (XSS) in the Web Dashboard.

Thank you for helping keep Promethium secure.
