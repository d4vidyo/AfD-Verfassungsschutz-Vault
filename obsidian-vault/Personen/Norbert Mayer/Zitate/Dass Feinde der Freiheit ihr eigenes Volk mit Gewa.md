---
type: zitat
speaker: "[[Norbert Mayer]]"
date: 2021-12-07
topic: Demokratieprinzip
page_bfv: 610
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Norbert Mayer]] vom 7.12.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Dass Feinde der Freiheit ihr eigenes Volk mit Gewalt unterdrücken, werden wir niemals hinnehmen! [...] Warum sich das für mich wie ein Déjà-vu anfühlt? Weil ich auch vor über 30 Jahren schon mal auf der Straße gegen ein totalitäres Unrechtsregime protestierte, welches sich mit Repressalien gegen Andersdenkende an die Macht klammerte: auf den Montagsdemos im Herbst 1989!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 610

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