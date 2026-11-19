# Grounded DI OS Arcade — native spot-check evidence

**Date:** 2026-11-19 · **Publisher:** Grounded DI LLC · **Source:** supplied local Arcade screenshot evidence ZIP.

This page records a bounded native-app verification session. It is **not** a release announcement, a full acceptance test, a security certification, or proof that every game is playable end-to-end.

## Identified artifact

- Application: Grounded DI OS Arcade Local
- Installed app version: **0.1.2 (build 3)**
- Bundle identifier: `com.groundeddi.osarcade.local`
- Recorded installer ZIP SHA-256: `322837992726c744c5f4a3fcecaa5dfe4ef79430525eee4098a80ab295af7d6a`
- Recorded embedded v8 ZIP SHA-256: `497999a7cd1fbc680ff139a7398b4eee10ff078ccc9aaf5f7a87935768022e23`

The source receipt reports strict signature verification and equality of 71 installed files with the pinned installer. **This GitHub documentation update did not independently rerun those installation checks.**

## Native spot-check matrix

| Area | Reported result | Exact scope and limitation |
| --- | --- | --- |
| Installed app launch | PASS | Native wrapper opened via loopback and showed 14 Arcade entries |
| Echo Vault keyboard round | PASS | One completed round: prompt 2, input 2, ROUNDS 1 / BEST 1 |
| Arcade Home | PASS | Shift–Command–H returned to lobby; native View → Home also provided route |
| Finder editing | PASS, scoped | Search field accepted test, select-all, and paste; Copy/Cut/Undo were not separately checked |
| Native quit/relaunch | PASS | Native Quit menu used, process listener stopped, app reopened; earlier Command–Q attempt was inconclusive |
| Persistence | PASS | Echo best 1 and recent-game history persisted after relaunch |
| PAGE TWO wrapper and story checkpoint | PASS, scoped | Chapter One mounted; full-page Continue · 1/6 appeared |
| PAGE TWO active progression | **UNVERIFIED** | Story paused overlay remained; viewport/document visibility not measured, no defect conclusion |
| Seaside launch | PASS | Game world and 0/60, 0:00 displayed |
| Seaside movement/completion | **UNVERIFIED** | Arrow-key probe did not establish movement or completion |
| Native backup export | PASS | Save dialog and 781-byte JSON export; receipt records four groups and Echo best 1 |
| Backup import preview | PASS, scoped | Open dialog inspected export; 0 missing groups, 4 existing groups preserved; **no restore write performed** |
| Screen reader, audio, all campaigns/routes | **UNVERIFIED** | Out of scope |

## Source image integrity

The submitted ZIP has seven original PNG captures; its ZIP CRC test passed and **all seven image sizes and SHA-256 values match the included manifest** when checked against the uploaded archive. See [image hash index](SCREENSHOT_HASH_INDEX.md).

**Publication boundary:** The PNG image bytes and full local installer are **not included in this GitHub commit**. This is a public text-and-hash record only. The original screenshots should not be represented as downloadable from this repository until the actual image files are separately uploaded.

The receipt also identifies a real local backup outside the screenshot ZIP (SHA-256 `0785ba4c5aed536462734fac1af612e0aa304d7b5d3e3c42dd63f97a9db3bec1`); that backup is not published.

## Interpretation

A successful screenshot, hash check, or single-round interaction supports only the identified observation. It does not verify long-form gameplay, accessibility, private runtime source, installer redistribution rights, or global deterministic behavior.

**No source code, executable, private backup, local absolute path, or runtime capsule is published here.**
