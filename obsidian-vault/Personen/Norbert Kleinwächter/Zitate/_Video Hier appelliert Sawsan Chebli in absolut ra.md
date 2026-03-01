---
type: zitat
speaker: "[[Norbert Kleinwächter]]"
date: 2025-01-21
topic: Menschenwürde
page_bfv: 893
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Norbert Kleinwächter]] vom 21.1.2025 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>\<Video Hier appelliert Sawsan Chebli in absolut rassistischer Art und Weise an die dritte und vierte Generation der Einwanderer, dass sie trotz aller Frustration nicht aufgeben sollen, sondern durch Demografie, also Kinderkriegen, Fakten schaffen sollen. Und Fakten schaffen bedeutet natürlich eben diese Unterwanderung unseres Landes mit Ausländern, mit Migranten unumkehrbar zu machen. [...] Und während das ja immer von den migrantischen Communities und auch einer Sawsan Chebli weit von sich gewiesen worden war, dass in irgendeiner Weise eine Absicht eines, Stichwort Bevölkerungsaustausches bestehe, argumentiert sie hier selbst damit. [...] Und wenn Demografie tatsächlich Fakten schafft, warum sollten wir uns als Deutsche gegen solche Fakten bitteschön nicht wehren können?\>

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 893

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