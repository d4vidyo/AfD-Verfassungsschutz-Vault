---
type: zitat
speaker: "[[Christina Baum]]"
date: 2021-11-01
topic: Menschenwürde
page_bfv: 147
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 1.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Bereits am 17. Januar 2015, also lange vor Merkels illegaler Grenzöffnung, warnte ich in meiner Bewerbungsrede zur Landesvorsitzenden in Karlsruhe vor 'einem schleichenden Genozid am deutschen Volk durch die Einwanderungspolitik der Grünen'. [...] Für mich jedoch, die ich 1989 aus der ethnisch homogenen deutschen DDR kam, war es von Anfang an ganz offensichtlich und so wies ich damals bereits im privaten Umfeld daraufhin, dass unsere Enkel, spätestens unsere Urenkel, eines Tages Kopftuch tragen werden. Doch niemand in meinem neuen westdeutschen Umfeld schien mich zu verstehen. [...] Inzwischen, so denke ich, ist es innerparteilich Konsens, dass wir weitere Zuwanderung stoppen müssen, um unsere eigene kulturelle Identität zu bewahren und unseren Fortbestand als deutsches Volk zu sichern. [...] Die Polen haben verstanden, dass es um ihren eigenen Fortbestand als ethnisches und souveränes Volk geht. Bei uns hat es leider die Mehrheit noch nicht verinnerlicht. An diese richte ich nun meinen Appell: Lasst Euch niemals einreden, das es moralisch schlecht oder gar ein Verbrechen sei, sein Volk, seine Kultur und seine Identität bewahren zu wollen! Das Gegenteil ist der Fall. Es ist unser aller Pflicht und Verpflichtung: Im Gedenken an unsere Ahnen und für die Zukunft unserer Kinder.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 147

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