---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2024-11-25
topic: Demokratieprinzip
page_bfv: 954
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 25.11.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Diese zwei Meldungen stehen repräsentativ für die politische Kultur der deutschen Polit-Elite seit Generationen: Alles für andere, nichts für die eigenen Leute. Von Linkspartei bis CDU - die Kartellparteien können nicht anders und werden für immer ausschließlich antideutsch handeln. Weil die AfD hier eine Ausnahme bildet, werden wir nicht nur politisch, sondern auch geheimdienstlich bekämpft. In ihrer Vorstellung ist es geradezu antisozial, für das eigene Volk einzustehen - ungefähr so, wie ein misshandeltes Kind als erwachsener Mensch aggressiv auf genuine Zuwendung reagiert, weil es Gewalt für eine normale zwischenmenschliche Beziehung hält. Wir müssen die Kartellpolitiker vollständig absetzen. Deswegen: Werdet Mitglied in der AfD, engagiert euch, macht mit bei der Rettung unseres Landes! Jeder wird gebraucht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 954

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