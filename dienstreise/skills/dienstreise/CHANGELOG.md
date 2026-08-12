# Changelog — Dienstreise-Assistent

Alle wesentlichen Änderungen am Skill werden hier dokumentiert. Format: [Semantic Versioning](https://semver.org/).

---

## [1.9.0] — 2026-08-12

### Neu
- **Tagegeld ist Pflichtposition in der Kostenkalkulation (DR-003)**: Auslöser ist die universitätsweite Email von Anna Scheer (Dez. Finanzen) vom 12.08.2026 — bei Inlandsdienstreisen fehlt regelmäßig die Tagegeld-Kalkulation, sodass die tatsächlichen Kosten die kalkulierten übersteigen. Der Skill behandelt Zeile 10 der DR-003 jetzt als Pflichtfeld mit genau zwei zulässigen Zuständen: berechneter Betrag mit Tagesaufstellung, oder `0` mit ausdrücklichem Verzichts-Vermerk.
- **Neue Referenzdatei**: `references/tagegeld-kalkulation.md` — Sätze (An-/Abreisetag max. 14 EUR, volle Tage 28 EUR), Kürzung bei gestellter Verpflegung (5,60 / 11,20 / 11,20 EUR, Untergrenze 0), Tagesaufstellung als Bestätigungstabelle, Format der Erläuterung in Spalte B, Verzichts-Pfad und Vollständigkeits-Checkliste für die gesamte Kalkulation.
- **Verpflegungs-Recherche in Phase 1**: Zwei neue Fragen in Schritt 1 (Verpflegung gestellt? / Tagegeld oder Verzicht?). Der Recherche-Schritt prüft aktiv Konferenzprogramm und Hotelangebot auf enthaltene Mahlzeiten und leitet daraus die Kürzung ab — bisher lief das erst in Phase 2 (Schritt 3a).
- **Vollständigkeitsprüfung vor der Übergabe**: Vor „Antrag fertig" geht der Skill die Kalkulation Zeile für Zeile durch und meldet jede bewusst leere Zeile mit Begründung. Zusammenfassung der Kalkulation inkl. Gesamtsumme wird dem User gezeigt.
- **Konsistenzprüfung DR-001 ↔ DR-003**: Verzichts-Checkbox Nr. 11 (`undefined_3`) und Tagegeld-Zeile der Kalkulation müssen dieselbe Aussage treffen. Dokumentiert in `references/form-fields-antrag.md`.

### Geändert
- `references/antrag-workflow.md`: Schritt 1 hat zwei zusätzliche Fragen; Schritt 2 (Veranstaltungsdetails) fordert die Verpflegungsrecherche explizit ein; Schritt 5 komplett überarbeitet mit Zeilentabelle der DR-003-Vorlage und Tagegeld-Pflichtblock; Schritt 6 beginnt mit der Kalkulationszusammenfassung.
- `references/rules.md`: neue Unterrubrik „Tagegeld muss auch in der Kostenkalkulation stehen (Pflicht)" plus Quellenhinweis.
- `SKILL.md`: Phase-1-Kurzübersicht auf 9 Fragen erweitert; Schritt 5 (Kostenkalkulation) mit Pflichtcharakter; zwei neue Fallstricke (#7 fehlendes Tagegeld, #8 veraltete HENRI-PDF), bisherige #7 (DB-Rechnung) ist jetzt #9; neue Zeile in „Wichtige Regeln".

### Bugfix
- **`plugin.json` hing auf 1.6.0 fest** — dadurch lief die installierte Plugin-Version weiter mit dem Stand von v1.6.0, und die Verbesserungen aus v1.7.0 (DB-Rechnungsprüfung) und v1.8.0 (Verpflegungs-Matrix, Email-MD-Dateien) kamen nie im Runtime an. `plugin.json` und der Eintrag in `marketplace.json` (stand auf 1.5.0) sind jetzt auf 1.9.0 gezogen und werden ab sofort bei jedem Release mitgepflegt.

### BUW-Regelwerk
- **Tagegeld-Beträge geklärt**: Die in `urls.md` verlinkte HENRI-Datei `Tagegeld__Verpflegungspauschalen_2020.pdf` ist ein TFM-Schreiben vom 19.12.2019 und nennt für das ThürRKG noch 12 / 24 EUR. Maßgeblich sind die vom Dez. Finanzen am 12.08.2026 bestätigten **14 / 28 EUR** — der Skill rechnet weiterhin damit. Widerspruch ist in `rules.md`, `urls.md` und Fallstrick #8 dokumentiert, damit er nicht erneut Verwirrung stiftet.
- Website-Prüfdatum unverändert (2026-04-10) — die Änderung beruht auf einer Email der Dez. Finanzen, nicht auf einer Aktualisierung der HENRI-Seite.

---

## [1.8.0] — 2026-05-06

### Neu
- **Verpflegungs-Abfrage in Phase 2 (neuer Schritt 3a)**: Pro Reisetag und pro Mahlzeit (Frühstück / Mittag / Abend) wird abgefragt, ob unentgeltliche Verpflegung bereitgestellt wurde — durch BUW oder Dritte (Hotel, Konferenz, …) — und in welcher Quelle (ÜK / TN-Gebühr / Flug / Sonstiges) sie enthalten war. Bisher wurde nur das Hotel-Frühstück gestreift; die Folge war, dass Section 4 von DR-004 unvollständig befüllt und die Tagegeld-Kürzungen (5,60 / 11,20 / 11,20 EUR) nicht sauber dokumentiert waren. Pre-Fills aus Belegen (z.B. Hotel mit Frühstück → automatisch Frühstück = Dritte/ÜK), Bestätigungstabelle vor dem Eintragen.
- **Feldmappings für Section 4 (Verpflegung)**: `references/form-fields-abrechnung.md` enthält jetzt die vollständige Tabelle mit allen 60 Checkbox-IDs (6 Zeilen × 10 Spalten) plus Datum-Textfelder und „Anlage 1 beigefügt"-Checkbox. Hinweis auf unregelmäßige Kid-Suffixe (`.0`, `.1`, …) und die robuste Alternative über X/Y-Koordinaten.
- **Email-Entwürfe als Markdown-Datei**: Antrag-, Abrechnung- und Abschlag-Emails werden zusätzlich als `Email-[Typ]_[Nachname]_[JJJJ]_[Zielort].md` im Reiseordner gespeichert. Format mit YAML-ähnlichem Header (An / CC / Betreff / Anhänge) plus Volltext, damit der User per Copy-Paste in seinen Mailclient übernehmen kann. Schema dokumentiert in `SKILL.md` Sektion „Digitale Einreichung".

### Geändert
- Phase 2 (Abrechnung) hat jetzt 9 Schritte (neuer Schritt 3a: Verpflegung).
- `references/abrechnung-workflow.md`: Schritt 3 verweist auf 3a; Schritt 4 (Tagegeld) erklärt die Kürzungs-Quelle; Schritt 5 (DR-004 ausfüllen) hat eigenen Block für Section 4; Schritt 6 zeigt das Email-MD-Format.
- `references/antrag-workflow.md`: Antrag- und Abschlag-Email werden im neuen MD-Format gespeichert.
- `SKILL.md`: Phase 2 Kurzübersicht Schritt 5 zeigt Verpflegung statt nur Frühstück.

### BUW-Regelwerk
- Geprüft am: 2026-04-10 — keine Änderung. Auslöser sind zwei Lücken im Skill-Workflow, nicht eine Regeländerung.

---

## [1.7.0] — 2026-05-06

### Neu
- **DB-Rechnungsprüfung**: Bei der Abrechnung erkennt der Skill, ob Bahn-Belege formale Rechnungen mit Mehrwertsteuerausweis sind oder nur Online-Tickets. Falls nur Online-Tickets vorliegen, wird der User gewarnt und bekommt eine Anleitung zum Nachladen aus dem Bahnkundenkonto („Meine Reisen" → Rechnung herunterladen). Hintergrund: Die Reisekostenstelle braucht die formale Rechnung für den Vorsteuerabzug — Online-Tickets allein führen zu Nachforderungen (dokumentierter Fall: Email Edvardsson, 2026-05-06).
- **Neue Referenzdatei**: `references/db-rechnung-pruefung.md` mit Erkennungskriterien (Rechnungsnummer, MwSt-Zeile, Brutto/Netto, Aussteller-Adresse vs. „Diese Fahrkarte ist keine Rechnung") und User-Vorlagen.

### Geändert
- Phase 2 (Abrechnung) hat jetzt 8 statt 7 Schritte (neuer Schritt 3: DB-Rechnung prüfen, dahinter um eins verschoben).
- `references/abrechnung-workflow.md`: neuer Schritt 2a (DB-Rechnungsprüfung) zwischen Schritt 2 und 2b; Pre-Flight-Reminder in Schritt 6, falls der User mit Online-Tickets statt Rechnungen weitergemacht hat.
- Neuer Fallstrick #7 in `SKILL.md` ("Bekannte Fallstricke").

### BUW-Regelwerk
- Geprüft am: 2026-04-10 — keine Regeländerung; Anpassung erfolgt aufgrund einer Rückfrage der Reisekostenstelle.

---

## [1.6.0] — 2026-04-10

### Neu
- **Erstnutzer-Onboarding**: Automatische Erkennung von Erstnutzern (kein `personal-data.md`). Zeigt eine verständliche Einführung in den gesamten Prozess, richtet den Dienstreise-Ordner ein, und erklärt was der Agent übernimmt vs. was der User tun muss.
- **Beleg-Umbenennung**: Belege werden bei der Abrechnung nach einheitlichem Schema umbenannt: `[NN]_[Kategorie]_[Beschreibung]_[Betrag]EUR.[ext]`. User muss die Umbenennung bestätigen. Schema dokumentiert in `references/beleg-naming.md`.
- **Versionierung & Statuszeile**: Bei jeder Aktivierung wird Version, letztes Update und Datum der letzten BUW-Regelwerk-Prüfung angezeigt.
- **Changelog**: Dieser Changelog — abrufbar wenn der User nach "was ist neu" oder der Version fragt.
- **Projekt-Ordnerstruktur**: Ein übergreifender Ordner (`Dienstreisen/`) sammelt alle Reisen. `personal-data.md` wird geteilt. Dokumentiert in `references/folder-convention.md`.
- **Formular-Benennung**: Ausgefüllte Formulare werden nach Schema `[Formular]_[Nachname]_[JJJJ]_[Zielort].[ext]` benannt (z.B. `DR-001-dienstreiseantrag_Bielik_2026_Koeln.pdf`). Ersetzt das alte `-ausgefuellt`-Suffix.

### Bugfix
- **K29 war falsch als "Deutschlandticket Ja" dokumentiert** — K29 ist tatsächlich die Anlage-Checkbox "Auslandsdienstreise". Bei Inlandsreisen mit Deutschlandticket wurde fälschlich das Feld "Anlage zum Antrag auf Finanzierung einer Auslandsdienstreise" angekreuzt. Fix: Deutschlandticket nutzt K28 + Nein_7, K29/K30 gehören zur Anlage-Sektion.
- **Anlage-Checkboxen vollständig dokumentiert** — Alle 7 Anlage-Checkboxen (K29-K35 auf Seite 1, K58-K64 auf Seite 2) sind jetzt mit korrekter Zuordnung dokumentiert: Auslandsdienstreise, Fahrauftrag, Vergleichsangebote, Abschlag, Einladung, Entsendungsantrag, Kostenkalkulation.

### Geändert
- Phase 2 (Abrechnung) hat jetzt 7 statt 6 Schritte (neuer Schritt 3: Belege umbenennen)
- `references/folder-convention.md` zeigt jetzt die Projekt-Ebene und die User-vs-Skill-Aufgabenteilung
- `references/abrechnung-workflow.md` enthält neuen Schritt 2b für Beleg-Umbenennung
- BahnCard/Deutschlandticket-Sektion in `references/form-fields-antrag.md` korrigiert (nur K27, K28, Nein_6, Nein_7)

### BUW-Regelwerk
- Geprüft am: 2026-04-10 — keine Änderungen gegenüber v1.5.0

---

## [1.5.0] — 2026-03-26

### Neu
- Dienstreiseantrag wird über InfAU Office (Franziska Schuchort) eingereicht statt direkt ans Dekanat
- Interaktionsregeln: Step-by-step geführte Interaktion, immer nur eine Frage pro Nachricht
- Lokale Asset-Tabelle — Formulare werden aus dem Skill-Verzeichnis kopiert statt heruntergeladen
- Sprachregel: Antwortsprache folgt dem User, nicht dem Skill-Dokument
- Explizite Referenz auf `references/kontakte-und-ablauf.md` für Einreichungswege

### BUW-Regelwerk
- Digitale Einreichung seit 18.03.2026 (Email statt Papier)
- Originalbelege: 5 Jahre Aufbewahrungspflicht durch Dienstreisende

---

## [1.4.0] — 2026-03-18

### Neu
- Digitale Einreichung: Kompletter Prozess auf Email umgestellt (Reisekostenabrechnung@uni-weimar.de)
- Email-Entwürfe werden vom Skill komplett vorformuliert
- Hinweis auf 5-Jahres-Aufbewahrungspflicht für Originalbelege

---

## [1.3.0] — 2026-03-01

### Neu
- Checkbox-Bugfixes dokumentiert (Lessons Learned Abschnitt)
- Korrekte Zuordnung der Unterkunft-Checkboxen (K7-K12) basierend auf Koordinaten-Analyse
- Anlage-Checkboxen auf beiden PDF-Seiten setzen (K35 + K64)

---

## [1.2.0] — 2026-02-15

### Neu
- DR-004 Reisekostenrechnung: Automatisches Ausfüllen via pypdf
- Formularfeld-Referenz: `references/form-fields-abrechnung.md`

---

## [1.1.0] — 2026-01-20

### Neu
- DR-001 Dienstreiseantrag: Automatisches Ausfüllen via pypdf
- DR-003 Kostenkalkulation: Automatisches Ausfüllen
- Formularfeld-Referenz: `references/form-fields-antrag.md`
- Hotel- und Zugrecherche via WebSearch

---

## [1.0.0] — 2025-12-01

### Initial Release
- Grundstruktur: Phase 1 (Antrag) und Phase 2 (Abrechnung)
- Ordnerstruktur-Konvention
- Regelwerk-Referenz (`references/rules.md`)
- Kontakte und Ablauf (`references/kontakte-und-ablauf.md`)
- Formular-URLs (`references/urls.md`)
- Personal-data.md Template
