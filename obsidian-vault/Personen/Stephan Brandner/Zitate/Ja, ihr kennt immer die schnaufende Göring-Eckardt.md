---
type: zitat
speaker: "[[Stephan Brandner]]"
date: 2025-01-18
topic: Demokratieprinzip
page_bfv: 956
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Stephan Brandner]] vom 18.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Ja, ihr kennt immer die schnaufende Göring-Eckardt im Nacken mit der Stoppuhr. Irgendeiner sagt mir mal, ich weiß gar nicht, ob man das hier wiederholen darf. Manche nennen sie Frau Reichsmarschall-Eckardt. Mache ich mir nicht zu eigen, Gott will, ich habe es nur gehört. Aber ihre Attitüde, ihr Gehabe ist tatsächlich manchmal so, wie man sich das vorstellt in den Geschichtsbüchern.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 956

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