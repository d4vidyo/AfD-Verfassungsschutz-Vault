---
type: zitat
speaker: "[[Christina Baum]]"
date: 2022-05-20
topic: Menschenwürde
page_bfv: 199
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 20.5.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Und wieder wird eine #Verschwörungstheorie wahr: Berliner Senat will mehr als 400.000 #Ausländer einbürgern Der #Bevölkerungsaustausch schreitet mit 7-Meilen-Stiefeln voran. Gut ausgebildete junge Deutsche wandern aus, #Sozialhilfeempfänger aus teils archaischen 'Kulturen' ein. So wird unsere #Heimat zum 3. Welt-Land: ohne #ldentität, ohne verbindende #Kultur und #Sprache, dafür mit #Parallelgesellschaften, hoher #Arbeitslosigkeit, #Verwahrlosung und immer weiter steigender Kriminalität. [...] Und so geht es immer weiter bergab mit dem Land unserer Ahnen....

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 199

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