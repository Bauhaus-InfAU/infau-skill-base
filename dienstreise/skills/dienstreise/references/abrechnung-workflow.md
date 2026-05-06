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
- **Verpflegung** — Eigener Klärungsblock, siehe Schritt 3a (immer durchlaufen, treibt Section 4 von DR-004 und die Tagegeld-Kürzungen)

### Bei Abweichungen fragen:
- **Andere Reisezeiten?** — Wenn Belege andere Zeiten zeigen als der Antrag
- **Zusätzliche Kosten?** — Kosten die nicht im Antrag kalkuliert waren
- **Fehlende Belege?** — Wenn für bewilligte Positionen kein Beleg vorliegt

## Schritt 3a: Verpflegung pro Tag und Mahlzeit

Section 4 von DR-004 verlangt für **jeden Reisetag** eine Matrix: pro Mahlzeit (Frühstück / Mittag / Abend) ist anzugeben, ob sie unentgeltlich bereitgestellt wurde — und falls ja, durch wen (BUW oder Dritte) und in welcher Quelle (ÜK / TN-Gebühr / Flug / Sonstiges) sie enthalten war. Diese Angaben treiben **direkt die Tagegeld-Kürzungen** (Frühstück 5,60 EUR / Mittag 11,20 EUR / Abend 11,20 EUR — siehe `references/rules.md`). Daher: immer durchgehen, auch wenn der User intuitiv sagt „Verpflegung war keine".

### Ablauf

1. **Pre-Fills aus den Belegen ableiten:**
   - **Hotelrechnung mit „inkl. Frühstück" auf BUW-Adresse** → Frühstück für jede Hotelnacht als „Dritte / ÜK" vormerken (das Hotel = Dritter; die Mahlzeit war in den Übernachtungskosten enthalten). Beispiel: Hotel-Check-in 21.04. → 21.04. + 22.04. Frühstück.
   - **Hotelrechnung auf Privatadresse** → Frühstück gilt **nicht** als auf Arbeitgeberveranlassung — nicht eintragen (Quelle: `rules.md`).
   - **Tagungsticket / Konferenzprogramm** mit Catering → entsprechende Mahlzeiten als „Dritte / TN-geb" vormerken.
   - **Flug mit Bordverpflegung in TN-fähiger Klasse** → Mahlzeit als „Dritte / Flug" vormerken (in der Praxis selten relevant für Inland).

2. **Pro Reisetag** (vom kalendarischen Beginn bis Ende laut tatsächlichen Reisezeiten) den User fragen, falls aus den Belegen nicht eindeutig:
   - „An [Datum] — wurden Mittag- oder Abendessen unentgeltlich bereitgestellt? Wenn ja: durch BUW oder durch Dritte (Hotel/Konferenz/…), und in welcher Quelle enthalten (ÜK / TN-Gebühr / Flug / Sonstiges)?"
   - **Eine Frage pro Nachricht** gilt auch hier — pro Tag eine Frage, nicht alle auf einmal.

3. **Bestätigungstabelle zeigen** (analog zum Beleg-Umbenennungs-Pattern in Schritt 2b):

   ```
   Verpflegungs-Übersicht — bitte bestätigen:

   | Datum      | Frühstück       | Mittag    | Abend     | Quelle |
   |------------|-----------------|-----------|-----------|--------|
   | 21.04.2026 | Dritte (Hotel)  | —         | —         | ÜK     |
   | 22.04.2026 | Dritte (Hotel)  | —         | —         | ÜK     |

   Stimmt das so? (Ja → DR-004 ausfüllen / Korrektur → was ändern?)
   ```

4. **Erst nach Bestätigung** in Schritt 5 die Daten ins DR-004 eintragen.

5. **Bei > 6 Reisetagen**: DR-006 (Anlage Verpflegung) aus `assets/formulare/DR-006-rkr_anlage_verpflegung.pdf` in den Reiseordner kopieren, weitere Tage dort eintragen, und in DR-004 die Checkbox `Anlage 1 beigefügt` setzen.

### Wenn keine Verpflegung unentgeltlich bereitgestellt wurde

User-Bestätigung „keine" → in Schritt 5 nur `Nein_6` ankreuzen, Tabelle bleibt leer. Trotzdem den Punkt in der Bestätigung explizit zeigen, damit der User die Aussage bewusst trifft (Tagegeld-Konsequenz).

## Schritt 4: Tagegeld berechnen

Anhand der tatsächlichen Reisezeiten:
1. Berechne die Abwesenheitsdauer (Beginn der Reise ab Wohnung bis Ende der Reise an Wohnung)
2. Wende die Tagegeld-Tabelle an (siehe `rules.md`)
3. Für An-/Abreisetage: Berechne Stunden separat
4. Kürze bei unentgeltlichen Mahlzeiten auf Arbeitgeberveranlassung — Eingaben kommen direkt aus **Schritt 3a** (Frühstück −5,60 EUR / Mittag −11,20 EUR / Abend −11,20 EUR vom vollen Tagessatz)

Die finale Berechnung macht die Reisekostenstelle — der Skill trägt nur die Verpflegungs-Matrix in Section 4 von DR-004 (Schritt 5) sowie die Reisezeiten ein. Die Korrektheit der Mahlzeitenangaben ist entscheidend, weil die Reisekostenstelle daraus die Kürzungen ermittelt.

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
| Verpflegung Section 4 | **Verpflegungs-Matrix aus Schritt 3a** (siehe unten) |
| Bahnkosten | Summe aller Bahntickets |
| Nebenkosten | Messe-Tickets, sonstige Belege |
| IBAN/BIC | personal-data.md |

### Section 4 (Verpflegung) ausfüllen

Aus der in Schritt 3a bestätigten Verpflegungs-Matrix:

- **Keine unentgeltliche Verpflegung** (User hat „keine" bestätigt) → nur `Nein_6` (=`/On`) ankreuzen, Tabelle leer lassen.
- **Unentgeltliche Verpflegung vorhanden** → `Ja wenn ja bitte Tabelle ausfüllen…` (=`/On`) ankreuzen plus pro Reisetag eine Tabellenzeile (Datum-Textfeld + die zutreffenden Mahlzeiten- und Quelle-Checkboxen, alle =`/Ja`).
- **> 6 Reisetage** → zusätzlich `Anlage 1 beigefügt` (=`/On`) ankreuzen, DR-006 aus `assets/formulare/` in den Reiseordner kopieren und befüllen.

Die exakten Feld-IDs pro Zeile/Spalte stehen in `references/form-fields-abrechnung.md` unter „Verpflegung (Sektion 4)". Die Suffixe (`.0`, `.1`, …) sind nicht zeilenweise sortiert — Tabelle dort konsultieren oder per X/Y-Koordinate adressieren.

## Schritt 6: Email formulieren und nächste Schritte erklären

Erstelle eine **komplett fertige Email**, die der User nur noch absenden muss. Verwende die konkreten Daten aus der Abrechnung.

**An:** Reisekostenabrechnung@uni-weimar.de
**Betreff:** `[Nachname], [Vorname]; [DD.-DD.MM.YYYY]; [Ort]; [Abrechnungsobjekt]`

Beispiel: `Name, Vorname; 24.-25.03.2026; Geschäftsort; Abrechnungsobjekt`

**Anhänge** (als PDF):
1. Ausgefüllte Reisekostenrechnung (DR-004) — unterschrieben
2. Genehmigter Dienstreiseantrag (DR-001) — den Scan vom Dekanat
3. Alle Belege als PDF
4. Falls > 6 Reisetage: Anlage 1 Verpflegung (DR-006)

### Email als Markdown-Datei speichern

Speichere die fertige Email zusätzlich als `Email-Abrechnung_[Nachname]_[JJJJ]_[Zielort].md` im Reiseordner. Der User kann den Inhalt von dort per Copy-Paste in den Mailclient übernehmen.

Format der .md-Datei (mit eingesetzten Werten):

```markdown
# Email — Reisekostenabrechnung [ORT], [DATUM_VON]–[DATUM_BIS]

**An:** Reisekostenabrechnung@uni-weimar.de
**Betreff:** [Nachname], [Vorname]; [DD.-DD.MM.YYYY]; [Ort]; [Abrechnungsobjekt]
**Anhänge:**
- DR-004-reisekostenrechnung_[Nachname]_[JJJJ]_[Zielort].pdf
- [genehmigter DR-001 Dateiname]
- Belege/[Beleg 1 Dateiname]
- Belege/[Beleg 2 Dateiname]
- …

---

Sehr geehrte Damen und Herren,

anbei übersende ich Ihnen meine Reisekostenabrechnung für die Dienstreise nach [ORT] vom [DATUM_VON] bis [DATUM_BIS].

Beigefügt sind:
- Reisekostenrechnung (DR-004)
- Genehmigter Dienstreiseantrag (DR-001)
- [ANZAHL] Belege:
  - [Beleg 1: z.B. "DB-Fahrkarte Weimar–Köln, 74,49 EUR"]
  - [Beleg 2: z.B. "DB-Fahrkarte Köln–Weimar, 101,49 EUR"]
  - [Beleg 3: z.B. "Hotelrechnung Premier Inn Köln, 111,87 EUR"]
  - [weitere…]

Mit freundlichen Grüßen
[Name]
[Fakultät/Bereich]
Tel. [Telefon]
```

Nach dem Speichern dem User den Pfad zur `Email-Abrechnung_…md` nennen.

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
