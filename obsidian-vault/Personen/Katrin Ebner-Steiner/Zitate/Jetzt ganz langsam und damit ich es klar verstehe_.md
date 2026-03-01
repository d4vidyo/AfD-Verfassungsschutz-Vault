---
type: zitat
speaker: "[[Katrin Ebner-Steiner]]"
date: 2025-01-22
topic: Menschenwürde
page_bfv: 935
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Katrin Ebner-Steiner]] vom 22.1.2025 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Jetzt ganz langsam und damit ich es klar verstehe: mehr als HUNDERT Jugendliche jagen einen 13-Jährigen, um ihn in Berlin abzustechen!? Der Junge flüchtet in Todesangst in einen EDEKA und versteckt sich zwischen Getränkekästen. Eine POLIZEIHUNDERTSCHAFT rückt an, um Bio-Deutsches Blut vorm jämmerlichen Verrecken zu retten. Und es wird klar: der Geburtendschihad ist längst zum Bürgerkrieg mutiert. Unsere Jungs sind nicht mehr sicher. Je jünger der Jahrgang desto gefährdeter. Deutschland! WACH AUF!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 935

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