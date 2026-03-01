---
type: zitat
speaker: "[[Lars Kuppi]]"
date: 2024-06-29
topic: Menschenwürde
page_bfv: 149
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Lars Kuppi]] vom 29.6.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Neubürger' entscheiden die nächste Wahl Werden wir Deutschen zur Minderheit? Die nächste Bundestagswahl wird wahrscheinlich von 'Neubürgern' entschieden. Durch die neuen Turbo-Einbürgerungen könnten 600.000 Migranten bis dahin einen deutschen Pass erhalten. Laut Experten könnte diese Gruppe von Ausländern die Wahl entscheiden, berichtet BILD. Die Zukunft sieht sogar noch düsterer aus, wenn das Verschenken deutscher Pässe nicht sofort gestoppt wird. So haben ausländische Frauen in Deutschland eine erheblich höhere Geburtenquote als deutsche Frauen. In vielen westdeutschen Großstädten sind die deutschen Ureinwohner bereits heute in der Minderheit.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 149

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