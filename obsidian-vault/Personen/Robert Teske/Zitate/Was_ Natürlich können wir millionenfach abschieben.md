---
type: zitat
speaker: "[[Robert Teske]]"
date: 2025-01-15
topic: Menschenwürde
page_bfv: 929
source: 'TikTok'
status: Unbewertet
---

# Zitat: [[Robert Teske]] vom 15.1.2025 veröffentlicht auf: 'TikTok'
> [!quote] Aussage
>Was? Natürlich können wir millionenfach abschieben! Alleine über den Berliner Flughafen werden jedes Jahr 23 Millionen Passagiere bewegt. Und in Frankfurt sind es sogar 59 Millionen! Remigration wäre also ohne Probleme machbar und bietet nur Vorteile: Mehr Platz, günstigere Mieten, weniger Kriminalität, geringere Steuerlast. Das Problem ist, es ist einfach nicht gewollt. Viele Menschen profitieren nämlich von dieser Masseneinwanderung und wollen, dass es genauso weitergeht. Mit uns, mit der Alternative für Deutschland, wird es das nicht geben. Denn wir stehen für eine Kehrtwende in der Migrationspolitik. Wenn Du diese Kehrtwende auch möchtest, dann musst du am 23. Februar zur Bundestagswahl die Alternative für Deutschland wählen. Und zwar mit beiden Stimmen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 929

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