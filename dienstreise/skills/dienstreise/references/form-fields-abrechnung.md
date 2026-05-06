# Feldmappings DR-004 Reisekostenrechnung

Das PDF DR-004 hat ausfüllbare Formularfelder. Diese Datei dokumentiert die Feld-IDs und ihre Zuordnung.

Hinweis: Die Checkbox-Werte in DR-004 sind GEMISCHT — manche verwenden `/On`+`/Off`, andere `/Ja`. Immer den tatsächlichen `checked_value` aus dem Formular verwenden! Die sicherste Methode ist, die Felder per pypdf zu extrahieren und die States zu prüfen.

## Seite 1

### Kopfbereich — BUW-Vorauszahlungen
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Inland` | checkbox (/On) | Ankreuzen bei Inlandsreise |
| `Ausland` | checkbox (/Ja) | Ankreuzen bei Auslandsreise |
| `Dienstreise` | checkbox (/On) | Ankreuzen bei Dienstreise |
| `Kontrollkästchen2` | checkbox (/Ja) | Aus- und Fortbildung |
| `Teilnahmegebühr` | checkbox (/On) | BUW hat Teilnahmegebühr bezahlt |
| `Unterkunftskosten` | checkbox (/On) | BUW hat Unterkunft bezahlt |
| `Bahntickets` | checkbox (/On) | BUW hat Bahntickets bezahlt |
| `Flugkosten` | checkbox (/On) | BUW hat Flug bezahlt |
| `sonstige Kosten` | checkbox (/On) | BUW hat sonstige Kosten bezahlt |
| `Text1` | text | Text zu sonstigen Kosten / Erläuterung |

### Grunddaten
| Feld-ID | Typ | Beschreibung | Beispielwert |
|---------|-----|-------------|-------------|
| `DRNr` | text | Dienstreise-Nummer | `97/26` |
| `AbrechnungsNr` | text | Von Reisekostenstelle — LEER lassen | |
| `Name Vorname` | text | Name, Vorname | `<aus personal-data.md>` |
| `FakultätLehrstuhl Bereich Hauspost` | text | Fakultät/Bereich | `<aus personal-data.md>` |
| `Telefon` | text | Telefonnummer | `<aus personal-data.md>` |
| `1a Wohnort Anschrift  Wohnort von dem aus regelm der Dienstantritt erfolgt` | text | Wohnanschrift | `<aus personal-data.md>` |
| `1b Familienwohnort Anschrift` | text | Familienwohnort (wenn abweichend) | |
| `1c vorübergehender Aufenthaltsort Anschrift` | text | Vorübergehender Aufenthaltsort | |
| `auswärtiger Geschäftsort Anschrift` | text | Geschäftsort | `<Geschäftsort Adresse>` |

### BahnCard / Deutschlandticket (y ≈ 550-560)
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Kontrollkästchen5` | checkbox (/Ja) | Ja, BC-Art |
| `Text59` | text | BC-Art (z.B. "BC50") |
| `Kontrollkästchen6` | checkbox (/Ja) | Nein (keine BahnCard) |
| `Kontrollkästchen10` | checkbox (/Ja) | Ja, Deutschlandticket |
| `Kontrollkästchen11` | checkbox (/Ja) | Nein (kein Deutschlandticket) |

### IBAN / BIC
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Text8` | text | IBAN |
| `Text9` | text | BIC |

### Abschlag / Pauschale
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Ja in Höhe von` | checkbox (/On) | Abschlag erhalten Ja |
| `EUR` | text | Abschlag-Betrag |
| `Nein_3` | checkbox (/On) | Abschlag Nein |
| `Ja in Höhe von_2` | checkbox (/On) | Pauschale erhalten Ja |
| `EUR_2` | text | Pauschale-Betrag |
| `Nein_4` | checkbox (/On) | Pauschale Nein |

### Reiseverlauf (Sektion 2)
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Kontrollkästchen12` | checkbox (/Ja) | a) Beginn ab Wohnort/Aufenthaltsort |
| `Dropdown14` | choice | Welcher Wohnort (1a/1b/1c) |
| `Kontrollkästchen13` | checkbox (/Ja) | a) Beginn ab Dienstort |
| `nach bei mehreren Geschäftsorten...` | text | Reiseziel |
| `mit Beförderungsmittel` | text | Beförderungsmittel Hinreise |
| `am Datuma...` | text | Datum Reisebeginn |
| `um Uhra...` | text | Uhrzeit Reisebeginn |
| `am Datumb Ankunft am Geschäftsort` | text | Datum Ankunft |
| `um Uhrb Ankunft am Geschäftsort` | text | Uhrzeit Ankunft |
| `mit Beförderungsmittel_2` | text | Beförderungsmittel am Geschäftsort |
| `am Datumc...` | text | Datum Beginn Dienstgeschäft |
| `um Uhrc...` | text | Uhrzeit Beginn Dienstgeschäft |
| `am Datumd Ende des Dienstgeschäftes` | text | Datum Ende Dienstgeschäft |
| `um Uhrd Ende des Dienstgeschäftes` | text | Uhrzeit Ende Dienstgeschäft |
| `mit Beförderungsmittel_3` | text | Beförderungsmittel Rückreise |
| `am Datume...` | text | Datum Abfahrt Geschäftsort |
| `um Uhre...` | text | Uhrzeit Abfahrt Geschäftsort |
| `Kontrollkästchen15` | checkbox (/Ja) | f) Ende an Wohnort/Aufenthaltsort |
| `Dropdown17` | choice | Welcher Wohnort (1a/1b/1c) |
| `Kontrollkästchen16` | checkbox (/Ja) | f) Ende an Dienstort |
| `am Datumf...` | text | Datum Reiseende |
| `um Uhrf...` | text | Uhrzeit Reiseende |

### Unterkunftskosten (Sektion 3)
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `des Amtes wegen bezahlt von` | checkbox (/On) | Unterkunft des Amtes wegen bereitgestellt |
| `undefined_4` | text | Bezahlt von (Name) |
| `aus privaten Gründen` | checkbox (/On) | Private Übernachtung genutzt |
| `Text18` | text | Anzahl Nächte (Übernachtungspauschale) |
| `Betrag` | text | ÜK-Eigenanteil in EUR |
| `Frühstück` | text | Anzahl enthaltener Frühstücke |
| `Mittagessen` | text | Anzahl enthaltener Mittagessen |
| `Abendessen` | text | Anzahl enthaltener Abendessen |
| `Kontrollkästchen21` | checkbox (/Ja) | Zimmer alleine genutzt: Ja |
| `Kontrollkästchen22` | checkbox (/Ja) | Zimmer alleine genutzt: Nein |
| `Kontrollkästchen19` | checkbox (/Ja) | Telefon/Internet dienstl. erforderlich: Ja |
| `Kontrollkästchen20` | checkbox (/Ja) | Telefon/Internet dienstl. erforderlich: Nein |

### Verpflegung (Sektion 4)

**Übersichts-Checkboxen** (Y ≈ 174.7):

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Nein_6` | checkbox (/On) | Keine unentgeltliche Verpflegung erhalten |
| `Ja wenn ja bitte Tabelle ausfüllen ggf Anlage 1 zur Reisekostenrechnung Nr 5 nutzen` | checkbox (/On) | Unentgeltl. Verpflegung erhalten — Tabelle ausfüllen |
| `Anlage 1 beigefügt` | checkbox (/On) | DR-006 Anlage Verpflegung beigefügt (bei > 6 Reisetagen nutzen) |

**Tabelle (6 Zeilen × 10 Checkboxen + Datum-Textfeld pro Zeile)** — alle Checkboxen verwenden `/Ja` als checked_value:

| Zeile | Datum (Tx) | F-BUW | F-Dritte | M-BUW | M-Dritte | A-BUW | A-Dritte | ÜK | TN-geb | Flug | Sonstiges |
|-------|------------|-------|----------|-------|----------|-------|----------|----|----|------|-----------|
| 1 | `Zeitraum Datum amvonbisRow1` | `Kontrollkästchen35` | `Kontrollkästchen41.0` | `Kontrollkästchen42.0` | `Kontrollkästchen43.0` | `Kontrollkästchen44.0` | `Kontrollkästchen45.0` | `Kontrollkästchen46.0` | `Kontrollkästchen47.0` | `Kontrollkästchen48.0` | `Kontrollkästchen49.0` |
| 2 | `Zeitraum Datum amvonbisRow2` | `Kontrollkästchen36` | `Kontrollkästchen41.3` | `Kontrollkästchen42.3` | `Kontrollkästchen43.3` | `Kontrollkästchen44.2` | `Kontrollkästchen45.2` | `Kontrollkästchen46.2` | `Kontrollkästchen47.2` | `Kontrollkästchen48.2` | `Kontrollkästchen49.2` |
| 3 | `Zeitraum Datum amvonbisRow3` | `Kontrollkästchen37` | `Kontrollkästchen41.5` | `Kontrollkästchen42.5` | `Kontrollkästchen43.5` | `Kontrollkästchen44.5` | `Kontrollkästchen45.5` | `Kontrollkästchen46.5` | `Kontrollkästchen47.5` | `Kontrollkästchen48.5` | `Kontrollkästchen49.5` |
| 4 | `Zeitraum Datum amvonbisRow4` | `Kontrollkästchen38` | `Kontrollkästchen41.1` | `Kontrollkästchen42.1` | `Kontrollkästchen43.1` | `Kontrollkästchen44.1` | `Kontrollkästchen45.1` | `Kontrollkästchen46.1` | `Kontrollkästchen47.1` | `Kontrollkästchen48.1` | `Kontrollkästchen49.1` |
| 5 | `Zeitraum Datum amvonbisRow5` | `Kontrollkästchen39` | `Kontrollkästchen41.2` | `Kontrollkästchen42.2` | `Kontrollkästchen43.4` | `Kontrollkästchen44.3` | `Kontrollkästchen45.3` | `Kontrollkästchen46.3` | `Kontrollkästchen47.3` | `Kontrollkästchen48.3` | `Kontrollkästchen49.3` |
| 6 | `Zeitraum Datum amvonbisRow6` | `Kontrollkästchen40` | `Kontrollkästchen41.4` | `Kontrollkästchen42.4` | `Kontrollkästchen43.2` | `Kontrollkästchen44.4` | `Kontrollkästchen45.4` | `Kontrollkästchen46.4` | `Kontrollkästchen47.4` | `Kontrollkästchen48.4` | `Kontrollkästchen49.4` |

Spaltenbedeutung:
- **F/M/A-BUW**: Frühstück / Mittag / Abend wurde durch die **BUW** unentgeltlich bereitgestellt (BUW hat direkt bezahlt)
- **F/M/A-Dritte**: Frühstück / Mittag / Abend wurde durch **Dritte** unentgeltlich bereitgestellt (z.B. Hotel im Rahmen der ÜK, Konferenz im Rahmen der TN-Gebühr, Caterer, etc.)
- **ÜK / TN-geb / Flug / Sonstiges**: Quelle der unentgeltlichen Mahlzeit — wo war sie enthalten?

> **Achtung — unregelmäßige Kid-Nummerierung**: Die Suffixe (`.0`, `.1`, `.2`, …) hinter dem `Kontrollkästchen41…49`-Präfix sind **nicht** zeilenweise sortiert (das PDF /Kids-Array ist intern unsortiert). Die obige Tabelle zeigt das tatsächliche Mapping. Spalten F-BUW (Erstspalte) sind als eigenständige Felder `Kontrollkästchen35..40` realisiert — eine pro Zeile.
>
> **Robuste Alternative**: Statt namen-basiert zu adressieren, kann die Implementierung die Page-Annotations iterieren und die Verpflegungs-Checkboxen über Y-Band (Zeile) und X-Band (Spalte) zuordnen. Y-Bänder: Z1 ≈ 127, Z2 ≈ 114, Z3 ≈ 102, Z4 ≈ 89, Z5 ≈ 76, Z6 ≈ 64. X-Bänder: F-BUW ≈ 182.5, F-Dritte ≈ 231.6, M-BUW ≈ 277.6, M-Dritte ≈ 320.1, A-BUW ≈ 359.5, A-Dritte ≈ 394.5, ÜK ≈ 430.1, TN-geb ≈ 465.5, Flug ≈ 500.9, Sonstiges ≈ 539.8.

## Seite 2

### Fahrkosten (Sektion 5)
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Bahn` | text | Bahnkosten in EUR |
| `Flug` | text | Flugkosten in EUR |
| `ÖVM` | text | ÖPNV-Kosten |
| `Mietrad` | text | Mietrad-Kosten |
| `Kosten Mietwagen` | text | Mietwagen-Kosten |
| `Kosten Taxi` | text | Taxi-Kosten |

### Nebenkosten (Sektion 8)
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Art der NK` | text | Beschreibung der Nebenkosten |
| `Höhe` | text | Betrag in EUR |

### Unterschrift
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Ort Datum` | text | Ort, Datum der Erklärung |
| `Text56` | text | Name Fußzeile Seite 2 |
| `Text58` | text | Name Fußzeile Seite 1 |
| `Text57` | text | Name Fußzeile Seite 3 |

## Hinweise zum Ausfüllen

1. **Checkbox-Werte mischen**: `/On` und `/Ja` kommen beide vor. IMMER den `checked_value` aus dem Formular extrahieren.
2. **Dropdown-Felder**: `Dropdown14` und `Dropdown17` akzeptieren die Werte `' '`, `'1a)'`, `'1b)'`, `'1c)'`.
3. **Bug-Workaround**: Das Skript `extract_form_field_info.py` hat einen Bug mit Choice-Feldern. Verwende stattdessen direktes pypdf zum Extrahieren der Felder.
4. **Reisekostenstelle-Felder**: Alles mit "Reisekostenstelle" im Namen NICHT ausfüllen.
5. **NeedAppearances**: Nach dem Füllen `writer.set_need_appearances_writer(True)` setzen, damit die Werte in PDF-Viewern korrekt angezeigt werden.
