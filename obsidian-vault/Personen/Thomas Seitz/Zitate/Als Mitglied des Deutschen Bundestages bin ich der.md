---
type: zitat
speaker: "[[Thomas Seitz]]"
date: Nicht Verfügbar
topic: Menschenwürde
page_bfv: 119
source: 'Facebook-Info'
status: Unbewertet
---

# Zitat: [[Thomas Seitz]] vom None veröffentlicht auf: 'Facebook-Info'
> [!quote] Aussage
>Als Mitglied des Deutschen Bundestages bin ich der Vertreter des ganzen Volkes. Gemeint ist damit des ganzen Deutschen Volkes. Also alle, die schon länger hier leben. Integrierte Migranten also keine Özils, die sich weiter als Türken sehen - gehören selbstverständlich auch dazu. Reine Passdeutsche formal auch - leider.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 119

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