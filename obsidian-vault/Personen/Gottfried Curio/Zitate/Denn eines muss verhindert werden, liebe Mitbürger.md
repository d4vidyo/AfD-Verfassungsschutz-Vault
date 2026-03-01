---
type: zitat
speaker: "[[Gottfried Curio]]"
date: 2025-01-08
topic: Menschenwürde
page_bfv: 883
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Gottfried Curio]] vom 8.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Denn eines muss verhindert werden, liebe Mitbürger. Eine Entheimatung der Deutschen in ihrem eigenen Land, in Deutschland. Das wollen wir nicht, dass sich unser Lebensgefühl verändert. Dass immer mehr öffentliche Räume zu Angsträumen werden, das haben die Deutschen nicht verdient in ihrem Land.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 883

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