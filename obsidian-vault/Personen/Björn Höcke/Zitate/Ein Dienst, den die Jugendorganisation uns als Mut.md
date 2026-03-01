---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-10-18
topic: Sonstiges
page_bfv: 828
source: 'YouTube; info-DIREKT Magazin'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 18.10.2022 veröffentlicht auf: 'YouTube; info-DIREKT Magazin'
> [!quote] Aussage
>Ein Dienst, den die Jugendorganisation uns als Mutterpartei leisten kann, ist, uns immer wieder mal [...] in den Hintern zu treten, damit wir lebendig bleiben. Sie muss selber dafür lebendig bleiben, also die Jugendorganisation, damit die Mutterpartei lebendig bleiben darf. Und das ist mir ein wichtiges Anliegen, und auch den Jugendlichen Mut zu machen. Denkt nicht so sehr in Funktionskategorien, denkt nicht so sehr in Organisationskategorien. Geht vor allen Dingen raus. Wir müssen draußen sein, wir müssen sichtbar sein. Das ist das allerentscheidenste. Der Kampf, den wir kämpfen, um die Existenz unserer Nation und Europas, der wird nicht in den Parlamenten entschieden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 828

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