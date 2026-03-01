---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2023-06-17
topic: Menschenwürde
page_bfv: 360
source: 'YouTube, Frank Chruschtschow'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 17.6.2023 veröffentlicht auf: 'YouTube, Frank Chruschtschow'
> [!quote] Aussage
>Und da kommen natürlich bei denen, bei dem Rest, kommen natürlich auch die dazu, die noch nie in unsere Sozialsysteme eingezahlt haben, die also zuhauf, zu Hunderttausenden jährlich nach Deutschland kommen, sich aber nicht beteiligen wollen an unserer Gesellschaft. Die wollen unsere Kultur nicht, sich an unsere Kultur nicht anpassen, nicht an unsere Traditionen anpassen und so weiter und so fort, sondern sie kommen nur her, um sich in die soziale Hängematte zu legen, und ab und zu zücken sie ein Messer und stechen irgendjemanden von uns ab. Und das muss natürlich auch aufhören. Und wir als AfD sind die einzig ernstzunehmende Partei, die dafür kämpft, dass die Migrationskrise endlich beendet wird. Wir brauchen eine Abschiebeinitiative.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 360

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