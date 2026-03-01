---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2025-02-02
topic: Menschenwürde
page_bfv: 947
source: 'Interview ARD'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 2.2.2025 veröffentlicht auf: 'Interview ARD'
> [!quote] Aussage
>Wir haben dort ebenfalls der Rede, der sehr andächtigen Rede, gelauscht. Und wir haben auch Beifall geklatscht, natürlich. Und für uns steht die Existenz Israels an erster Stelle. Ich weiß, dass das Framing ein komplett anderes ist, das mediale Framing. Aber es ist nun mal so. Wir gedenken dem Holocaust zusammen mit den Juden in der AfD. Das ist eine Vereinigung bei uns.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 947

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