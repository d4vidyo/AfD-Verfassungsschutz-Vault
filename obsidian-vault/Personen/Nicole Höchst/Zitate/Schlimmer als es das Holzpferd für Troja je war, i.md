---
type: zitat
speaker: "[[Nicole Höchst]]"
date: 2023-01-10
topic: Menschenwürde
page_bfv: 138
source: 'Youtube, Deutschland Kurier'
status: Unbewertet
---

# Zitat: [[Nicole Höchst]] vom 10.1.2023 veröffentlicht auf: 'Youtube, Deutschland Kurier'
> [!quote] Aussage
>Schlimmer als es das Holzpferd für Troja je war, ist der Migrationskult für Deutschland. Und es hilft erfahrungsgemäß auch nicht, wenn man alle Täter und Integrationsunwilligen mit der deutschen Staatsbürgerschaft bewirft. Klar, das bereinigt zwar die Kriminalitätsstatistiken, aber die Problematik bleibt natürlich bestehen. [...] Ich persönlich verachte diese 'Deutschland-verrecke-ldeologie', die hinter all dem steht, und ich verachte eine Regierung, die genau nach dieser Ideologie zum Schaden des deutschen Volkes, entgegen ihres Amtseides handelt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 138

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