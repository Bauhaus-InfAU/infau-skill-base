# DB-Rechnung mit Mehrwertsteuerausweis prüfen

## Warum das wichtig ist

Die Reisekostenstelle der BUW braucht für Bahnfahrten **die formale Rechnung mit Mehrwertsteuerausweis**, nicht nur das Online-Ticket. Die Rechnung wird für den Vorsteuerabzug der Universität benötigt — auf dem Online-Ticket fehlen die dafür nötigen Pflichtangaben (Rechnungsnummer, Aussteller-Adresse, Netto/Brutto/MwSt-Aufschlüsselung).

Folge bei fehlender Rechnung: Die Reisekostenstelle fordert sie nach (Email an die Dienstreisende:n), die Abrechnung verzögert sich. Dieser Fall trat z.B. am 2026-05-06 bei einer Abrechnung von M. Bielik auf (Email Saskia Edvardsson, Reisekostenstelle).

Der Skill soll diesen Fall **vor** der Email-Einreichung erkennen und den User warnen.

---

## Online-Ticket vs. Rechnung — Unterschied erkennen

Beim Buchen einer Bahnfahrt auf bahn.de bekommt man per Email **das Online-Ticket** (= die Fahrkarte für die Kontrolle). Das ist **nicht dasselbe** wie die Rechnung. Die Rechnung muss separat im Bahnkundenkonto unter "Meine Reisen" heruntergeladen werden.

### Indikatoren für eine **Rechnung mit MwSt-Ausweis** (das wollen wir!)

Mindestens drei dieser Merkmale müssen vorliegen:

- Wort **„Rechnung"** prominent im Dokumenttitel oder Kopfbereich (nicht nur in der Fußzeile als Verweis)
- **„Rechnungsnummer:"** oder **„Rechnungsnr.:"** mit eigener Nummer (verschieden von der Auftragsnummer)
- Vollständige Kunden-Anschrift (Name, Straße, PLZ, Ort)
- Explizite **MwSt-Zeile**: „MwSt. 7%" / „USt. 7%" / „Umsatzsteuer 7%" mit ausgewiesenem EUR-Betrag (Fernverkehr Inland 7% seit 2020, Nahverkehr 19%)
- **Netto- und Brutto-Beträge** getrennt ausgewiesen
- Aussteller: „DB Vertrieb GmbH" oder „DB Fernverkehr AG" mit voller Anschrift, Steuernummer / USt-IdNr.

### Indikatoren für ein **Online-Ticket ohne Rechnung** (das reicht NICHT!)

- Kopfzeile **„Online-Ticket"**, **„Ihre Fahrkarte"** oder **„Sparpreis-Ticket"**
- **Auftragsnummer** vorhanden, aber keine separate Rechnungsnummer
- **Aztec-Barcode** für die Kontrolle prominent platziert
- Sätze wie **„Diese Fahrkarte ist keine Rechnung"** oder **„Die Rechnung können Sie unter bahn.de in 'Meine Reisen' abrufen"**
- Pers. Daten beschränken sich auf Name + ggf. Geburtsdatum (Bahn-Kundennummer), keine vollständige Postadresse

### Edge Case

Manche aktuelle Online-Tickets enthalten am Fuß eine kurze MwSt-Zeile. Das **reicht der BUW-Reisekostenstelle in der Praxis nicht** — sie hat in dokumentierten Fällen (s. oben) die formale Rechnung nachgefordert. Daher: **Im Zweifel immer die Rechnung anfordern**, auch wenn das Online-Ticket eine MwSt-Angabe enthält.

---

## Ablauf im Skill

Beim Klassifizieren der Belege in Schritt 2 (siehe `abrechnung-workflow.md`) für **jede Bahn-PDF** zusätzlich klassifizieren:

- **Rechnung** ✓ — Mindestens 3 Rechnungs-Indikatoren erfüllt
- **Online-Ticket** ✗ — Online-Ticket-Indikatoren überwiegen oder „Diese Fahrkarte ist keine Rechnung" steht im Text

Dann in **Schritt 2a (DB-Rechnungsprüfung)** dem User eine Tabelle zeigen:

```
Bahn-Belege gefunden:

| # | Datei                       | Strecke         | Typ            |
|---|-----------------------------|-----------------|----------------|
| 1 | Ticket_ICE_1234.pdf         | Weimar→Köln     | Online-Ticket  |
| 2 | Ticket_ICE_5678.pdf         | Köln→Weimar     | Online-Ticket  |

⚠ Für 2 Bahnfahrten liegt nur das Online-Ticket vor, nicht die formale
Rechnung mit Mehrwertsteuerausweis. Die Reisekostenstelle braucht aber
die Rechnung (für den Vorsteuerabzug der Uni).
```

Falls mindestens ein Online-Ticket dabei ist → Anleitung zum Nachladen anbieten (siehe unten). Anschließend fragen, ob der User a) die Rechnungen jetzt nachlädt oder b) trotzdem weitermacht (Reisekostenstelle wird die Rechnung dann später nachfordern).

**Egal wie der User entscheidet → Workflow läuft weiter** (kein Block).

---

## Anleitung zum Nachladen aus bahn.de — User-Vorlage

Diese Anleitung ist die Standardantwort, wenn nur Online-Tickets gefunden wurden. Übersetze sie in die Sprache des Users.

```
So bekommst du die Rechnung mit MwSt-Ausweis aus dem Bahnkundenkonto:

1. Gehe auf https://www.bahn.de und logge dich in dein Bahnkundenkonto ein.
2. Klicke oben auf „Meine Reisen" (oder „Meine Buchungen").
3. Wähle die betroffene Reise aus der Liste aus (z.B. Weimar–Köln,
   24.03.2026).
4. Klicke auf „Rechnung herunterladen" / „Rechnung anzeigen"
   (manchmal heißt der Link auch „Quittung"). Eine PDF mit
   Rechnungsnummer und MwSt-Zeile wird erzeugt.
5. Speichere die PDF und ersetze damit das Online-Ticket im
   Belege-Ordner. (Den Dateinamen passe ich dann beim Umbenennen
   automatisch an.)

Wiederhole Schritt 3–5 für jede Fahrt, von der noch keine Rechnung da ist.

Sag mir Bescheid, wenn du fertig bist — dann lese ich die neuen
Belege ein und mache mit der Abrechnung weiter. Falls du die Rechnung
gerade nicht ziehen kannst, können wir auch ohne weitermachen — die
Reisekostenstelle wird sie aber dann per Email nachfordern.
```

---

## Pre-Flight-Reminder vor der Email (Schritt 6)

Falls in Schritt 2a Online-Tickets als „nicht Rechnung" markiert wurden und der User sich für „trotzdem weitermachen" entschieden hat: bei der Email-Vorbereitung (Schritt 6) noch einmal explizit erinnern:

```
⚠ Erinnerung: Bei den Bahn-Belegen sind aktuell nur Online-Tickets
beigefügt (keine formalen Rechnungen). Die Reisekostenstelle wird
voraussichtlich die Rechnung per Email nachfordern. Falls du sie
jetzt schon nachladen willst, sag Bescheid — dann pausieren wir
das Versenden.
```
