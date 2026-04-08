# Ordnerstruktur-Konvention für Dienstreisen

## Empfohlene Struktur pro Reise

```
[NN]_[Zielort] [Veranstaltung]/
├── DR-001-dienstreiseantrag.pdf          ← Leeres Formular (wird ausgefüllt)
├── DR-001-dienstreiseantrag-ausgefuellt.pdf  ← Ausgefüllter Antrag
├── DR_Antrag_Bewilligung.pdf             ← Gescannter bewilligter Antrag
├── DR-003-anlage_kostenkalkulation.xlsx  ← Kostenkalkulation
├── DR-004-reisekostenrechnung.pdf        ← Leeres Formular
├── DR-004-reisekostenrechnung-ausgefuellt.pdf ← Ausgefüllte Abrechnung
├── Belege/
│   ├── [Bahntickets].pdf
│   ├── [Hotelrechnung].pdf
│   ├── [Konferenztickets].pdf
│   └── [Sonstige Belege].pdf
└── Formulare/                            ← Optionaler Ordner mit Blanko-Formularen
    ├── Inland/
    │   └── Staedtekatalog_Inland_*.pdf
    └── Ausland/
        └── DR-002-dienstreise_ausland.pdf
```

## Namenskonventionen

- Ordnername: `[NN]_[Ort] [Veranstaltung]` — z.B. `01_Koln DigitalBau`, `02_Berlin BIM World`
- NN = laufende Nummer im Jahr
- Ausgefüllte Formulare: Originaldateiname + `-ausgefuellt` Suffix

## Wie der Skill den Ordner erkennt

Der Skill sucht nach folgenden Hinweisen um zu erkennen wo der User im Prozess steht:

| Datei gefunden | Bedeutung |
|----------------|-----------|
| `DR_Antrag_Bewilligung.pdf` | Antrag genehmigt → Phase 2 (Abrechnung) anbieten |
| `Belege/` mit PDFs darin | Belege vorhanden → bereit für Abrechnung |
| `DR-001-*ausgefuellt*` | Antrag schon ausgefüllt, aber noch nicht genehmigt |
| Leerer Ordner | Neue Reise → Phase 1 (Antrag) starten |
| `Formulare/` Ordner | User hat Formulare lokal, können als Vorlagen genutzt werden |
