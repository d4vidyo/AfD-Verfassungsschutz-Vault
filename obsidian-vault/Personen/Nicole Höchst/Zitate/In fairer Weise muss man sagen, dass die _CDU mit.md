---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2023-11-22
topic: Menschenwürde
page_bfv: 246
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 22.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>In fairer Weise muss man sagen, dass die #CDU mit Angela Merkel diese Weichen für Deutschland bereits gestellt hatte. Die #Ampel ist nur mit dem #Abwracken, #Zerstören und #Vernichten von #Volk, #Volkseigentum, #Wirtschaft, #Sprache, #Kultur, #Bildung, #Familie, #Tradition und #Generationenzusammenhalt VIEL effizienter, effektiver und erfolgreicher

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 246

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