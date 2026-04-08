---
description: Guide through BUW business travel — request (DR-001), cost calculation (DR-003), or settlement (DR-004)
argument-hint: "[antrag|abrechnung]"
---

# /dienstreise - Dienstreise-Assistent

Begleitet BUW-Beschäftigte durch den gesamten Dienstreise-Prozess: vom Antrag über die Kostenkalkulation bis zur Reisekostenrechnung.

## Usage

```
/dienstreise                Start — the assistant determines your current phase
/dienstreise antrag         Jump to Phase 1: plan a new trip (DR-001 + DR-003)
/dienstreise abrechnung     Jump to Phase 2: settle a completed trip (DR-004)
```

## Workflow

Invoke the `dienstreise` skill to process `$ARGUMENTS`.

The skill works in two phases:

1. **Antrag (before the trip)** — Capture trip details, research hotels & trains, create folder structure, fill DR-001 and DR-003
2. **Abrechnung (after the trip)** — Read receipts, calculate per diem, fill DR-004, draft submission email

## Examples

**Plan a new business trip:**
```
/dienstreise antrag
```
Claude will ask where you're going, search for hotels and train connections, create the folder structure, and fill out DR-001 + DR-003.

**Settle a completed trip:**
```
/dienstreise abrechnung
```
Claude will read your receipts from the Belege/ folder, calculate Tagegeld, fill DR-004, and draft the email to Reisekostenabrechnung@uni-weimar.de.
