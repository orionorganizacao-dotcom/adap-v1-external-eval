
Markdown
# A-DAP v2 — Auditable Decision Protocol

Minimal protocol for externally verifiable decision integrity.

---

## Core Principle

Evidence must be verifiable independently of the system that produced it.

---

## Problem

Most automated decision systems operate under a silent assumption:

The same system that decides is also responsible for recording, explaining and validating its own decisions.

This creates a structural limitation:

- internal logs are not independent proof  
- explanations do not guarantee integrity  
- auditability becomes self-referential  

---

## Approach

A-DAP v2 separates:

- decision execution  
- evidence generation  
- external verification  

---

## Components

- Canonical decision ledger (JSON)
- SHA-256 hash
- Asymmetric signature (Ed25519)
- Public key verification
- External timestamp
- Optional public anchoring

---

## Verification

Any third party can verify:

- integrity of the record  
- authorship of the signature  
- existence at a given time  

Without privileged access.

---

## What A-DAP v2 Guarantees

- integrity (no tampering)
- authenticity (who signed)
- temporal existence (when it existed)
- independent verification

---

## What It Does NOT Guarantee

- correctness of the decision  
- fairness or bias  
- validity of inputs  

A-DAP is about process integrity, not outcome validity.

---

## Minimal Structure
ledger.json
ledger.sha256
ledger.sig
public_key.pem
manifest.json
verify_adap_v2.py

---

## Why It Matters

If evidence cannot be verified independently, governance becomes narrative.

---

## Status

Experimental — minimal viable specification (v2)

---

## Author

Ezio v.s. Santos  
Independent Researcher — AI Governance & Systemic Risk
