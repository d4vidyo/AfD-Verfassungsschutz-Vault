---
type: zitat
speaker: "[[Reimond Hoffmann]]"
date: 2025-01-20
topic: Menschenwürde
page_bfv: 894
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Reimond Hoffmann]] vom 20.1.2025 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Sawsan Chebli will euch euer Land wegnehmen. Sie sagt den Migranten: kämpft dafür! Demografie wird Fakten schaffen. [...] Was bei der politischen Rechten als Verschwörungstheorie durch den Verfassungsschutz eingestuft wird, nämlich die Ersetzungsmigration, genau das befürwortet Sawsan Chebli als SPD-Politikerin. Sie hetzt somit gegen das deutsche Volk und wünscht eine Minorisierung. Kämpfen wir dagegen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 894

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