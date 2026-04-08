# DR-001 Dienstreiseantrag — Formularfelder

Alle Felder aus der ausfüllbaren PDF `assets/formulare/DR-001-dienstreiseantrag.pdf`.

**Checkbox-Werte**: DR-001 hat zwei Arten von Checkboxen:
- Felder mit Namen wie "Antrag auf...", "wissenkünstl Personal" etc. → checked_value = `/On`
- Felder mit Namen wie "Kontrollkästchen1", "Kontrollkästchen2" etc. → checked_value = `/Ja`
- Beide verwenden `/Off` als unchecked_value

**Dropdown-Felder**: `Dropdown5` und `Dropdown6` → Optionen: `[' ', '1a)', '1b)', '1c)']`

---

## Seite 1

### Kopfbereich — Art des Antrags

| Feld-ID | Typ | Beschreibung | Checked Value |
|---------|-----|-------------|---------------|
| `Kontrollkästchen1` | Btn | ☑ Dienstreise (Hauptkästchen links) | `/Ja` |
| `Antrag auf Ausbzw Fortbildung` | Btn | ☑ Aus-/Fortbildungsreise | `/On` |

> **Logik**: Für normale Dienstreisen `Kontrollkästchen1` = `/Ja`. Für Aus-/Fortbildungsreisen zusätzlich `Antrag auf Ausbzw Fortbildung` = `/On`.

### Kopfbereich — Personalart

| Feld-ID | Typ | Beschreibung | Checked Value |
|---------|-----|-------------|---------------|
| `Kontrollkästchen2` | Btn | ☑ wissen./künstl. Personal (linkes Kästchen) | `/Ja` |
| `wissenkünstl Personal` | Btn | ☑ wissen./künstl. Personal (rechtes Kästchen) | `/On` |
| `Kontrollkästchen3` | Btn | ☑ nicht-wiss. Personal (linkes Kästchen) | `/Ja` |
| `nicht wissen Personal` | Btn | ☑ nicht-wiss. Personal (rechtes Kästchen) | `/On` |
| `Kontrollkästchen4` | Btn | ☑ Beamte/r | `/Ja` |

> **Hinweis**: Es gibt jeweils ein linkes (Kontrollkästchen) und rechtes Kästchen pro Personalart. Beide setzen! Beispiel für wiss./künstl. Personal → `Kontrollkästchen2` = `/Ja` UND `wissenkünstl Personal` = `/On`.

### Kopfbereich — Nummern

| Feld-ID | Typ | Beschreibung | Auto-Fill |
|---------|-----|-------------|-----------|
| `DRNr` | Text | DR-Nummer (wird von Reisekostenstelle vergeben) | leer lassen |
| `AbrechnungsNr` | Text | Abrechnungs-Nr. (wird von Reisekostenstelle vergeben) | leer lassen |

### Nr. 1 — Persönliche Daten

| Feld-ID | Typ | Beschreibung | Quelle personal-data.md |
|---------|-----|-------------|------------------------|
| `1 Reisender Antragstellerin Name Vorname` | Text | Name, Vorname | aus personal-data.md |
| `Dienstort ltVertrag` | Text | Dienstort lt. Vertrag | aus personal-data.md |
| `Fakultät Bereich` | Text | Fakultät/Bereich | aus personal-data.md |
| `Telefon` | Text | Telefon | aus personal-data.md |

### Nr. 1a/1b/1c — Adressen

| Feld-ID | Typ | Beschreibung | Quelle personal-data.md |
|---------|-----|-------------|------------------------|
| `1a Wohnort PLZ Ort Straße Nr...` | Text | Wohnort (PLZ, Ort, Straße) | aus personal-data.md |
| `1b Familienwohnort PLZ Ort Straße Nr` | Text | Familienwohnort (wenn abweichend) | meist leer |
| `1c vorübergeh Aufenthaltsort zB Urlaubsort PLZ Ort Straße Nr` | Text | Vorübergehender Aufenthaltsort | nur bei Urlaub/Privatreise |

### Nr. 2 — Mitreisende

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `ja eintragen unter Nr 13 alle Teilnehmer...` | Btn | ☑ Ja, Mitreisende (→ unter Nr. 13 auflisten) | `/On` |

### Nr. 3 — Reiseziel

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `3 Reiseziel komplette Anschrift` | Text | Vollständige Adresse des Reiseziels |

### Nr. 4 — Reisezweck

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `4 Reisezweck bitte ausführlich angeben...` | Text | Reisezweck (ausführlich!) |

### Nr. 5 — Reiseverlauf

#### Tägliche Rückkehr

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Ja tägliche Rückkehr wie unter 5a bis 5d angegeben` | Btn | ☑ Tägliche Rückkehr | `/On` |

#### 5a — Beginn der Reise

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `a Beginn der Reise am` | Btn | ☑ Wohnort/Aufenthaltsort (lt. 1a/1b/1c) | `/On` |
| `Dropdown5` | Choice | Auswahl: 1a), 1b) oder 1c) — von wo die Reise beginnt | `1a)` |
| `Dienstort` | Btn | ☑ Dienstort | `/On` |
| `am Datum5 Reiseverlauf...a Beginn der Reise am...` | Text | Datum Reisebeginn (TT.MM.JJJJ) |
| `um Uhr5 Reiseverlauf...a Beginn der Reise am...` | Text | Uhrzeit Reisebeginn (HH:MM) |

> **Logik**: Entweder `a Beginn der Reise am` (= Wohnort) + `Dropdown5` ODER `Dienstort` ankreuzen. Nicht beides!

#### 5b — Beginn des Dienstgeschäfts

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `b Beginn des Dienstgeschäftes in Ort` | Text | Ort des Dienstgeschäfts |
| `am Datumb Beginn des Dienstgeschäftes...` | Text | Datum (TT.MM.JJJJ) |
| `um Uhrb Beginn des Dienstgeschäftes...` | Text | Uhrzeit (HH:MM) |
| `weiterer Geschäftsort` | Text | Weiterer Geschäftsort (optional) |
| `am Datumb...weiterer Geschäftsort..._2` | Text | Datum weiterer Ort |
| `um Uhrb...weiterer Geschäftsort..._2` | Text | Uhrzeit weiterer Ort |

#### 5c — Ende des Dienstgeschäfts

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `c Ende des Dienstgeschäftes in Ort` | Text | Ort |
| `am Datumc Ende des Dienstgeschäftes in Ort` | Text | Datum (TT.MM.JJJJ) |
| `um Uhrc Ende des Dienstgeschäftes in Ort` | Text | Uhrzeit (HH:MM) |

#### 5d — Ende der Reise

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `undefined` | Btn | ☑ Wohnort/Aufenthaltsort (lt. 1a/1b/1c) | `/On` |
| `Dropdown6` | Choice | Auswahl: 1a), 1b) oder 1c) — wo die Reise endet | `1a)` |
| `Dienstort_2` | Btn | ☑ Dienstort | `/On` |
| `am Datumd Ende der Reise am...` | Text | Datum Reiseende (TT.MM.JJJJ) |
| `um Uhrd Ende der Reise am...` | Text | Uhrzeit Reiseende (HH:MM) |

### Nr. 6 — Besondere Gründe Aufenthaltsort

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Die DR wird aus besonderen dienstlichen Gründen an dem vorübergehenden Aufenthaltsort 1c angetreten  beendet` | Btn | ☑ Reise beginnt/endet am vorübergehenden Aufenthaltsort | `/On` |

### Nr. 7 — Privatreise / Urlaub

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Mit dieser Reise wird eine UrlaubsPrivatreise verbunden...` | Btn | ☑ Privatreise verbunden | `/On` |
| `Ja` | Btn | ☑ Ja (Urlaub genehmigt) | `/On` |
| `Nein` | Btn | ☑ Nein (Urlaub nicht genehmigt) | `/On` |
| `priv Aufenthalt Wochenende Zeitausgleich vom` | Text | Privataufenthalt von (Datum) |
| `bis` | Text | Privataufenthalt bis (Datum) |
| `Urlaub im Zeitraum vom` | Text | Urlaubszeitraum von |
| `bis_2` | Text | Urlaubszeitraum bis |
| `bewilligt am` | Text | Urlaub bewilligt am |
| `Urlaubsort` | Text | Urlaubsort |

### Nr. 8 — Unterkunft

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Höhe der Kosten je Nacht` | Text | Übernachtungskosten pro Nacht (EUR) |
| `steht des Amtes wegen unentgeltlich bereit` | Btn | ☑ Unterkunft steht dienstlich unentgeltlich bereit | `/On` |
| `Ja bezahlt von` | Text | Unterkunft ja, bezahlt von... |
| `undefined_2` | Text | Weitere Angaben zur Unterkunft |
| `Kosten liegen über Städtekatalog es` | Btn | ☑ Kosten über Städtekatalog | `/On` |
| `Nein_5` | Btn | ☑ Keine Unterkunft benötigt | `/On` |
| `von Veranstalter vorreserviertes` | Btn | ☑ Vom Veranstalter vorreserviertes Hotel | `/On` |

#### Unterkunfts-Optionen Checkboxen (Kontrollkästchen7-12)

| Feld-ID | Typ | Visuelle Position | Checked Value |
|---------|-----|------------------|---------------|
| `Kontrollkästchen7` | Btn | "private Unterkunft wird genutzt: **Ja**" | `/Ja` |
| `Kontrollkästchen8` | Btn | "private Unterkunft wird genutzt: **Nein**" | `/Ja` |
| `Kontrollkästchen9` | Btn | "Übernachtungspauschale wird beantragt: **Ja**" | `/Ja` |
| `Kontrollkästchen10` | Btn | "Übernachtungspauschale wird beantragt: **Nein**" | `/Ja` |
| `Kontrollkästchen11` | Btn | "inkl. Frühstück: **Ja**" | `/Ja` |
| `Kontrollkästchen12` | Btn | "inkl. Frühstück: **Nein**" | `/Ja` |

> **Typisches Hotel-Szenario**: Bei einer normalen Hotelübernachtung:
> - K8 = `/Ja` (private Unterkunft: Nein — es ist ein Hotel)
> - K10 = `/Ja` (Übernachtungspauschale: Nein — tatsächliche Kosten)
> - K12 = `/Ja` (inkl. Frühstück: Nein — falls kein Frühstück)
> - `Höhe der Kosten je Nacht` = Preis pro Nacht in EUR

### Nr. 9 — Beförderungsmittel

#### BahnCard / Deutschlandticket

| Feld-ID | Typ | Beschreibung | Quelle personal-data.md |
|---------|-----|-------------|------------------------|
| `Ja BC zB BCB 50 oder BC 25` | Text | BahnCard Art (z.B. "BC 50") | aus personal-data.md (leer wenn keine BC) |
| `Nein_6` | Btn | ☑ Keine BahnCard | `/On` |
| `Kontrollkästchen27` | Btn | ☑ BahnCard Ja | `/Ja` |
| `Kontrollkästchen28` | Btn | ☑ BahnCard Nein | `/Ja` |
| `Nein_7` | Btn | ☑ Kein Deutschlandticket | `/On` |
| `Kontrollkästchen29` | Btn | ☑ Deutschlandticket Ja | `/Ja` |
| `Kontrollkästchen30` | Btn | ☑ Deutschlandticket Nein | `/Ja` |

> **Logik**: BahnCard-Status und Deutschlandticket aus personal-data.md lesen. Beispiel: BahnCard Nein → `Nein_6` = `/On`, `Kontrollkästchen28` = `/Ja`. Deutschlandticket Ja → `Kontrollkästchen29` = `/Ja`.

#### Mitfahrer

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Mitfahrerin bei` | Text | Mitfahrer*in bei (Name) |
| `Dienststelle` | Text | Dienststelle des/der Mitfahrenden |

#### Beförderungsmittel-Matrix (Kontrollkästchen13-26)

Die Beförderungsmittel-Tabelle hat 7 Spalten × 2 Zeilen (Hin / Rück):

| Spalte | Hin (obere Reihe) | Rück (untere Reihe) |
|--------|-------------------|---------------------|
| Bahn | `Kontrollkästchen13` | `Kontrollkästchen14` |
| Flugzeug | `Kontrollkästchen15` | `Kontrollkästchen16` |
| Privat-Kfz | `Kontrollkästchen17` | `Kontrollkästchen18` |
| Dienst-Kfz | `Kontrollkästchen19` | `Kontrollkästchen20` |
| Mietwagen | `Kontrollkästchen21` | `Kontrollkästchen22` |
| Taxi | `Kontrollkästchen23` | `Kontrollkästchen24` |
| Sonstige | `Kontrollkästchen25` | `Kontrollkästchen26` |

Alle verwenden checked_value = `/Ja`.

#### PKW-Anerkennung (Kontrollkästchen31-35)

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Kontrollkästchen31` | Btn | Privat-Kfz: triftige Gründe Ja | `/Ja` |
| `Kontrollkästchen32` | Btn | Privat-Kfz: triftige Gründe Nein | `/Ja` |
| `Kontrollkästchen33` | Btn | Dienst-Kfz: angefordert Ja | `/Ja` |
| `Kontrollkästchen34` | Btn | Dienst-Kfz: angefordert Nein | `/Ja` |
| `Kontrollkästchen35` | Btn | **Anlage: Kostenkalkulation** (Fußzeile Seite 1) | `/Ja` |

#### Anlage-Checkboxen (Fußzeile beider Seiten)

Beide Seiten haben am unteren Rand identische "Anlage:"-Checkboxen. Bei Seite 1 sind es K29-K35 (Achtung: K29 = Deutschlandticket, gehört NICHT zur Anlage), bei Seite 2 K58-K64.

| Seite 1 | Seite 2 | Beschreibung |
|---------|---------|-------------|
| `Kontrollkästchen33` | `Kontrollkästchen62` | Anlage: bestätigter Fahrauftrag |
| `Kontrollkästchen35` | `Kontrollkästchen64` | Anlage: Kostenkalkulation |

> **Wichtig**: Wenn DR-003 (Kostenkalkulation) beiliegt, IMMER K35 (Seite 1) UND K64 (Seite 2) auf `/Ja` setzen!

---

## Seite 2

### Nr. 9 Fortsetzung — Triftige Gründe PKW

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `erhebliche Dienstliche Gründe  5 Abs 2 liegen vor...` | Btn | ☑ Erhebliche dienstliche Gründe (§5 Abs. 2) | `/On` |

### Nr. 10 — Sonstige Kosten

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `EUR für` | Text | Betrag (EUR) |
| `10 Sonstige Kosten zB Tagungspauschalen Nebenkosten` | Text | Beschreibung der sonstigen Kosten |
| `Tagungspauschale enthält Verpflegung` | Btn | ☑ Tagungspauschale enthält Verpflegung | `/On` |

### Nr. 11 — Verpflegung (Tagegeld-Verzicht)

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `undefined_3` | Btn | ☑ Auf Tagegeld wird verzichtet | `/On` |

#### Verpflegungs-Checkboxen (Kontrollkästchen36-45)

Sieben Wochentage in der Tabelle. Die Checkboxen markieren, an welchen Tagen unentgeltliche Verpflegung bereitgestellt wird:

| Feld-ID | Bedeutung |
|---------|-----------|
| `Kontrollkästchen36` | Montag - Frühstück |
| `Kontrollkästchen37` | Dienstag - Frühstück |
| `Kontrollkästchen38` | Mittwoch - Frühstück |
| `Kontrollkästchen39` | Donnerstag - Frühstück |
| `Kontrollkästchen40` | Freitag - Frühstück |
| `Kontrollkästchen41` | Samstag - Frühstück |
| `Kontrollkästchen42` | Mittwoch - Mittag |
| `Kontrollkästchen43` | Mittwoch - Abend |
| `Kontrollkästchen44` | Donnerstag - Mittag |
| `Kontrollkästchen45` | Donnerstag - Abend |

> **Achtung**: Die genaue Zuordnung der Verpflegungs-Checkboxen zu Wochentagen/Mahlzeiten muss visuell am PDF verifiziert werden. Die obige Zuordnung ist eine Annäherung basierend auf den Koordinaten.

### Nr. 13 — Erläuterungen / Begründungen

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `13 ErläuterungenBegründungen zum Reiseantrag` | Text (mehrzeilig) | Freitext für Begründungen, Mitreisende, PKW-Begründung etc. |

### Verzicht auf Erstattung

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Ich verzichte auf die Erstattungen die den Betrag in Höhe von` | Btn | ☑ Verzicht auf Erstattungen über Betrag X | `/On` |
| `EUR übersteigen` | Text | Betrag (EUR) |

### Unterschrift Antragsteller*in

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Datum Unterschrift Antragstellerin` | Text | Datum der Unterschrift |
| `undefined_4` | Text | Abrechnungsobjekt (Seite 2 oben) — wird evtl. vom Vorgesetzten eingetragen |

### Genehmigungsteil (wird vom Vorgesetzten / Reisekostenstelle ausgefüllt)

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Name in Druckbuchstaben` | Text | Name Vorgesetzte*r |
| `Name in Druckbuchstaben_2` | Text | Name Dekan*in / Kanzler*in |
| `Abrechnungsobjekt` | Text | Abrechnungsobjekt (Kostenstelle) |
| `Namen in Druckbuchstaben` | Text | Name genehmigend (Seite 2 unten) |

#### Genehmigungs-Checkboxen (Seite 2)

| Feld-ID | Typ | Beschreibung |
|---------|-----|-------------|
| `Benutzung regelmäßig verkehrender Beförderungsmittel` | Btn | ☑ Genehmigt: ÖPNV/Bahn | `/On` |
| `Benutzung eines Dienstwagens aus dienstl Gründen wird` | Btn | ☑ Genehmigt: Dienstwagen | `/On` |
| `Kontrollkästchen46` | Btn | Genehmigung Checkbox 1 | `/Ja` |
| `Kontrollkästchen47` | Btn | Genehmigung Checkbox 2 | `/Ja` |
| `Kontrollkästchen48` | Btn | Genehmigt: Variante A | `/Ja` |
| `Kontrollkästchen49` | Btn | Genehmigt: Variante B | `/Ja` |
| `Kontrollkästchen50`-`53` | Btn | Anerkennung PKW/Taxi (anerkannt/nicht anerkannt) | `/Ja` |
| `anerkannt_2` | Btn | ☑ Privat-PKW anerkannt | `/On` |
| `nicht anerkannt_2` | Btn | ☑ Privat-PKW nicht anerkannt | `/On` |
| `anerkannt_3` | Btn | ☑ Taxi anerkannt | `/On` |
| `nicht anerkannt_3` | Btn | ☑ Taxi nicht anerkannt | `/On` |
| `anerkannt_4` | Btn | ☑ Mietwagen anerkannt | `/On` |
| `nicht anerkannt_4` | Btn | ☑ Mietwagen nicht anerkannt | `/On` |
| `ja` | Btn | ☑ Ja (Abschlag) | `/On` |
| `ja_2` | Btn | ☑ Ja (weitere Genehmigung) | `/On` |

> **Wichtig**: Der gesamte Genehmigungsteil wird NICHT vom Antragsteller ausgefüllt. Diese Felder nur dokumentieren, nicht befüllen!

---

## Zusammenfassung: Vom Antragsteller auszufüllende Felder

Für einen typischen Dienstreiseantrag (Inland, Bahn, Hotel) müssen folgende Felder befüllt werden:

```python
# Beispiel field_values — typische Inlandsdienstreise (Bahn, Hotel)
# Persönliche Daten aus personal-data.md lesen!
fields_page1 = {
    # Art: Dienstreise
    "Kontrollkästchen1": "/Ja",
    # Personalart: aus personal-data.md (hier: wiss./künstl.)
    "Kontrollkästchen2": "/Ja",
    "wissenkünstl Personal": "/On",
    # Persönliche Daten → aus personal-data.md laden
    "1 Reisender Antragstellerin Name Vorname": "<Name, Vorname>",
    "Dienstort ltVertrag": "<Dienstort>",
    "Fakultät Bereich": "<Fakultät/Bereich>",
    "Telefon": "<Telefon>",
    "1a Wohnort PLZ Ort Straße Nr...": "<PLZ, Ort, Straße>",
    # Reiseziel
    "3 Reiseziel komplette Anschrift": "<Zielort, Straße, PLZ Ort>",
    # Reisezweck
    "4 Reisezweck bitte ausführlich angeben...": "<Reisezweck>",
    # Reiseverlauf 5a: Beginn ab Wohnort
    "a Beginn der Reise am": "/On",
    "Dropdown5": "1a)",
    "am Datum5 Reiseverlauf...a Beginn der Reise am...": "<TT.MM.JJJJ>",
    "um Uhr5 Reiseverlauf...a Beginn der Reise am...": "<HH:MM>",
    # 5b-5d analog...
    # Unterkunft (Hotel-Szenario)
    "Höhe der Kosten je Nacht": "<Preis>",
    "Kontrollkästchen8": "/Ja",   # private Unterkunft: NEIN (Hotel!)
    "Kontrollkästchen10": "/Ja",  # Übernachtungspauschale: NEIN
    "Kontrollkästchen12": "/Ja",  # inkl. Frühstück: NEIN
    # BahnCard/Deutschlandticket aus personal-data.md
    "Nein_6": "/On",              # Keine BahnCard (Beispiel)
    "Kontrollkästchen28": "/Ja",  # BahnCard Nein
    "Kontrollkästchen29": "/Ja",  # Deutschlandticket Ja (Beispiel)
    # Beförderungsmittel: Bahn hin + rück
    "Kontrollkästchen13": "/Ja",
    "Kontrollkästchen14": "/Ja",
    # Anlage: Kostenkalkulation
    "Kontrollkästchen35": "/Ja",
}

fields_page2 = {
    # Erläuterungen
    "13 ErläuterungenBegründungen zum Reiseantrag": "<Mitreisende, Begründungen>",
    # Unterschrift
    "Datum Unterschrift Antragstellerin": "<TT.MM.JJJJ>",
    # Anlage: Kostenkalkulation (Seite 2)
    "Kontrollkästchen64": "/Ja",
}
```

> **Hinweis**: Die exakten Feld-IDs sind sehr lang. Bei der Befüllung die vollständigen Feld-IDs aus dieser Datei verwenden, nicht kürzen!
