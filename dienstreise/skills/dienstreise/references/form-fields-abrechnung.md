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
| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Nein_6` | checkbox (/On) | Keine unentgeltliche Verpflegung |
| `Ja wenn ja bitte Tabelle ausfüllen...` | checkbox (/On) | Unentgeltl. Verpflegung erhalten |

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
