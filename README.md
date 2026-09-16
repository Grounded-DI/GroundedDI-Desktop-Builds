# Grounded DI Desktop Builds

A public evidence archive for Grounded DI LLC's local-first desktop prototypes, replay demonstrations, validation records, and visual build artifacts.

## Overview

This repository preserves selected public artifacts from Grounded DI desktop application work across legal review, environmental monitoring, defensive security, and games. The collection includes screenshots, videos, PDF implementation records, replay evidence, a redacted comparative report, and cryptographic checksums.

The represented systems use rule-governed processing, explicit validation states, human release boundaries, audit receipts, and replay or hash controls where the individual artifact documents them. In this context, *deterministic* means reproducible or threshold-defined behavior under stated inputs and serialization conditions; it does not mean that every output is universally correct or invariant.

This is an evidence and demonstration repository. The `main` branch does **not** currently contain application source code, installers, package manifests, deployment configuration, or a runnable automated test suite. Build and test results described below are therefore historical records unless expressly identified as rechecked during the current repository review.

## Why It Matters

Desktop AI and decision-support software can be difficult to evaluate from screenshots or output samples alone. The artifacts here focus on inspectable operational questions:

- What inputs and records were bound to a run?
- Which rules or gates controlled progression?
- Was a result held, released, or marked unresolved?
- Can a saved state be replayed and compared?
- What receipts, manifests, or hashes preserve artifact identity?
- Where does human authorization remain required?

The repository is intended to support technical review and scoped commercial evaluation without publishing private prompts, runtime packages, internal governance materials, or other nonpublic implementation details.

## Repository Highlights

| Area | Public evidence | Supported scope |
| --- | --- | --- |
| Grounded DI Local Control Desk | [`Grounded_DI_Local_Control_Desk_Implementation_Record_v1.pdf`](Grounded_DI_Local_Control_Desk_Implementation_Record_v1.pdf) | A documented local-first macOS MVP workflow with state controls, baseline preservation, JSON import, local persistence, receipts, SHA-256 manifest generation, and ZIP export. The record reports React/Vite and Tauri 2 implementation. |
| BriefWise DI² audit and replay | [`BriefWise_DI²_Audit_and_Replay_Offline_close_reopen_fresh_evaluation_canonical-byte_comparison_and_SHA-256_matched.pdf`](BriefWise_DI%C2%B2_Audit_and_Replay_Offline_close_reopen_fresh_evaluation_canonical-byte_comparison_and_SHA-256_matched.pdf) | Visual evidence of frozen inputs, fresh recomputation, canonical serialization, replay comparison, and SHA-256 identity checks in a synthetic legal workflow. |
| BriefWise DI² legal review | [`BriefWise_DI2_Localhost_Demo_Output_Deterministic_Intelligence_Grounded_DI_LLC.pdf`](BriefWise_DI2_Localhost_Demo_Output_Deterministic_Intelligence_Grounded_DI_LLC.pdf) and [`BriefWise_DI_Caselaw_Heatmap_Demo_Localhost.pdf`](BriefWise_DI_Caselaw_Heatmap_Demo_Localhost.pdf) | Localhost demonstrations of issue decomposition, unresolved-item handling, filing-readiness gating, and authority-oriented visual analysis. These are demonstrations, not legal advice or proof of legal correctness. |
| Cross-engine legal drafting report | [`reports/briefwise-di2-on-gemini/`](reports/briefwise-di2-on-gemini/) | A redacted report, supporting evidence archive, source index, limitations, and SHA-256 checksums. The report analyzes errors in both compared answers and expressly rejects causal or superiority conclusions from a single unmatched comparison. |
| Environmental and safety interfaces | [`earthwise_visual_1_command_center_hd.png`](earthwise_visual_1_command_center_hd.png), [`earthwise_visual_2_eloc_events_hd.png`](earthwise_visual_2_eloc_events_hd.png), [`earthwise_visual_3_cleanair_map_hd.png`](earthwise_visual_3_cleanair_map_hd.png), [`earthwise_visual_4_audit_reviewer_hd.png`](earthwise_visual_4_audit_reviewer_hd.png), and related PDFs | Visual prototypes for structured observations, threshold events, map-based review, audit-chain review, and defensive security observations. Source and executable builds are not included. |
| Native game demonstrations | `Page Two`, `The Courier: Wrong Door`, `PUT THE MOON BACK`, `The Morning Line`, and `The Tornado` artifacts | macOS-oriented screenshots, visual portfolios, and short gameplay recordings documenting interface and gameplay behavior. These are media and build records, not distributable game packages. |

## Key Capabilities Evidenced

- Local-first and offline workflows in the identified demonstrations.
- Explicit control states and fail-closed outcomes that block progression or export when required conditions remain unresolved.
- Structured separation of sources, propositions, candidate work, control decisions, audit records, and authorized export in the BriefWise materials.
- Baseline preservation and bounded-change records in the Local Control Desk implementation record.
- Canonical serialization identified as `BW-JCS-NFC-LF-1` in the BriefWise replay artifacts.
- SHA-256 bindings, manifests, and publication checksums for artifact-identity verification.
- Human review and release boundaries, including attorney-controlled disposition in the Local Control Desk record.
- Public-safe evidence packaging with marked redactions and explicit scope limitations.

## Technical Highlights

### Rule-governed state control

The Local Control Desk record describes an enforced state sequence, field-specific validation, an immutable baseline, a one-declared-condition mutation guard, and separate `HOLD` and `RELEASE` controls. A demonstrated rerun changes one condition from false to true, reduces the recorded gap count, and remains on `HOLD` because other required conditions are unresolved.

### Replay and canonical identity

The BriefWise replay materials show a save-close-reopen cycle followed by fresh evaluation, canonical-byte comparison, and SHA-256 recomputation. The v1.1 artifact records a replay pass and displays separate bindings for restart identity, event-chain tip, evaluation, sources, gate results, and rule pack. These screenshots document the represented run; the repository does not include the replay engine needed to reproduce it independently.

### Audit packaging

The repository includes human-readable records, machine-readable evidence within the redacted ZIP archive, SHA-256 manifests, and Git commit history. Hashes can establish that bytes match a recorded artifact; they do not establish factual, legal, scientific, or analytical correctness.

### Deliberate validation boundaries

The strongest records state their limitations. Examples include synthetic inputs, no claim of universal determinism, no independent third-party certification, no complete legal validation, and no claim of production-security review or enterprise deployment readiness.

## Architecture

The desktop control applications represented here generally follow this documented pattern:

```text
Matter or evidence input
  -> frozen or normalized records
  -> structured source / proposition mapping
  -> rule and validation gates
  -> HOLD, RELEASE, or FilingReady disposition
  -> audit and replay record
  -> authorized export with receipts and hashes
```

The exact stages vary by product. This diagram is a repository-grounded summary of the public evidence, not a substitute for unpublished implementation specifications.

## How It Works

1. **Bind the input.** A matter, observation, source set, or game seed establishes the run context.
2. **Create structured records.** The interface separates inputs, mappings, candidates, and unresolved items rather than treating the result as a single text response.
3. **Evaluate controls.** Required fields, thresholds, mappings, or other declared conditions determine whether the run can progress.
4. **Route the state.** The system records a disposition such as `HOLD`, `RELEASE`, `FilingReady`, or unresolved.
5. **Preserve evidence.** Receipts, event history, canonical representations, exports, and hashes provide an inspection trail where shown by the relevant artifact.

## Repository Structure

```text
.
├── README.md
├── Grounded_DI_Local_Control_Desk_Implementation_Record_v1.pdf
├── BriefWise_DI2_Localhost_Demo_Output_...pdf
├── BriefWise_DI_Caselaw_Heatmap_Demo_Localhost.pdf
├── BriefWise_DI²_Audit_and_Replay_...pdf
├── BriefWise_DI²_Grounded_DI_1.0_With_Receipt.pdf
├── BriefWise_DI²_Grounded_DI_1.1_Audit_and_Replay_Match_With_Receipt.pdf
├── earthwise_visual_*.png
├── media/
│   ├── the-tornado-level-2-muted.mp4
│   └── the-tornado-v1.1.0-comparison.png
├── reports/
│   └── briefwise-di2-on-gemini/
│       ├── README.md
│       ├── BriefWise_DI2_on_Gemini.md
│       ├── BriefWise_DI2_on_Gemini.pdf
│       ├── BriefWise_DI2_on_Gemini_Evidence.zip
│       └── SHA256SUMS.txt
└── additional game, safety, weather, and provenance media
```

## Quick Start

Clone the public evidence archive:

```bash
git clone https://github.com/Grounded-DI/GroundedDI-Desktop-Builds.git
cd GroundedDI-Desktop-Builds
```

Open the top-level PDFs, images, and videos with standard desktop viewers. Start with the Local Control Desk implementation record for the clearest control-flow summary, then review the BriefWise replay artifact and the redacted report package.

Verify the three publication artifacts covered by the report checksum file:

```bash
cd reports/briefwise-di2-on-gemini
sha256sum -c SHA256SUMS.txt
```

On macOS, use:

```bash
shasum -a 256 -c SHA256SUMS.txt
```

There is no application build or installation command on `main` because executable packages, source trees, and package configuration are not included.

## Validation and Testing

| Evidence | What the repository records | Current review status |
| --- | --- | --- |
| Local Control Desk MVP 0.1.0, Version 6 | Typecheck, lint, production build, 14/14 automated tests, visual QA, print inspection, persistence/reset testing, and exported-byte comparison are reported in the implementation record. Physical Mac operation is shown separately. | Historical, creator-supplied record; no runnable suite is present here. |
| BriefWise DI² replay | Close, reopen, fresh evaluation, canonical-byte comparison, and SHA-256 match are shown for a synthetic filing-integrity vertical slice. | Artifact inspected; replay could not be independently executed from this repository. |
| The Tornado v1.1.0 | The supplied build record reports 45 passing tests across nine files, type checks, lint, production build, scripted replay, and offscreen rendering. | Historical record; the application suite was not rerun during publication. The build remains labeled `DRAFT` pending stated browser/native checks. |
| Redacted Gemini report package | `SHA256SUMS.txt` binds the PDF, Markdown report, and evidence ZIP; the ZIP also contains a per-file integrity manifest. | All three published checksums passed during the September 16, 2026 repository review. This confirms byte identity only. |

No source-level test coverage can be calculated from the current `main` branch. No artifact in this repository should be treated as independent certification, a legal-correctness guarantee, or a production-readiness finding.

## Example Use Cases

### Demonstrated in the repository

- Synthetic legal proposition review with separate checks for citation validity, quotation fidelity, procedural fit, authority treatment, record support, and filing readiness.
- Local control-desk routing that preserves a baseline, records a bounded change, and retains `HOLD` when mandatory conditions remain unresolved.
- Replay-oriented comparison using canonical bytes and SHA-256 bindings.
- Environmental and clean-air dashboard concepts with observation events, threshold states, map views, and reviewer packets.
- Local macOS game interfaces and gameplay demonstrations with replay, accessibility, and persistence features shown in the associated artifacts.

### Potential integration scenarios

Subject to access to the applicable implementation and separate commercial terms, an organization could evaluate these patterns for controlled desktop workflows, audit-receipt generation, rule-gated review, replayable decision support, or human-authorized export. These are evaluation scenarios, not claims of existing deployment.

## Commercial and Integration Context

A practical evaluation can begin with a narrow workflow and explicit acceptance criteria:

1. Select one decision or release boundary.
2. Define the required inputs, control states, failure behavior, and audit outputs.
3. Agree on which results must be reproducible and under what environment and serialization conditions.
4. Run a scoped proof of concept with synthetic or appropriately governed data.
5. Review integration, security, deployment, and licensing requirements separately.

Commercial licensing and integration inquiries: [mark@groundeddi.ai](mailto:mark@groundeddi.ai).

## Authorship and Provenance

This repository contains versioned development records and provenance artifacts designed to preserve technical history and authorship traceability.

- Repository records identify **Grounded DI LLC** as the organization responsible for the published collection.
- The Local Control Desk implementation record identifies **Mark S. Weinstein** as creator and operator and distinguishes human-authored architecture from AI-assisted implementation.
- The public repository was created on July 29, 2026, and its commit history records subsequent additions and revisions.
- Individual artifacts carry their own dates, version identifiers, metadata, receipts, or hashes where available.
- The redacted report package includes both an external checksum list and an internal per-file manifest.

Repository timestamps, commit metadata, hashes, and internal records are useful provenance and integrity evidence. They do not, by themselves, establish legal ownership, inventorship, patent priority, or the truth of an artifact's substantive claims.

Recommended citation:

> Grounded DI LLC. (2026). *Grounded DI Desktop Builds* [Public evidence archive]. GitHub. https://github.com/Grounded-DI/GroundedDI-Desktop-Builds

## Intellectual Property

Copyright © 2026 Grounded DI LLC. Product names and project terminology are used for identification and attribution.

This repository does not currently include an open-source `LICENSE` file. Public availability should not be interpreted as an open-source license or permission to reuse confidential or proprietary implementation material. Patent status is not asserted in this README because the current repository contents do not provide filing records sufficient to support a specific public statement.

Private prompts, source archives, runtime packages, and internal governance materials are outside the public repository unless expressly included in a marked publication artifact.

## Status

**Public evidence archive / prototype documentation.** The collection supports artifact review, provenance analysis, and preliminary technical or commercial diligence. It is not an installable product distribution, complete source release, independent audit, certification, or statement of production readiness. The repository currently has no tagged releases.

## Contact and Collaboration

For technical evaluation, controlled demonstrations, integration discussions, or commercial licensing, contact [Grounded DI LLC](mailto:mark@groundeddi.ai). When inquiring, identify the artifact or workflow of interest and the acceptance criteria you need to evaluate.

---

#DeterministicAI #LocalFirst #AIValidation #Auditability #Replayability #LegalTech #DeveloperTools #GroundedDI
