---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2021-12-02
topic: Demokratieprinzip
page_bfv: 625
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 2.12.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Wer schützt uns noch vor den Beschützern? Können wir noch sicher von einer gewährleisteten Gewaltenteilung in Deutschland ausgehen? Seit dem "Klimaurteil" ahnten wir es, nun dürfen wir uns wohl endgültig von der Vorstellung verabschieden, das oberste Gericht unseres Landes stünde noch als Schutzwall zwischen der Bundesregierung und unseren Grundrechten. Was bisher durch die Verzögerungstaktik bei wichtigen Urteilen nur erahnt werden konnte, wird nun zur Gewißheit: Das Bundesverfassungsgericht scheut nicht davor zurück, den Referenden einen Blankoscheck für Willkür auszustellen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 625

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