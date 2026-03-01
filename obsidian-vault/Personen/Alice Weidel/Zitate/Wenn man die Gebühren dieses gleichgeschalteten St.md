---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2024-08-25
topic: Demokratieprinzip
page_bfv: 595
source: 'Interview'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 25.8.2024 veröffentlicht auf: 'Interview'
> [!quote] Aussage
>Wenn man die Gebühren dieses gleichgeschalteten Staatsfunks - Ne? Also, Regierungskritik ist da ja nicht erlaubt. Nicht wahr? - Wenn man die nicht zahlt, dann landen Sie einfach ähm, einfach im Knast. [...] Gegen die eigene Bevölkerung! Und vor allen Dingen gegen Kritiker. Und das kennen wir aus repressiven Regimen. Das ist DDR 2.0, das muss man mal ganz, ganz offen sagen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 595

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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