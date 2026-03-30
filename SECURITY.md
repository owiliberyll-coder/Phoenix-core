# Security Policy

## Security Updates

Phoenix Core takes security seriously. We are committed to patching vulnerabilities promptly.

## Reporting Security Vulnerabilities

**Please do not create public GitHub issues for security vulnerabilities.**

Instead, report security issues to: **owiliberyll@gmail.com**

Include:
- Description of the vulnerability
- Steps to reproduce (if applicable)
- Potential impact
- Suggested fix (optional)

We will acknowledge receipt within 48 hours and aim to release a fix within 7 days for critical issues.

## Security Considerations

### Current Implementation
- Runs at userspace on Termux (no elevated privileges initially)
- Image processing is done locally (no external API calls)
- All detection happens on-device
- No data collection or telemetry

### Kernel Module (Future)
- When migrating to kernel space, we will:
  - Use secure module loading
  - Implement proper isolation
  - Follow Linux security best practices
  - Regular security audits

### Cryptographic Key Management
- Future versions will support encrypted logging
- Multi-party key system planned for Q4 2025
- Hardware-backed keys via TPM when available

## Privacy by Design

- No data is sent to external servers
- All processing is local
- Optional encrypted local logging only
- User has full control over data

## Dependencies

We use minimal dependencies:
- PIL/Pillow (image processing)
- NumPy (numerical computation)
- Termux API (camera access)

All dependencies are open-source and regularly updated.

## Compliance

Phoenix Core is designed to respect:
- User privacy
- User autonomy
- Platform terms of service
- Applicable laws and regulations

Users are responsible for ensuring their use complies with local laws.

## Security Roadmap

- Q2 2025: Kernel module with secure loading
- Q3 2025: Encrypted logging
- Q4 2025: Multi-party key system
- 2026: Third-party security audit

---

For questions about security, contact: owiliberyll@gmail.com
