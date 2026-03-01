---
type: zitat
speaker: "[[Andreas Galau]]"
date: 2022-06-03
topic: Menschenwürde
page_bfv: 391
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Andreas Galau]] vom 3.6.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Auch bei der Einwanderung hat die AfD bei allen Kritikpunkten bei der bewusst ungesteuerten gesellschaftszerstörende Zuwanderung illegaler Migranten Recht behalten. Millionen von Menschen wurden ohne Rücksichtnahme auf Qualifikation und kultureller Kompatibilität in unser kleines Land geschleust. [...] Auch hier wieder: mit einer AfD in Regierungsverantwortung hätte es eine Massenzuwanderung niemals gegeben!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 391

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