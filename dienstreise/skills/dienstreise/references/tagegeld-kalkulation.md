# Tagegeld in der Kostenkalkulation (DR-003)

> **Anlass**: Email Anna Scheer (Dez. Finanzen), 12.08.2026 — „Berechnung von Tagegeld – Kostenkalkulation Inlandsdienstreisen". Bei Inlandsdienstreisen fehlt in der Kostenkalkulation regelmäßig das Tagegeld. Folge: die kalkulierten Kosten liegen unter den tatsächlichen, die Mittelplanung der Bereiche stimmt nicht. Zitat: *„Gerade in Zeiten von knappen Mitteln ist es wichtig, unsere Kalkulationen so exakt wie möglich zu machen."*

## Grundregel

**Die Zeile „Tagegeld" in DR-003 darf niemals leer bleiben.** Es gibt genau zwei zulässige Zustände:

| Fall | Zeile C10 (Betrag) | Zeile B10 (Erläuterung) | DR-001 Nr. 11 |
|------|--------------------|--------------------------|---------------|
| Tagegeld wird beansprucht (Regelfall) | berechneter Betrag | Tagesaufstellung (siehe unten) | Verzicht-Checkbox **nicht** setzen |
| Auf Tagegeld wird verzichtet | `0` | `Verzicht auf Tagegeld (siehe DR-001 Nr. 11)` | `undefined_3` = `/On` |

Frage den User aktiv, welcher der beiden Fälle gilt — nicht stillschweigend annehmen. Der Verzicht ist die Ausnahme.

## Sätze Inland

| Reisetag | Ansatz in der Kalkulation |
|----------|---------------------------|
| Anreisetag | max. **14 EUR** |
| voller Zwischentag (über 24h Abwesenheit) | **28 EUR** |
| Abreisetag | max. **14 EUR** |
| eintägige Reise, Abwesenheit unter 14h | **0 EUR** |
| eintägige Reise, Abwesenheit 14–24h | **14 EUR** |

Bei **Aus- und Fortbildungsreisen** (§15 ThürRKG) gelten die reduzierten Sätze 10,50 / 21,00 EUR — siehe `rules.md`.

**Ausland**: Die länderspezifischen Tabellen stehen in HENRI (siehe `urls.md`). Nicht mit den Inlandssätzen kalkulieren.

## Kürzung bei bereitgestellter Verpflegung

Werden Mahlzeiten unentgeltlich bereitgestellt — durch Veranstalter*in, Hotel (Frühstück in der Übernachtung enthalten), BUW oder eine andere Einheit — reduziert sich das Tagegeld **schon in der Kalkulation**:

| Mahlzeit | Kürzung (Anteil vom vollen Tagessatz 28 EUR) |
|----------|----------------------------------------------|
| Frühstück | 20 % = **5,60 EUR** |
| Mittagessen | 40 % = **11,20 EUR** |
| Abendessen | 40 % = **11,20 EUR** |

Wichtig:
- Die Kürzung bemisst sich immer am **vollen** Tagessatz (28 EUR), auch an An-/Abreisetagen mit 14 EUR Ansatz.
- Das Tagegeld eines Tages kann dadurch auf **0 EUR** sinken, wird aber **nie negativ**. Bei 0 abschneiden.
- Frühstück im Hotel zählt nur, wenn die Rechnung **auf die BUW** ausgestellt ist (siehe `rules.md`). Auf Privatadresse ausgestellte Hotelrechnungen lösen keine Kürzung aus.
- In der Kalkulationsphase sind das Schätzungen. Lieber die Kürzung ansetzen, wenn das Konferenzprogramm Catering ankündigt — die exakte Feststellung passiert in Phase 2 (`abrechnung-workflow.md` Schritt 3a).

## Ablauf im Antrag

1. **Reisezeiten festlegen** — kalendarischer Beginn (Abfahrt Wohnung) bis Ende (Rückkehr Wohnung). Die Tage kommen aus dem DR-001 Reiseverlauf, nicht aus dem Veranstaltungszeitraum.
2. **Verpflegung recherchieren** — Konferenz-/Veranstaltungswebsite prüfen: Ist Catering in der Teilnahmegebühr enthalten (Lunches, Conference Dinner, Coffee Breaks)? Hotelangebot: Frühstück inklusive? Das ist Teil des Recherche-Auftrags in `antrag-workflow.md` Schritt 2.
3. **Tagesaufstellung bauen** (siehe Beispiel unten) und dem User zur Bestätigung zeigen.
4. **In DR-003 eintragen** — Betrag nach C10, Aufstellung nach B10.
5. **Mit DR-001 abgleichen** — Verpflegungs-Checkboxen (Nr. 11) und ggf. `Tagungspauschale enthält Verpflegung` (Nr. 10) müssen dieselbe Aussage treffen wie die Kalkulation.

## Tagesaufstellung — Format

Zeige dem User vor dem Eintragen diese Tabelle und lass sie bestätigen:

```
Tagegeld-Kalkulation — bitte bestätigen:

| Datum      | Art        | Ansatz  | Verpflegung gestellt   | Kürzung  | Tagegeld |
|------------|------------|---------|------------------------|----------|----------|
| 08.09.2026 | Anreise    | 14,00 € | —                      |  0,00 €  | 14,00 €  |
| 09.09.2026 | voller Tag | 28,00 € | Frühstück, Mittag      | 16,80 €  | 11,20 €  |
| 10.09.2026 | voller Tag | 28,00 € | Frühstück, Mittag      | 16,80 €  | 11,20 €  |
| 11.09.2026 | voller Tag | 28,00 € | Frühstück, Mittag      | 16,80 €  | 11,20 €  |
| 12.09.2026 | Abreise    | 14,00 € | Frühstück              |  5,60 €  |  8,40 €  |
|            |            |         |                        | Summe    | 56,00 €  |

Stimmt das so? (Ja → in DR-003 eintragen / Korrektur → was ändern?)
```

## Eintrag in DR-003

| Zelle | Inhalt |
|-------|--------|
| `C10` | Summe als Zahl, z.B. `56` — oder als nachvollziehbare Formel, z.B. `=14+3*11.2+8.4` |
| `B10` | Kurzform der Aufstellung, z.B. `Anreise 14 € + 3 volle Tage à 28 € + Abreise 14 € = 112 €; abzgl. Verpflegung (4× Frühstück, 3× Mittag) −56 € = 56 €` |

Die Erläuterung in B10 ist Pflicht — die Prüfstelle muss die Zahl nachvollziehen können. Eine bloße Zahl ohne Herleitung ist genau das, was in der Email vom 12.08.2026 bemängelt wurde.

## Vollständigkeitsprüfung vor der Übergabe

Bevor du dem User sagt „Antrag fertig", prüfe die Kostenkalkulation Zeile für Zeile:

- [ ] `Tagegeld` (Zeile 10) gefüllt — Betrag **und** Erläuterung, oder explizit `0` mit Verzicht-Vermerk
- [ ] `Unterkunft` (Zeile 9) mit Anzahl Nächte in der Erläuterung
- [ ] Fahrtkosten in der passenden Zeile (Bahn / Flug / ÖPNV / PKW), nicht unter „sonstiges"
- [ ] `Teilnehmergebühr` (Zeile 18), falls vorhanden — auch wenn bereits bezahlt
- [ ] Kopfdaten: Geschäftsort, Zeitraum, Reisender
- [ ] Gesamtsumme (C21) rechnet sich plausibel
- [ ] Kalkulierte Summe ≥ realistisch erwartbare Ist-Kosten — bei knapper Kalkulation den User warnen

Melde dem User jede Zeile, die du bewusst leer lässt, mit Begründung. Stillschweigend leere Zeilen sind der eigentliche Fehler.
