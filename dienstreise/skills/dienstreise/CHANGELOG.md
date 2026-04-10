# Changelog — Dienstreise-Assistent

Alle wesentlichen Änderungen am Skill werden hier dokumentiert. Format: [Semantic Versioning](https://semver.org/).

---

## [1.6.0] — 2026-04-10

### Neu
- **Erstnutzer-Onboarding**: Automatische Erkennung von Erstnutzern (kein `personal-data.md`). Zeigt eine verständliche Einführung in den gesamten Prozess, richtet den Dienstreise-Ordner ein, und erklärt was der Agent übernimmt vs. was der User tun muss.
- **Beleg-Umbenennung**: Belege werden bei der Abrechnung nach einheitlichem Schema umbenannt: `[NN]_[Kategorie]_[Beschreibung]_[Betrag]EUR.[ext]`. User muss die Umbenennung bestätigen. Schema dokumentiert in `references/beleg-naming.md`.
- **Versionierung & Statuszeile**: Bei jeder Aktivierung wird Version, letztes Update und Datum der letzten BUW-Regelwerk-Prüfung angezeigt.
- **Changelog**: Dieser Changelog — abrufbar wenn der User nach "was ist neu" oder der Version fragt.
- **Projekt-Ordnerstruktur**: Ein übergreifender Ordner (`Dienstreisen/`) sammelt alle Reisen. `personal-data.md` wird geteilt. Dokumentiert in `references/folder-convention.md`.

### Geändert
- Phase 2 (Abrechnung) hat jetzt 7 statt 6 Schritte (neuer Schritt 3: Belege umbenennen)
- `references/folder-convention.md` zeigt jetzt die Projekt-Ebene und die User-vs-Skill-Aufgabenteilung
- `references/abrechnung-workflow.md` enthält neuen Schritt 2b für Beleg-Umbenennung

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
