---
type: zitat
speaker: "[[Mariana Harder-Kühnel]]"
date: 2024-02-16
topic: Menschenwürde
page_bfv: 266
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Mariana Harder-Kühnel]] vom 16.2.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Massenmigration bedeutet explodierende Kriminalität, Zerstörung unseres Sozialstaates, Import fremder Konflikte in unser Land, migrantische Clanbildung, niedrigere Löhne durch Lohndumping, steigende Mieten und Immobilienpreise durch Wohnraummangel. Und das neue Staatsangehörigkeitsrecht, das verewigt diese Entwicklung. Und genau das ist nicht in unserem Interesse, liebe Freunde. [...] Sonst wird Deutschland zu einem Kalifat und wir wollen kein Kalifat. Wir wollen ein Deutschland, das deutsch bleibt, liebe Freunde.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 266

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