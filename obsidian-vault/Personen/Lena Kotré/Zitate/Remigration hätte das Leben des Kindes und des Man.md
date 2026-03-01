---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2025-01-22
topic: Menschenwürde
page_bfv: 912
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 22.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Remigration hätte das Leben des Kindes und des Mannes, der versucht hat, das Kind zu beschützen, retten können. Es ist unfassbar und es macht mich als Mutter wahnsinnig betroffen, wenn ich das höre. Man gibt morgens sein Kind in der Kita ab und wird es dann am Abend nicht mehr wiedersehen, weil diese ungezügelte Masseneinwanderung von Messermigranten in unser Land hier Einzug gehalten hat. [...] Wir brauchen keine Zuwanderung aus Afghanistan. Wir brauchen keine Zuwanderung von Menschen, die nichts Gutes hier im Sinne haben. Und wir brauchen schon gar keine Zuwanderung von Messermigranten. [...] Liebe Freunde, das ist eine Machtdemonstration von Messermigranten und es ist auch eine Landnahme von diesen Menschen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 912

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