---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2022-05-21
topic: Demokratieprinzip
page_bfv: 622
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 21.5.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Dieser "Pakt gegen neue Pandemien" ist in Wahrheit ein Pakt um die Volksherrschaft (Art. 20, Abs. 2 GG) abzuschaffen. Das wissen Sie sehr genau, Herr @Karl_Lauterbach! Geben Sie endlich Butter bei die Fische und hören Sie auf, die Bürger für dumm zu verkaufen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 622

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