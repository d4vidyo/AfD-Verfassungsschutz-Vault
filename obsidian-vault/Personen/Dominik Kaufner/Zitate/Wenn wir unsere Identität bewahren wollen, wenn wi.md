---
type: zitat
speaker: "[[Dominik Kaufner]]"
date: 2023-02-11
topic: Menschenwürde
page_bfv: 252
source: 'Beitrag auf freilich-magazin.com'
status: Unbewertet
---

# Zitat: [[Dominik Kaufner]] vom 11.2.2023 veröffentlicht auf: 'Beitrag auf freilich-magazin.com'
> [!quote] Aussage
>Wenn wir unsere Identität bewahren wollen, wenn wir nicht zur Minderheit im eigenen Land werden wollen, dann gibt es nur eine Möglichkeit: Konsequente Remigration.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 252

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