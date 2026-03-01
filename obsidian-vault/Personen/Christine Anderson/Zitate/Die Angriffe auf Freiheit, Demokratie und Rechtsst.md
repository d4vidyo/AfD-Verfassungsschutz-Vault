---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2023-07-29
topic: Menschenwürde
page_bfv: 317
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 29.7.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Die Angriffe auf Freiheit, Demokratie und Rechtsstaatlichkeit, auf unsere nationale, kulturelle, gar sexuelle Identität, die bestialische Körper- und Genitalverstümmelung unserer Kinder, der Raub und die Destabilisierung unserer Heimat durch den millionenfachen Import von 'purem Gold' werden inzwischen auf allen Ebenen aller Regierungs- und Nicht-Regierungsinstitutionen vorangetrieben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 317

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