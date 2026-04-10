# Beleg-Benennungsschema

## Schema

```
[NN]_[Kategorie]_[Beschreibung]_[Betrag]EUR.[ext]
```

| Bestandteil | Beschreibung | Beispiel |
|-------------|-------------|----------|
| `NN` | Laufende Nummer, zweistellig mit führender Null | `01`, `02`, `13` |
| `Kategorie` | Belegtyp (siehe Tabelle unten) | `Bahn`, `Hotel` |
| `Beschreibung` | Kerninfo zum Beleg — Route, Name, Ort. Teile mit `-` verbinden. | `Weimar-Koeln`, `PremierInn-Koeln-2N` |
| `Betrag` | Rechnungsbetrag in EUR, mit Punkt als Dezimaltrenner | `74.49`, `111.87` |
| `[ext]` | Originale Dateiendung beibehalten | `.pdf`, `.jpg` |

## Kategorien

| Kategorie | Verwendung |
|-----------|-----------|
| `Bahn` | DB-Tickets, Fernbus-Tickets |
| `Hotel` | Hotelrechnungen, Pensionen, Hostels |
| `Konferenz` | Teilnahmegebühren, Messe-Tickets, Tagungsbeiträge |
| `OEPNV` | U-Bahn, Straßenbahn, Bus (Nahverkehr) |
| `Taxi` | Taxi-Quittungen |
| `Flug` | Flugtickets, Boarding-Pässe mit Preisangabe |
| `Parkgebuehr` | Parktickets, Parkhaus-Quittungen |
| `Sonstige` | Alles was in keine andere Kategorie passt |

## Beschreibung — Formatregeln

- **Bahn**: `[Von]-[Nach]` — z.B. `Weimar-Koeln`, `Koeln-Weimar`
- **Hotel**: `[Hotelname]-[Ort]-[N]N` — z.B. `PremierInn-Koeln-2N` (2 Nächte)
- **Konferenz**: `[Veranstaltungsname]` — z.B. `DigitalBau-Tagesticket`
- **OEPNV**: `[Verkehrsmittel]-[Ort]` — z.B. `UBahn-Koeln`, `Tram-Berlin`
- **Taxi**: `[Von]-[Nach]` oder `[Ort]` — z.B. `Hbf-Hotel`, `Koeln`
- **Flug**: `[Von]-[Nach]` — z.B. `BER-MUC`
- **Parkgebuehr**: `[Ort]` — z.B. `Flughafen-BER`, `Hbf-Weimar`
- **Sonstige**: Kurze Beschreibung — z.B. `Gepaeckaufbewahrung-Hbf`

### Zeichenregeln

- Keine Umlaute: `ae`, `oe`, `ue`, `ss` statt `ä`, `ö`, `ü`, `ß`
- Keine Leerzeichen: `-` als Trenner innerhalb der Beschreibung
- Keine Sonderzeichen: nur `a-z`, `A-Z`, `0-9`, `-`, `_`, `.`

## Beispiele

```
01_Bahn_Weimar-Koeln_74.49EUR.pdf
02_Bahn_Koeln-Weimar_101.49EUR.pdf
03_Hotel_PremierInn-Koeln-2N_111.87EUR.pdf
04_Konferenz_DigitalBau-Tagesticket_45.00EUR.pdf
05_OEPNV_UBahn-Koeln_3.20EUR.pdf
06_Taxi_Hbf-Messe_18.50EUR.pdf
07_Sonstige_Gepaeckschliessfach-Hbf_4.00EUR.pdf
```

## Nummerierung

Die laufende Nummer spiegelt die chronologische Reihenfolge der Kosten wider:
1. Hinfahrt (Bahn/Flug)
2. ÖPNV/Taxi am Zielort (Ankunft)
3. Hotel
4. Konferenz/Messe
5. ÖPNV/Taxi am Zielort (Abreise)
6. Rückfahrt (Bahn/Flug)
7. Sonstiges

Falls die genaue Reihenfolge nicht aus den Belegen hervorgeht, nach Datum sortieren. Belege gleichen Datums nach Kategorie gruppieren.

## Ablauf im Skill

1. **Belege einlesen und klassifizieren** (Schritt 2 der Abrechnung)
2. **Neuen Dateinamen ableiten** — Aus den erkannten Daten (Kategorie, Route/Name, Betrag) den Dateinamen nach Schema zusammensetzen
3. **Dem User als Tabelle zur Bestätigung vorzeigen:**

   ```
   Die Belege würde ich wie folgt umbenennen:

   | # | Aktueller Name              | Neuer Name                              |
   |---|-----------------------------|-----------------------------------------|
   | 1 | Ticket_ICE_1234.pdf         | 01_Bahn_Weimar-Koeln_74.49EUR.pdf       |
   | 2 | booking-confirm.pdf         | 02_Hotel_PremierInn-Koeln-2N_111.87EUR.pdf |
   | 3 | Rechnung.pdf                | 03_Konferenz_DigitalBau_45.00EUR.pdf    |

   Soll ich die Dateien so umbenennen?
   ```

4. **Erst nach Bestätigung umbenennen** — Dateien im `Belege/`-Ordner per `mv` (oder Plattform-äquivalent) umbenennen
5. Falls der User einzelne Namen anpassen möchte, die Korrekturen übernehmen und nochmals bestätigen lassen
