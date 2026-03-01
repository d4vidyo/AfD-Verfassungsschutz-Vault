---
type: zitat
speaker: "[[Daniel Halemba]]"
date: 2023-11-01
topic: Menschenwürde
page_bfv: 156
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Daniel Halemba]] vom 1.11.2023 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der Zuzug kulturgleicher Hugenotten ist nicht mit der modernen Ersetzungsmigrationdurch Afrikaner & Araber zu vergleichen [...] Wollen Sie mir etwa erzählen, dass Hugenotten nicht einfacher zu assimilieren sind als Araber und Afrikaner? Das ist doch absurd! Weil Göthe und Friedrich arabische Kultur toll fanden glauben Sie die Herren würden die heutige Ersetzungsmigration befürworten? [...] Migration aus Nahost / Afrika ist ein Nettoverlust für uns. Das weiss jeder.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 156

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