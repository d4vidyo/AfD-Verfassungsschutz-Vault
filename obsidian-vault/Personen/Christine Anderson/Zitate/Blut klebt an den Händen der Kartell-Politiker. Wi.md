---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2025-01-26
topic: Demokratieprinzip
page_bfv: 960
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 26.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Blut klebt an den Händen der Kartell-Politiker. Wie viele tote oder vergewaltigte Kinder, Frauen und Männer wollen wir noch hinnehmen, während unsere Grenzen weiter ungeschützt offenstehen? Wie lange wollen wir uns noch von hunderttausenden - längst abschiebepflichtigen - Illegalen ausnutzen und auf der Nase herumtanzen lassen? Wer die Grenzen nicht schützt und Migration nicht kontrolliert, reißt unser Land absichtlich ins Chaos. Alle Statistiken beweisen es. CDU Kanzlerkandidat Friedrich Merz ist ein Lügner, ein Schwätzer und ein erbärmlicher Wendehals. Wir brauchen keine machtgeilen Politdarsteller. Wir brauchen STACHELDRAHT, BETON und PUSHBACKS! Jetzt!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 960

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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