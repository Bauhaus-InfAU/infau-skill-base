# Ordnerstruktur-Konvention für Dienstreisen

## Projekt-Ordner (übergreifend)

Ein einzelner Ordner sammelt **alle** Dienstreisen eines Users. Der Ordner wird beim Erstnutzer-Onboarding eingerichtet (Standard: `Dienstreisen/`). Die Datei `personal-data.md` liegt auf dieser Ebene und wird von allen Reisen geteilt.

```
Dienstreisen/                             ← Projekt-Ordner (einmal pro User)
├── personal-data.md                      ← Persönliche Daten (einmalig, geteilt)
├── 01_Koeln DigitalBau/                  ← Erste Reise
│   └── ...
├── 02_Berlin BIM World/                  ← Zweite Reise
│   └── ...
└── 03_Muenchen Forschungstreffen/        ← Dritte Reise
    └── ...
```

## Struktur pro Reise

Jeder Reise-Unterordner wird vom Skill automatisch angelegt. Der User muss nur die Belege in den `Belege/`-Ordner legen — alles andere erstellt und füllt der Skill.

```
[NN]_[Zielort] [Veranstaltung]/
├── DR-001-dienstreiseantrag_Bielik_2026_Koeln.pdf  ← Ausgefüllter Antrag
├── DR_Antrag_Bewilligung.pdf             ← Gescannter bewilligter Antrag
├── DR-003-anlage_kostenkalkulation_Bielik_2026_Koeln.xlsx  ← Kostenkalkulation
├── DR-004-reisekostenrechnung_Bielik_2026_Koeln.pdf ← Ausgefüllte Abrechnung
├── Belege/
│   ├── 01_Bahn_Weimar-Koeln_74.49EUR.pdf
│   ├── 02_Bahn_Koeln-Weimar_101.49EUR.pdf
│   ├── 03_Hotel_PremierInn-Koeln-2N_111.87EUR.pdf
│   ├── 04_Konferenz_DigitalBau-Tagesticket_45.00EUR.pdf
│   └── 05_OEPNV_UBahn-Koeln_3.20EUR.pdf
└── Formulare/                            ← Optionaler Ordner mit Blanko-Formularen
    ├── Inland/
    │   └── Staedtekatalog_Inland_*.pdf
    └── Ausland/
        └── DR-002-dienstreise_ausland.pdf
```

## Was der User tun muss vs. was der Skill macht

| Wer | Was |
|-----|-----|
| **Skill** | Ordner anlegen, Formulare kopieren, Formulare ausfüllen, Belege umbenennen, Emails formulieren |
| **User** | Belege (PDFs) in den `Belege/`-Ordner legen, Antrag/Abrechnung unterschreiben, Email absenden, Originalbelege 5 Jahre aufbewahren |

## Namenskonventionen

- Ordnername: `[NN]_[Ort] [Veranstaltung]` — z.B. `01_Koln DigitalBau`, `02_Berlin BIM World`
- NN = laufende Nummer im Jahr
- Ausgefüllte Formulare: `[Formular]_[Nachname]_[JJJJ]_[Zielort].[ext]` — z.B. `DR-001-dienstreiseantrag_Bielik_2026_Koeln.pdf`
- Belege: `[NN]_[Kategorie]_[Beschreibung]_[Betrag]EUR.[ext]` — siehe `references/beleg-naming.md`

## Wie der Skill den Ordner erkennt

Der Skill sucht nach folgenden Hinweisen um zu erkennen wo der User im Prozess steht:

| Datei gefunden | Bedeutung |
|----------------|-----------|
| `DR_Antrag_Bewilligung.pdf` | Antrag genehmigt → Phase 2 (Abrechnung) anbieten |
| `Belege/` mit PDFs darin | Belege vorhanden → bereit für Abrechnung |
| `DR-001-dienstreiseantrag_*` | Antrag schon ausgefüllt, aber noch nicht genehmigt |
| Leerer Ordner | Neue Reise → Phase 1 (Antrag) starten |
| `Formulare/` Ordner | User hat Formulare lokal, können als Vorlagen genutzt werden |
