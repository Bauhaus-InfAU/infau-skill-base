# Phase 2: Reisekostenabrechnung — Detaillierter Workflow

## Schritt 1: Bewilligten Antrag lesen

Suche im Workspace-Ordner nach dem genehmigten Dienstreiseantrag. Typische Dateinamen:
- `DR_Antrag_Bewilligung.pdf`
- `DR-001-dienstreiseantrag*.pdf` (mit Stempeln/Unterschriften)
- Jedes PDF das auf Seite 2 einen Genehmigungsstempel hat

Extrahiere daraus:
- DR-Nr.
- Name, Vorname, Fakultät, Telefon, Adresse
- Reiseziel (komplette Anschrift)
- Reiseverlauf (Datum/Uhrzeit Beginn/Ende)
- Beförderungsmittel
- Unterkunftskosten (bewilligter Betrag, inkl. Frühstück ja/nein)
- Sonstige Kosten (Teilnahmegebühren etc.)
- Ob höhere ÜK genehmigt wurden
- Deutschlandticket/BahnCard vorhanden

## Schritt 2: Belege einlesen

Suche im `Belege/`-Unterordner nach allen PDF-Dateien. Lies jede und klassifiziere:

### Bahntickets (DB Online-Tickets)
Erkennbar an: "Online-Ticket", "ICE Fahrkarte", "Sparpreis", "Super Sparpreis"
Extrahiere: Preis, Strecke (von→nach), Datum, Zugbindung, Klasse
Achtung: Abschnitte die "nicht gültig" sind (z.B. Weimar→Erfurt bei Deutschlandticket) werden NICHT erstattet

**Zusätzlich klassifizieren — Rechnung oder Online-Ticket?**
Für jede Bahn-PDF prüfen, ob es die formale Rechnung mit Mehrwertsteuerausweis ist oder nur das Online-Ticket. Kriterien und Ablauf in `references/db-rechnung-pruefung.md`. Das Ergebnis (`Rechnung` ✓ oder `Online-Ticket` ✗) wird in Schritt 2a dem User vorgelegt.

### Hotelrechnungen
Erkennbar an: "Check-in", "Check-out", "Booking", Hotel-Name
Extrahiere: Gesamtpreis, Anzahl Nächte, Frühstück enthalten ja/nein
Wichtig: Prüfe ob Rechnung auf BUW oder Privatadresse ausgestellt ist!

### Messe-/Konferenztickets
Erkennbar an: "Tagesticket", "Teilnehmergebühr", Rechnungsnummer
Extrahiere: Einzelpreis, Anzahl, Gesamtpreis

### Sonstige Belege
ÖPNV-Tickets, Taxi-Quittungen, Parkgebühren etc.

## Schritt 2a: DB-Rechnungsprüfung

**Nur wenn mindestens ein Bahn-Beleg vorliegt.** Vollständige Kriterien in `references/db-rechnung-pruefung.md`.

**Ablauf:**

1. Zeige dem User eine Tabelle aller Bahn-Belege mit Klassifikation (`Rechnung` ✓ / `Online-Ticket` ✗):

   ```
   Bahn-Belege gefunden:

   | # | Datei                | Strecke      | Typ            |
   |---|----------------------|--------------|----------------|
   | 1 | Ticket_ICE_1234.pdf  | Weimar→Köln  | Online-Ticket  |
   | 2 | Ticket_ICE_5678.pdf  | Köln→Weimar  | Rechnung       |
   ```

2. Falls **alle** Bahn-Belege bereits Rechnungen sind → kurz bestätigen, weiter mit Schritt 2b.

3. Falls **mindestens ein Online-Ticket** dabei ist:
   - Warne den User explizit: Die Reisekostenstelle braucht die formale Rechnung mit Mehrwertsteuerausweis (für den Vorsteuerabzug der Uni). Online-Tickets allein führen zu Nachforderungen.
   - Zeige die bahn.de-Anleitung aus `references/db-rechnung-pruefung.md` (übersetzt in die Sprache des Users).
   - Frage den User: **(a) Rechnungen jetzt nachladen** (Workflow pausiert, bis User die neuen PDFs in `Belege/` ablegt) oder **(b) Trotzdem weitermachen** (Skill merkt sich die fehlenden Rechnungen und erinnert in Schritt 6 noch einmal).

4. **Workflow läuft in beiden Fällen weiter** — kein Hard-Block. Bei (a) erst nach Bestätigung des Users, dass die neuen PDFs abgelegt sind, Schritt 2 für die geänderten Belege wiederholen.

5. Merke dir intern, ob in der finalen Belegliste noch Online-Tickets ohne Rechnung enthalten sind → für den Pre-Flight-Reminder in Schritt 6.

## Schritt 2b: Belege einheitlich umbenennen

Nach dem Einlesen und Klassifizieren werden die Belegdateien nach einem einheitlichen Schema umbenannt. Das Schema und der genaue Ablauf sind in `references/beleg-naming.md` beschrieben.

**Ablauf:**
1. Belege klassifizieren (bereits in Schritt 2 geschehen)
2. Neuen Dateinamen nach Schema ableiten
3. Tabelle mit Zuordnung `alter Name → neuer Name` dem User zeigen
4. **Erst nach expliziter Bestätigung umbenennen!**
5. Dateien im `Belege/`-Ordner umbenennen

## Schritt 3: Abweichungen und Klärung

Vergleiche die tatsächlichen Belege mit dem bewilligten Antrag. Stelle per AskUserQuestion Klärungsfragen:

### Immer fragen:
- **Selbst bezahlt vs. BUW?** — Für jeden größeren Posten (Bahn, Hotel, Tickets)
- **IBAN/BIC** — Wenn nicht in personal-data.md hinterlegt
- **Frühstück im Hotel?** — Nur fragen wenn nicht eindeutig aus dem Beleg ersichtlich

### Bei Abweichungen fragen:
- **Andere Reisezeiten?** — Wenn Belege andere Zeiten zeigen als der Antrag
- **Zusätzliche Kosten?** — Kosten die nicht im Antrag kalkuliert waren
- **Fehlende Belege?** — Wenn für bewilligte Positionen kein Beleg vorliegt

## Schritt 4: Tagegeld berechnen

Anhand der tatsächlichen Reisezeiten:
1. Berechne die Abwesenheitsdauer (Beginn der Reise ab Wohnung bis Ende der Reise an Wohnung)
2. Wende die Tagegeld-Tabelle an (siehe rules.md)
3. Für An-/Abreisetage: Berechne Stunden separat
4. Kürze bei unentgeltlichen Mahlzeiten auf Arbeitgeberveranlassung

Das Tagegeld wird von der Reisekostenstelle berechnet — nicht in DR-004 eintragen. Aber die Angaben zu Mahlzeiten und Reisezeiten müssen korrekt sein, da sie die Berechnung bestimmen.

## Schritt 5: DR-004 ausfüllen

Der DR-004 ist ein ausfüllbares PDF. Verwende die Methode aus der PDF-Skill:

1. Kopiere DR-004 aus `assets/formulare/` in den Reiseordner (falls nicht schon vorhanden)
2. Prüfe Formularfelder
3. Extrahiere Feldinfos (siehe `references/form-fields-abrechnung.md`)
4. Erstelle `field_values.json` mit allen Werten
5. Fülle das PDF aus
6. Verifiziere visuell (PDF→Bilder→Ausschnitte prüfen)

### Wichtige Felder und ihre Quellen:

| Feld | Quelle |
|------|--------|
| Persönliche Daten | personal-data.md oder DR-Antrag |
| DR-Nr. | Aus bewilligtem Antrag |
| Reiseverlauf | Tatsächliche Zeiten aus Belegen (Tickets) |
| Übernachtungskosten | Hotelrechnung |
| Frühstück/Mahlzeiten | Hotelrechnung + User-Angabe |
| Bahnkosten | Summe aller Bahntickets |
| Nebenkosten | Messe-Tickets, sonstige Belege |
| IBAN/BIC | personal-data.md |

## Schritt 6: Email formulieren und nächste Schritte erklären

Erstelle eine **komplett fertige Email**, die der User nur noch absenden muss. Verwende die konkreten Daten aus der Abrechnung:

**An:** Reisekostenabrechnung@uni-weimar.de
**Betreff:** `[Nachname], [Vorname]; [DD.-DD.MM.YYYY]; [Ort]; [Abrechnungsobjekt]`

Beispiel: `Name, Vorname; 24.-25.03.2026; Geschäftsort; Abrechnungsobjekt`

**Anhänge** (als PDF):
1. Ausgefüllte Reisekostenrechnung (DR-004) — unterschrieben
2. Genehmigter Dienstreiseantrag (DR-001) — den Scan vom Dekanat
3. Alle Belege als PDF

**Email-Text** (mit eingesetzten Werten!):
```
Sehr geehrte Damen und Herren,

anbei übersende ich Ihnen meine Reisekostenabrechnung für die Dienstreise nach [ORT] vom [DATUM_VON] bis [DATUM_BIS].

Beigefügt sind:
- Reisekostenrechnung (DR-004)
- Genehmigter Dienstreiseantrag (DR-001)
- [ANZAHL] Belege:
  - [Beleg 1: z.B. "DB-Fahrkarte Weimar–Köln, 74,49 EUR"]
  - [Beleg 2: z.B. "DB-Fahrkarte Köln–Weimar, 101,49 EUR"]
  - [Beleg 3: z.B. "Hotelrechnung Premier Inn Köln, 111,87 EUR"]
  - [weitere...]

Mit freundlichen Grüßen
[Name]
[Fakultät/Bereich]
Tel. [Telefon]
```

### Pre-Flight-Reminder bei fehlenden Bahn-Rechnungen

Falls in Schritt 2a Online-Tickets als „nicht Rechnung" markiert wurden und der User sich für *Trotzdem weitermachen* entschieden hat: vor dem Versenden noch einmal explizit erinnern (Vorlage in `references/db-rechnung-pruefung.md`). Andernfalls diesen Block überspringen.

### Nächste Schritte — dem User klar mitteilen:

1. **DR-004 unterschreiben** — Ausdrucken, unterschreiben, einscannen (oder digital signieren)
2. **Email absenden** — Den vorbereiteten Email-Entwurf mit allen Anhängen senden
3. **Originalbelege 5 Jahre aufbewahren!** — Seit 18.03.2026 liegt die Aufbewahrungspflicht bei den Dienstreisenden selbst. Belege müssen nach Aufforderung der Reisekostenstelle vorgelegt werden können.
4. **Frist beachten**: Abrechnung muss innerhalb von **3 Monaten nach Reiseende** eingereicht werden (Ausschlussfrist!)
5. Die Reisekostenstelle prüft und berechnet den finalen Erstattungsbetrag

### Bei Fragen oder Problemen:
- **Reisekostenstelle**: Tel. +49 (0) 36 43 / 58 22 14 oder 58 22 22
- **Email**: Reisekostenabrechnung@uni-weimar.de
- **Bei Fragen zum digitalen Prozess**: Beate Haltmeyer-Forstner (beate.haltmeyer-forstner@uni-weimar.de)
