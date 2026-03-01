---
type: zitat
speaker: "[[Birgit Bessin]]"
date: 2024-02-07
topic: Sonstiges
page_bfv: 837
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Birgit Bessin]] vom 7.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Erinnert euch zurück, wer als kritischer Bürger in der Corona-Zeit sich mit ähnlichen Anfeindungen unberechtigterweise auseinandersetzen musste ...! Ich kenne nur JAIer die auf dem Boden des Grundgesetzes stehen. Deshalb stehe ich auch weiter zu unserer JA.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 837

**Verfassungsschutz Kategorisierung:** Sonstiges.

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