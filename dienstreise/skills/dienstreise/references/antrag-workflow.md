# Phase 1: Dienstreiseantrag — Detaillierter Workflow

## Schritt 1: Kontext erfassen — EINE FRAGE NACH DER ANDEREN

**WICHTIG: Stelle immer nur EINE Frage pro Nachricht.** Warte auf die Antwort, bevor du die nächste Frage stellst. Biete bei jeder Frage konkrete Optionen oder Hilfe an.

Reihenfolge:

1. **Wohin?** — Frage nach Stadt/Ort. Wenn der User den Veranstaltungsnamen nennt, recherchiere Adresse und Details selbst.
2. **Warum?** — Frage nach Reisezweck. Biete Optionen: `Konferenz | Forschungstreffen | Fortbildung | Messe | Gremiensitzung | Sonstiges`
3. **Wann?** — Frage nach Reisedaten. Falls nur Veranstaltungszeitraum bekannt, schlage An-/Abreisezeiten vor basierend auf Zugverbindungen.
4. **Wie?** — Beförderungsmittel. Zeige Optionen mit Hinweisen:
   - Bahn (Standard, Deutschlandticket deckt Nahverkehr)
   - Privat-PKW (nur mit Begründung, 0,20-0,38 EUR/km)
   - Flug (nur über 1000 km erlaubt)
5. **Übernachtung?** — Hotel nötig? Biete Recherche an, nenne Städtekatalog-Limit.
6. **Sonstige Kosten?** — Tagungsgebühren, Eintritt, etc.
7. **Verpflegung gestellt?** — Sind Mahlzeiten in Teilnahmegebühr, Hotel oder Programm enthalten (Lunches, Conference Dinner, Frühstück)? Recherchiere das selbst am Programm und lass den User nur bestätigen. Treibt die Tagegeld-Kürzung in der Kalkulation.
8. **Tagegeld beanspruchen oder verzichten?** — Standardfall ist beanspruchen. Frage nur, wenn nicht offensichtlich: *„Möchtest du Tagegeld abrechnen (Regelfall) oder darauf verzichten?"* Bei Verzicht wird in DR-001 Nr. 11 die Verzichts-Checkbox gesetzt und in DR-003 `0` mit Vermerk eingetragen.

Wenn der User bei einem Punkt unsicher ist (z.B. "ich weiß nicht welches Hotel"), wechsle in den Recherche-Modus und hilf aktiv, statt einfach zur nächsten Frage zu springen.

Prüfe ob der User schon persönliche Daten hinterlegt hat. Suche nach `personal-data.md` im Workspace-Ordner (z.B. `00_Dienstreise/personal-data.md`), dann im übergeordneten Ordner. Falls nicht gefunden, frage den User und speichere die Daten automatisch in `personal-data.md` im Workspace-Ordner. Vorlage: `references/personal-data.md` im Skill-Verzeichnis.

## Schritt 2: Recherche-Assistent

Das ist das Herzstück von Phase 1 — du bist nicht nur Formularausfüller, sondern aktiver Recherche-Partner.

### Hotels recherchieren
1. Lies den **Städtekatalog** (`assets/formulare/Inland/Staedtekatalog_Inland_ab_01.01.2025.pdf`) und finde den maximalen Übernachtungsbetrag für die Zielstadt
2. Suche via WebSearch nach Hotels in der Nähe des Veranstaltungsorts, die unter dem Städtekatalog-Limit liegen
3. Präsentiere 2-3 Optionen mit Name, Preis, Entfernung zum Veranstaltungsort
4. Weise darauf hin: Hotelrechnung möglichst auf BUW ausstellen lassen!
5. Falls Kosten über Städtekatalog: Hinweis geben, dass höhere Kosten im Antrag vorab beantragt und begründet werden müssen

### Zugverbindungen recherchieren
1. Suche via WebSearch nach Zugverbindungen von Weimar/Erfurt zum Zielort
2. Berücksichtige: User hat Deutschlandticket (Nahverkehr kostenlos)
3. Gib Abfahrtszeiten und ungefähre ICE-Preise an (Sparpreis vs. Flexpreis)
4. Tipp: Sparpreise früh buchen, Fahrkarten über BUW-Bucher bestellen

### Veranstaltungsdetails
Wenn nur der Veranstaltungsname bekannt ist:
1. Suche nach offizieller Website
2. Finde: Adresse, Datum, Teilnahmegebühr, Programm
3. **Prüfe ob Verpflegung enthalten ist** — im Programm (Lunches, Coffee Breaks, Conference Dinner, Welcome Reception), in der Teilnahmegebühr, im Hotelangebot (Frühstück). Notiere pro Tag welche Mahlzeit gestellt wird. Das geht direkt in die Tagegeld-Kürzung der Kostenkalkulation (`references/tagegeld-kalkulation.md`) — nicht überspringen.

## Schritt 3: Ordnerstruktur anlegen

Erstelle im ausgewählten Workspace-Ordner folgende Struktur:
```
[NN_Stadt Veranstaltung]/
├── DR-001-dienstreiseantrag.pdf   (kopiert aus assets/formulare/)
├── DR-003-kostenkalkulation.xlsx  (kopiert aus assets/formulare/)
└── Belege/                        (leerer Ordner für spätere Belege)
```

Für Auslandsreisen zusätzlich:
```
├── DR-002-auslandsdienstreise.pdf
└── DR-012-entsendungsantrag.pdf   (wenn nötig)
```

Kopiere die Formulare aus `assets/formulare/` in den Reiseordner.

## Schritt 4: DR-001 ausfüllen

Der DR-001 ist ein ausfüllbares PDF. Verwende die Methode aus der PDF-Skill FORMS.md:

1. Prüfe die Formularfelder mit `check_fillable_fields.py`
2. Extrahiere Feldinfos mit dem pypdf-Ansatz (nicht `extract_form_field_info.py` — der hat einen Bug mit Choice-Feldern, umgehe ihn mit eigenem Skript)
3. Erstelle `field_values.json` und fülle das Formular

Welche Felder auszufüllen sind — siehe `references/form-fields-antrag.md`.

### Daten zusammenstellen

Aus den Recherche-Ergebnissen und User-Angaben berechne:
- **Reiseverlauf**: Abfahrt, Ankunft, Beginn/Ende Dienstgeschäft, Rückkehr
- **Beförderungsmittel**: Bahn/ÖPNV, Privat-Kfz, Flug etc.
- **Unterkunftskosten**: Preis pro Nacht, inkl. Frühstück ja/nein
- **Sonstige Kosten**: Teilnahmegebühren, Nebenkosten

## Schritt 5: DR-003 Kostenkalkulation ausfüllen

Die Kostenkalkulation ist eine Excel-Datei. Verwende den xlsx-Skill zum Bearbeiten.

> **Die Kalkulation muss vollständig sein.** Die Dez. Finanzen hat am 12.08.2026 ausdrücklich darauf hingewiesen, dass bei Inlandsdienstreisen regelmäßig das **Tagegeld** fehlt und die tatsächlichen Kosten die kalkulierten dadurch übersteigen. Eine leere Zeile ist kein „nicht zutreffend", sondern ein Fehler — jede bewusst leere Zeile dem User mit Begründung melden.

### Zeilen der Vorlage

| Zelle | Position | Was hinein gehört |
|-------|----------|-------------------|
| B4 / B5 / B6 | Kopf | Geschäftsort / Zeitraum / Reisender |
| Zeile 9 | Unterkunft | Anzahl Nächte × Preis, Erläuterung mit Hotelname und Städtekatalog-Bezug |
| **Zeile 10** | **Tagegeld** | **Pflichtfeld** — siehe unten |
| Zeile 11 | Bahn | Geschätzte ICE/IC-Kosten Hin- und Rückfahrt |
| Zeile 12 | Flug | Nur bei Flugreisen (über 1000 km, sonst begründen) |
| Zeile 13 | Öffent. Verkehrsmittel | Nahverkehr vor Ort, soweit nicht vom Deutschlandticket gedeckt |
| Zeile 15 | Privat PKW | km × Satz (0,20 / 0,38 EUR) |
| Zeile 18 | Teilnehmergebühr | Auch eintragen, wenn bereits bezahlt — Vermerk in Spalte B |
| Zeile 19 | Nebenkosten | Visa, Parkgebühren, Kurtaxe, Eintritt … |
| C21 | Gesamtsumme | Formel `=SUM(C9:C20)` beibehalten |

### Tagegeld (Zeile 10) — Pflichtposition

Vorgehen vollständig in `references/tagegeld-kalkulation.md`. Kurzfassung:

1. Tage aus dem Reiseverlauf ableiten: An-/Abreisetag je max. **14 EUR**, volle Zwischentage je **28 EUR**.
2. Gestellte Mahlzeiten aus der Recherche (Schritt 2) abziehen: Frühstück −5,60 / Mittag −11,20 / Abend −11,20 EUR, nie unter 0 EUR pro Tag.
3. **Tagesaufstellung als Tabelle zeigen und bestätigen lassen** (Format in `tagegeld-kalkulation.md`).
4. Betrag nach C10, nachvollziehbare Erläuterung nach B10 — z.B. `Anreise 14 € + 3 volle Tage à 28 € + Abreise 14 € = 112 €; abzgl. Verpflegung (4× Frühstück, 3× Mittag) −56 € = 56 €`.
5. **Nur bei Verzicht** `0` eintragen, mit Erläuterung `Verzicht auf Tagegeld (siehe DR-001 Nr. 11)` — und die Verzichts-Checkbox in DR-001 (`undefined_3`) setzen. Beides muss zusammenpassen.

Bei Auslandsreisen gelten die Ländersätze aus HENRI, nicht 14/28 (siehe `urls.md`).

### Vor der Übergabe: Kalkulation gegenprüfen

Gehe die Checkliste aus `references/tagegeld-kalkulation.md` („Vollständigkeitsprüfung vor der Übergabe") durch, bevor du dem User den Antrag als fertig meldest.

## Schritt 6: Übergabe an den User

Zeige zuerst eine kurze Zusammenfassung der Kalkulation (alle gefüllten Positionen + Gesamtsumme) und weise ausdrücklich auf die Tagegeld-Zeile hin. Erkläre dann die nächsten Schritte klar und konkret:

### Was der User jetzt tun muss:
1. **Ausdrucken und unterschreiben** — DR-001 (Nr. 16) und DR-003 ausdrucken und handschriftlich unterschreiben
2. **An Dekanat abgeben** — Beide Dokumente bei **Claudia Rehm** im Dekanat abgeben:
   - Geschwister-Scholl-Straße 8, 99423 Weimar
   - Tel.: +49 (0) 3643 583112
3. **Auf Genehmigung warten** — Der Antrag geht über:
   - Sichtvermerk Fachvorgesetzte*r (Nr. 17)
   - Mittelbewirtschafter*in bestätigt Haushaltsmittel (Nr. 18)
   - Genehmigung durch Dekan/Geschäftsführer (Nr. 20)
4. **Genehmigten Antrag per Email erhalten** — Seit 18.03.2026 sendet Claudia Rehm den genehmigten Antrag als Scan per Email zurück. **Diese Email gut aufheben — wird für die Abrechnung benötigt!**
5. Bei Auslandsreisen: Zusätzlich DR-002 und ggf. Entsendungsantrag einreichen

### Wichtige Hinweise:
- Bahntickets erst nach Genehmigung über die BUW-Bucher*innen bestellen!
- Bei Abschlag > 100 EUR: DR-005 mit Kopie des genehmigten Antrags per Email an Reisekostenabrechnung@uni-weimar.de
- Bei Fragen zum Antrag: Reisekostenstelle kontaktieren (Tel. 58 22 14 / 58 22 22)

### Email für Antrag-Einreichung an InfAU Office:

Speichere die Email als `Email-Antrag_[Nachname]_[JJJJ]_[Zielort].md` im Reiseordner. Format:

```markdown
# Email — Dienstreiseantrag [ORT], [DATUM_VON]–[DATUM_BIS]

**An:** caad@architektur.uni-weimar.de
**Betreff:** Dienstreiseantrag — [Nachname], [Vorname]; [DD.-DD.MM.YYYY]; [Ort]
**Anhänge:**
- DR-001-dienstreiseantrag_[Nachname]_[JJJJ]_[Zielort].pdf
- DR-003-anlage_kostenkalkulation_[Nachname]_[JJJJ]_[Zielort].xlsx

---

Liebe Franzi,

anbei mein Dienstreiseantrag für die Reise nach [ORT] vom [DATUM_VON] bis [DATUM_BIS] ([REISEZWECK]).

Bitte leite die Unterlagen ans Dekanat weiter.

Mit freundlichen Grüßen
[NAME]
```

### Email für Abschlag-Antrag (wenn zutreffend):

Speichere die Email als `Email-Abschlag_[Nachname]_[JJJJ]_[Zielort].md` im Reiseordner. Format:

```markdown
# Email — Abschlag-Antrag [ORT], [DATUM_VON]–[DATUM_BIS]

**An:** Reisekostenabrechnung@uni-weimar.de
**Betreff:** Abschlag — [Nachname], [Vorname]; [DD.-DD.MM.YYYY]; [Ort]; [Abrechnungsobjekt]
**Anhänge:**
- DR-005-reisekostenabschlag_antrag_[Nachname]_[JJJJ]_[Zielort].doc
- [genehmigter DR-001 Dateiname]

---

Sehr geehrte Damen und Herren,

hiermit beantrage ich einen Reisekostenabschlag für meine Dienstreise nach [ORT] vom [DATUM_VON] bis [DATUM_BIS].

Die voraussichtlichen Kosten belaufen sich auf [GESAMTKOSTEN] EUR. Ich beantrage einen Abschlag in Höhe von [80% der Kosten] EUR.

Anbei der genehmigte Dienstreiseantrag sowie der ausgefüllte Abschlag-Antrag (DR-005).

Mit freundlichen Grüßen
[NAME]
[FAKULTÄT/BEREICH]
```

Nach dem Speichern dem User jeweils den Pfad zur .md-Datei nennen, damit er sie zum Copy-Paste finden kann.
