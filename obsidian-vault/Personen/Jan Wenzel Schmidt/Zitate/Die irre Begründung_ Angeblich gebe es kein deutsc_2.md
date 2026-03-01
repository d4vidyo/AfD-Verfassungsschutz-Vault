---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2023-04-27
topic: Sonstiges
page_bfv: 742
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 27.4.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die irre Begründung: Angeblich gebe es kein deutsches Volk außer dem deutschen Staatsvolk (den Passdeutschen). [...] Die Beobachtung durch den VS ist zutiefst antidemokratisch und falsch. Damit sie sich juristisch wehren können, spende ich eine 'Demokratieabgabe' an JA, IfS und 'Ein Prozent'. Macht ihr mit?

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[Die irre Begründung_ Angeblich gebe es kein deutsc]]

**SPIEGEL-Notiz:** Gutachten Seite: 742

**Verfassungsschutz Kategorisierung:** Sonstiges.

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