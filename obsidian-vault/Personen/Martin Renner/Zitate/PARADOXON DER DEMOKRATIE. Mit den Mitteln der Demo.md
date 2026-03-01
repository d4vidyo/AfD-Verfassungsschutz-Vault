---
type: zitat
speaker: "[[Martin Renner]]"
date: 2023-04-22
topic: Demokratieprinzip
page_bfv: 601
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 22.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>PARADOXON DER DEMOKRATIE. Mit den Mitteln der Demokratie kann man die Demokratie schwer schädigen und sogar endgültig zerstören. Und diese Zerstörung betreiben die Parteien der 'Neuen Einheitspartei Deutschlands (NED)' immer unverhohlener und aggressiver.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 601

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