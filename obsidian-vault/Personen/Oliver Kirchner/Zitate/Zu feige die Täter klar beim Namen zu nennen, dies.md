---
type: zitat
speaker: "[[Oliver Kirchner]]"
date: 2023-01-03
topic: Menschenwürde
page_bfv: 278
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Oliver Kirchner]] vom 3.1.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Zu feige die Täter klar beim Namen zu nennen, dieses Staatsfernsehen. Es waren kriminelle Zuwanderer, denen unser friedliches Zusammenleben vollkommen egal ist. Wir brauchen kein bundesweites Böllerverbot, sondern ein bundesweites Einreiseverbot für diese illegalen Armuts-, Wirtschafts- und Sozialeinwanderer. Vor allem aber brauchen wir drakonische Strafen und eine Abschiebeoffensive für solche Typen. Schluß mit der Verharmlosung dieser Straftaten gegen unsere Ordnungskräfte. Wenn ich schon höre, es wären gruppendynamische Prozesse nach zwei Jahren Pandemie. Schwachsinn! Es sind nicht integrierbare Zuwanderer! Also, abschieben, abschieben, abschieben lautet die Botschaft.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 278

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