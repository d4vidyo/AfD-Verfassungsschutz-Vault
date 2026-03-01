---
type: zitat
speaker: "[[Christina Baum]]"
date: 2023-06-03
topic: Menschenwürde
page_bfv: 491
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 3.6.2023 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Das Ziel der Globalisten war und ist klar: der geplante Bevölkerungsaustausch soll so lange geleugnet und Mahner als Verschwörungstheoretiker gebrandmarkt werden, bis er irreversibel ist. Deshalb soll so lange abgelenkt, gelogen und getäuscht werden, bis man vor vollendeten Tatsachen steht.

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[Das Ziel der Globalisten war und ist klar_ der gep]]

**SPIEGEL-Notiz:** Gutachten Seite: 491

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