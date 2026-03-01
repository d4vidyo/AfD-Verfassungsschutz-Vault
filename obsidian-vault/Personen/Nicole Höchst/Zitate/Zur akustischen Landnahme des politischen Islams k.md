---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2021-10-17
topic: Menschenwürde
page_bfv: 474
source: 'Kolumne'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 17.10.2021 veröffentlicht auf: 'Kolumne'
> [!quote] Aussage
>Zur akustischen Landnahme des politischen Islams kommt aber leider noch etwas hinzu: Allahu Akbar ist zugleich nämlich auch der Schlachtruf selbsternannter Dschihadisten und ,Sprenggläubiger' - Für die Opfer unzähliger Terrorattacken, Messerangriffe und sonstiger Anschläge auf europäischen Straßen war es das Letzte, was sie in ihrem Leben hörten. Ob die Angreifer anschließend für schuldfähig erklärt werden oder (wie zumeist) nicht, tut dabei tatsächlich wenig zur Sache: Allahu Akbar [...] ist mittlerweile untrennbar bedeutungsverwoben mit den blutigen Horrorbildern, die wir alle hinlänglich kennen [...]. [...] Wir zivilisierten Bürger haben kein Interesse daran, unser multikulturelles Zusammenleben täglich auf der Straße mit Messern, Macheten oder anderem Tötungswerkzeug ,neu auszuhandeln'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 474

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

---
## Meine Auswertung:

**Meine Bewertung:** `INPUT[inlineSelect(option(Unbewertet), option(Legitim), option(Fragwürdig), option(Nicht legitim), defaultValue(Unbewertet)):status]`

_Mein Kommentar:_ 


---
# Nächste Aussage:
```dataview
TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
FROM "Personen"
WHERE type = "zitat" and status = "Unbewertet" AND file.name != this.file.name
SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
LIMIT 10
```