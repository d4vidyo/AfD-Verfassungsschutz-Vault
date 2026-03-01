---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023
topic: Menschenwürde
page_bfv: 430
source: 'Buch'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 2023 veröffentlicht auf: 'Buch'
> [!quote] Aussage
>Rechte Politik für Deutschland muß die statistischen Realitäten beachten: Es sind nicht Hochqualifizierte, die nach Deutschland und Europa einwandern. Mit einem IQ von 80 oder 90 kann man keine qualifizierten Arbeiten ausführen; ein deutscher Handwerksberuf wie Elektriker, Zahntechniker, Mechatroniker erfordert eine höhere Intelligenz. Diese IQ-Unterschiede sind wenig problematisch, solange die Menschen in ihren natürlichen Heimatregionen leben; ein Afrikaner in Afrika, ein Syrer in Syrien, ein Afghane in Afghanistan kann in seiner Gesellschaft wertvolle Beiträge leisten. Aber in der hochkomplexen europäischen Gesellschaft und Arbeitswelt kann er das kaum. Da viele Eigenschaften, Intelligenz eingeschlossen, überwiegend vererbt werden, ist der Plan, durch Masseneinwanderung die nicht mehr geborenen autochthonen Fachkräfte zu ersetzen, zum Scheitern verurteilt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 430. aus Krahs Buch "Politik von rechts"

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