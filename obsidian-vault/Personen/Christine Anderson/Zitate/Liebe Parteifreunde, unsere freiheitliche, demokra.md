---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2023-07-29
topic: Menschenwürde
page_bfv: 500
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 29.7.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Liebe Parteifreunde, unsere freiheitliche, demokratische und rechtsstaatliche Gesellschaft, bestehend aus freien, mündigen Bürgern mit unveräußerlichen Grundrechten soll in ein unter totalitärer Herrschaft stehendes Kollektiv überführt werden, in dem der Einzelne lediglich noch Teil einer willenlosen, formbaren, völlig verarmten, entrechteten, entmündigten und entsolidarisierten Masse ist, über die die globalitären Misanthropen nach freiem Belieben verfügen können. Schluss damit! [...] Während die EU, während die EU aber jetzt 'nur' für die Entrechtung der europäischen Völker zuständig ist, schreitet man auf globaler Ebene zur Entrechtung aller Völker dieser Erde. Bislang musste man das so den Nationalstaaten überlassen, die öffentliche Gesundheit durch massive Grundrechtseinschränkung, Diskriminierung, Schikane und Ausgrenzung der Bürger 'sicher zu stellen'. In Zukunft will – nein, muss man das dem wesentlich einfacher zu steuernden Gremium der WHO überlassen. Dieses korrupte, von Multimilliardären gesteuerte und kontrollierte Gremium bietet zudem den Vorteil, dem Bürger gegenüber in keinster Weise politisch verantwortlich zu sein. Deshalb kann und wird die WHO gänzlich unbeeindruckt von der Bestrafung an der Wahlurne mit noch sehr viel totalitären Maßnahmen die öffentliche Gesundheit zu schützen wissen, verlassen sie sich darauf.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 500

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