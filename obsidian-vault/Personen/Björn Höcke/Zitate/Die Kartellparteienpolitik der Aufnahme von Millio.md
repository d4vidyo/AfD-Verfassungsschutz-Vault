---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-23
topic: Menschenwürde
page_bfv: 917
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 23.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Kartellparteienpolitik der Aufnahme von Millionen illegaler Immigranten aus fremden Kulturen zerstört den im Grundgesetz beschriebenen Souverän und Staat. Sie ist in der Tat verfassungswidrig und extremistisch! [...] Die unschuldigen Opfer der immigrationsbedingten Gewalt in Deutschland werden nicht mehr lebendig werden. Und die Toten von Aschaffenburg werden nicht die letzten gewesen sein. Trotzdem haben die Menschen in Deutschland am 23. Februar die Möglichkeit den fatalsten Irrweg der deutschen Nachkriegsgeschichte zu beenden - den der identitäts- und staatsauflösenden Politik der offenen Grenzen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 917

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