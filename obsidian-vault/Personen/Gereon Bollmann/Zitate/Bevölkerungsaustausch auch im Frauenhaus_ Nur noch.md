---
type: zitat
speaker: "[[Gereon Bollmann]]"
date: 2024-03-01
topic: Menschenwürde
page_bfv: 197
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Gereon Bollmann]] vom 1.3.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Bevölkerungsaustausch auch im Frauenhaus: Nur noch ein Drittel Deutsche [...] Der AfD-Bundestagsabgeordnete Gereon Bollmann, Mitglied im Familienausschuss, erklärt dazu: 'Die Trendrichtung ist damit auch in den deutschen Frauenhäusern klar: Einheimische raus, Fremde rein. Für einheimische Frauen sind kaum noch Kapazitäten übrig. Dieser Trend muss schnellstmöglich umgedreht werden. [...] Die Gesellschaft kann nicht weiter hinnehmen, dass eine schutzsuchende deutsche Frau mit ihren Kindern abgewiesen wird, weil mehr als die Hälfte der Plätze im Frauenhaus von Frauen und Kindern mit Migrationshintergrund besetzt ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 197

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