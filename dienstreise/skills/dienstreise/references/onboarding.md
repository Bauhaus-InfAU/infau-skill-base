# Erstnutzer-Onboarding

Dieser Text wird dem User beim allerersten Kontakt gezeigt (wenn noch kein `personal-data.md` existiert). Er erklärt den gesamten Prozess in einfacher Sprache. Der Text wird in der Sprache des Users wiedergegeben — die deutsche Version unten dient als inhaltliche Vorlage.

## Sprache

Übersetze den Inhalt in die Sprache des Users. Verwende die gleiche warme, direkte Tonalität.

---

## Onboarding-Text (Vorlage)

> **Willkommen beim Dienstreise-Assistenten!**
>
> Ich begleite dich durch den kompletten Dienstreiseprozess an der BUW — vom Antrag bis zur Abrechnung. Du musst dich nicht mit den Formularen oder Vorschriften auskennen, das übernehme ich.
>
> **So funktioniert's:**
>
> Wir richten jetzt einmalig einen Ordner ein, in dem alle deine Dienstreisen gesammelt werden. Für jede Reise lege ich darin automatisch einen Unterordner mit allen nötigen Formularen an.
>
> **Vor einer Reise** sagst du mir einfach wohin es geht und wann — ich kümmere mich um den Rest:
> - Ich recherchiere Hotels und Zugverbindungen
> - Ich fülle den Dienstreiseantrag (DR-001) und die Kostenkalkulation (DR-003) aus
> - Ich sage dir genau, was du einreichen musst und an wen
>
> **Nach einer Reise** legst du deine Belege (Bahntickets, Hotelrechnung, etc.) einfach als PDF in den Belege-Ordner. Dann:
> - Ich lese die Belege automatisch ein
> - Ich fülle die Reisekostenabrechnung (DR-004) aus
> - Ich benenne die Belege einheitlich um
> - Ich formuliere die fertige Email, die du nur noch absenden musst
>
> **Was du selbst tun musst:**
> - Belege als PDF in den Ordner legen
> - Den fertigen Antrag unterschreiben (Abrechnung: ausdrucken, unterschreiben, einscannen)
> - Die vorbereitete Email absenden
> - Originalbelege 5 Jahre aufbewahren
>
> **Was du NICHT tun musst:**
> - Formulare suchen oder herunterladen
> - Vorschriften oder Pauschalen nachschlagen
> - Felder im Formular selbst ausfüllen
> - Den Betreff oder Text der Email formulieren
>
> Lass uns starten! Ich brauche zuerst ein paar persönliche Daten von dir (Name, Adresse, Bankverbindung) — die speichere ich einmalig, damit ich sie nicht jedes Mal neu fragen muss.

---

## Nach dem Onboarding-Text

1. Frage den User nach dem **Dienstreise-Ordner**: *"In welchem Ordner sollen deine Dienstreisen gespeichert werden? Das kann ein bestehender Ordner sein oder ich lege einen neuen an (z.B. `Dienstreisen/`)."*
2. Falls der User keinen Vorschlag hat, schlage `Dienstreisen/` im aktuellen Arbeitsverzeichnis vor.
3. Erstelle den Ordner falls nötig.
4. Weiter mit **Schritt 1** (persönliche Daten erfassen) — `personal-data.md` wird in diesem Ordner angelegt.

## Ordnerstruktur-Erklärung (nur bei Bedarf)

Falls der User fragt wie die Ordnerstruktur aussieht, erkläre kurz:

> Dein Dienstreise-Ordner sieht so aus — das meiste davon lege ich automatisch an:
>
> ```
> Dienstreisen/
> ├── personal-data.md                    (deine Daten, einmalig)
> ├── 01_Koeln DigitalBau/               (erste Reise)
> │   ├── DR-001-..._Bielik_2026_Koeln.pdf (Antrag — fülle ich aus)
> │   ├── DR-003-..._Bielik_2026_Koeln.xlsx (Kalkulation — fülle ich aus)
> │   ├── DR_Antrag_Bewilligung.pdf       (kommt vom Dekanat zurück)
> │   ├── DR-004-..._Bielik_2026_Koeln.pdf (Abrechnung — fülle ich aus)
> │   └── Belege/                         (deine Belege — legst du hier rein)
> │       ├── 01_Bahn_Weimar-Koeln_...pdf
> │       └── ...
> ├── 02_Berlin BIM World/               (zweite Reise)
> │   └── ...
> └── ...
> ```
>
> Du musst nur den `Belege/`-Ordner befüllen — alles andere mache ich.
