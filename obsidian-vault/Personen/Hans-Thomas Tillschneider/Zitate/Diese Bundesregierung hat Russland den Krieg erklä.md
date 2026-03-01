---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2023-02-20
topic: Demokratieprinzip
page_bfv: 632
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 20.2.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Diese Bundesregierung hat Russland den Krieg erklärt. Noch viel mehr aber hat diese Bundesregierung dem eigenen Volk den Krieg erklärt. [...] Wenn wir eine Regierung haben, die gegen uns Krieg führt, dann führen wir Krieg gegen diese Regierung. [...] Es muss jede Bundesregierung, die aus Altparteien gebildet wird, vertrieben werden. Wir sind gekommen, diese Gestalten aus ihren Sesseln zu vertreiben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 632

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