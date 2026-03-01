---
type: zitat
speaker: "[[Richard Graupner]]"
date: 2025-01-20
topic: Menschenwürde
page_bfv: 893
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Richard Graupner]] vom 20.1.2025 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Nun ist es Frau Chebli nicht vorzuwerfen, dass sie eine Tatsache benennt. Der Bevölkerungsaustausch ist Realität und er ist in vollem Gange. Frau Chebli weiß das. Wir wissen das. Aber Frau Chebli freut sich darüber und sie fordert indirekt mehr davon. Die AfD hingegen fordert aus diesem Grunde Remigration. Denn auch Remigration wird Fakten schaffen! Fakten jedoch zugunsten, und nicht zu Lasten des deutschen Volkes. — Darum am 23.02. mit beiden Stimmen AfD

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