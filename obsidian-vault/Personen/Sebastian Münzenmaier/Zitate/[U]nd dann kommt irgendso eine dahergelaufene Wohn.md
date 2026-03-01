---
type: zitat
speaker: "[[Sebastian Münzenmaier]]"
date: 2023-02-23
topic: Menschenwürde
page_bfv: 219
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Münzenmaier]] vom 23.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>[U]nd dann kommt irgendso eine dahergelaufene Wohnungsgesellschaft und sagt 'Wir schmeißen Sie jetzt raus! Wir brauchen Platz für Ausländer!' Deutlicher kann ich einem Volk doch gar nicht mehr sagen, dass sie eigentlich gar nicht erwünscht sind! Und dann sollen wir den Begriff der Umvolkung nicht benutzen dürfen. Grüße an den Verfassungsschutz. Ja, was ist es denn sonst?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 219

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