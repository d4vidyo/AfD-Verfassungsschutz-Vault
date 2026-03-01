---
type: zitat
speaker: "[[Kay Gottschalk]]"
date: 2024-12-03
topic: Sonstiges
page_bfv: 859
source: 'Phoenix'
status: Unbewertet
---

# Zitat: [[Kay Gottschalk]] vom 3.12.2024 veröffentlicht auf: 'Phoenix'
> [!quote] Aussage
>Das ist, ich finde, eine Weiterentwicklung wie in einer Liebesbeziehung. Wir entwickeln diese Beziehung jetzt weiter, wollen sie [...] auf eine neue Stufe stellen. [...]. Also eine viel, viel engere Bindung – was ja immer in einer Partnerschaft positiv ist – an die Mutterpartei an der Stelle. [...] Man ist unter 36 und man muss Parteimitglied sein und ich finde, das ist richtig. Das ist wie in der richtigen Familie dann auch. Und insoweit rücken wir näher aneinander ran, das ist der Punkt. Und wir wollen natürlich auch dann entsprechend mit unserer Jugend auch weiter vernünftige Prozesse anstoßen, damit wir auch bei den Menschen draußen und bei den jungen Leuten ankommen. Also insoweit nichts, was jetzt [...] einer Auflösung oder einer Neugründung gleichkäme, sondern ich nenne das Weiterentwicklung. Und das ist auch richtig nach fast 10 Jahren.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 859

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