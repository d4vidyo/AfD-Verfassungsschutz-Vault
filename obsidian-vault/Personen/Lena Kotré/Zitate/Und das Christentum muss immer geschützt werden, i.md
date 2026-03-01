---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-12-14
topic: Menschenwürde
page_bfv: 937
source: 'Podiumsdiskussion'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 14.12.2024 veröffentlicht auf: 'Podiumsdiskussion'
> [!quote] Aussage
>Und das Christentum muss immer geschützt werden, immer, immer - vor allem vor Einwanderern, die aus dem muslimischen Kulturkreis kommen, es ist einfach so. Ich habe große Sorge vor einer Islamisierung meiner Heimat. [...] Und viele Menschen aus diesem Kulturkreis, die in den letzten Jahren erst zu uns gekommen sind, die wollen uns hier im Prinzip das Land streitig machen, das ist meine feste Überzeugung. Es sind selbstverständlich nicht alle und es sind auch in großen Teilen nicht diejenigen, die schon länger hier sind, aber wir müssen da auf der Hut sein in meinen Augen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 937

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