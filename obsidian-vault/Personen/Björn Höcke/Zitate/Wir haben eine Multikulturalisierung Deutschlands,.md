---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-08-01
topic: Menschenwürde
page_bfv: 237
source: 'Interview beim MDR'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom August 2022 veröffentlicht auf: 'Interview beim MDR'
> [!quote] Aussage
>Wir haben eine Multikulturalisierung Deutschlands, die in wenigen Jahrzehnten, wenn man das Geburtsdefizit der Deutschen noch dazurechnet, zum Ende dessen führen wird, was wir ein Deutsches Volk nennen. Und das kann doch nicht in Ordnung sein. [...] Ich distanziere mich um Gottes Willen nicht von Frau Baum.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: August 2022

**SPIEGEL-Notiz:** Gutachten Seite: 237

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