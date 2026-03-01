---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-08-12
topic: Menschenwürde
page_bfv: 297
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 12.8.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Messermigration beenden - Innere Sicherheit wiederherstellen. Schützt unsere Mitbürger! [...] Tägliche Messerstechereien, Morddrohungen gegen Islamkritiker, die nur mit massiven Polizeischutz durchs Leben kommen und ein heutiges Messerattentat auf einen islamkritischen Autor in New York komplettieren die falsche Migrationspolitik von westlichen Eliten. [...] Wir werden die Messermigration aus aller Herren Länder stoppen, die Grenzen schützen und kriminelle Straftäter bestmöglich abschieben! [...] Der tägliche Messerterror muss sofort beendet werden!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 297

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