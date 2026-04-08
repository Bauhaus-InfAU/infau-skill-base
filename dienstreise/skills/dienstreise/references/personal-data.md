# Persönliche Daten des Dienstreisenden — VORLAGE

Diese Datei ist eine **Vorlage**. Die tatsächlichen persönlichen Daten werden NICHT im Skill gespeichert, sondern im Arbeitsverzeichnis des Users (z.B. `00_Dienstreise/personal-data.md`).

## Warum separate Datei?

Dieser Skill soll von allen BUW-Beschäftigten nutzbar sein. Persönliche Daten gehören deshalb ins Arbeitsverzeichnis des jeweiligen Users, nicht in den Skill selbst.

## Wo sucht der Skill nach den Daten?

Der Skill sucht automatisch in dieser Reihenfolge:
1. Im **ausgewählten Workspace-Ordner** (z.B. `00_Dienstreise/personal-data.md`)
2. Im **übergeordneten Ordner** des aktuellen Reise-Ordners
3. Falls nicht gefunden: **User wird gefragt** und die Daten werden automatisch gespeichert

## Vorlage

```markdown
# Persönliche Daten des Dienstreisenden

## Grunddaten (DR-001, DR-004)
- **Name, Vorname**: [Nachname, Vorname]
- **Dienstort (lt. Vertrag)**: [z.B. Weimar]
- **Fakultät/Bereich**: [z.B. A+U/InfAU]
- **Telefon**: [Durchwahl]
- **Personalart**: [wissen./künstl. Personal | nicht-wiss. Personal | Beamte/r]

## Wohnanschrift (1a)
- **PLZ, Ort, Straße, Nr.**: [PLZ, Ort, Straße Nr.]

## Bankdaten (DR-004)
- **IBAN**: [IBAN]
- **BIC**: [BIC]

## Beförderungsmittel-Vorgaben
- **BahnCard**: [Ja (welche?) | Nein]
- **Deutschlandticket**: [Ja | Nein]

## Zusätzliche Daten (für Auslandsreisen, DR-012 Entsendung)
- **Uni-Email**: [vorname.nachname@uni-weimar.de]
- **Rentenversicherungsnummer**: [nur für Entsendung]
- **Krankenkasse**: [Name, Adresse — nur für Entsendung]
- **Beschäftigt bei BUW seit**: [Datum — nur für Entsendung]

## Arbeitgeber-Daten (für Entsendeanträge)
- **Arbeitgeber**: Bauhaus-Universität Weimar, Dezernat Personal, Belvederer Allee 6, 99425 Weimar
- **Betriebsnummer**: 06809750
- **Ansprechpartner**: Reisekostenstelle
- **Telefon**: +49 (0) 36 43 / 58 22 22
- **Email**: saskia.edvardsson@uni-weimar.de

## Änderungshistorie
- [DATUM]: Erstmalige Anlage
```

## Automatisches Speichern und Aktualisieren

Wenn der User zum ersten Mal persönliche Daten angibt, speichere sie automatisch in `personal-data.md` im Arbeitsverzeichnis und informiere den User. Bei zukünftigen Reisen diese Daten automatisch wiederverwenden — nicht erneut fragen.

Falls sich Daten ändern (neue Adresse, BahnCard erworben, etc.), aktualisiere die Datei und vermerke die Änderung in der Änderungshistorie mit Datum.
