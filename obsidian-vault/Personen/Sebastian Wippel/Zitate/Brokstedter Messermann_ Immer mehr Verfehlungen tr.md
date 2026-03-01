---
type: zitat
speaker: "[[Sebastian Wippel]]"
date: 2023-02-15
topic: Menschenwürde
page_bfv: 297
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Wippel]] vom 15.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Brokstedter Messermann: Immer mehr Verfehlungen treten zutage - und das ist nur die Spitze des Eisbergs! Das Ausmaß des staatlichen sowie Behördenversagens im Falle des Brokstedter Messermanns nimmt kein Ende: Seit der blutigen Metzelei in einem Regionalzug von Kiel nach Hamburg im vergangenen Januar vergeht kein Tag, an welchem nicht neue Enthüllungen menschlichen Versagens zutage treten. [...] Brokstedt ist ein Symbol geworden - ein Symbol dafür, was passiert, wenn ein dekadenter und linksideologisch-globalistisch geprägter Staat über seine Belastungsgrenzen hinweg die eigene Identität aufgibt und zum Einwanderungszentrum der gesamten arabischen und afrikanischen Welt wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 297

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