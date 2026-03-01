---
type: zitat
speaker: "[[Lena Kotré]]"
date: 2025-01-22
topic: Menschenwürde
page_bfv: 913
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Lena Kotré]] vom 22.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Das sind keine Einzelfälle! Diese Morde passieren systematisch und werden immer häufiger, bis wir endlich die Remigration durchsetzen und unser Land wieder unter Kontrolle bekommen. Selbst der Anschlag von Magdeburg ist mittlerweile aus den Medien und den Köpfen verschwunden - so häufig töten Migranten in Deutschland! Die beiden Toten von heute gehen auf das Konto von CDU, SPD, Grünen und FDP.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 913

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