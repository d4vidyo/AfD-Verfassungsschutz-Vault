---
type: zitat
speaker: "[[Oliver Kirchner]]"
date: 2022-08-28
topic: Menschenwürde
page_bfv: 130
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Oliver Kirchner]] vom 28.8.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Ich möchte, dass Deutschland und ich möchte, dass Sachsen-Anhalt deutsch bleibt! Denn wer hier die Veränderung dieses Staatsvolks betreibt, der ist verfassungswidrig. Dieses Staatsvolk hat es nicht verdient, hier mit Zuwanderung vollgestopft zu werden und für unsere eigenen Bürger kein Geld mehr zu haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 130

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