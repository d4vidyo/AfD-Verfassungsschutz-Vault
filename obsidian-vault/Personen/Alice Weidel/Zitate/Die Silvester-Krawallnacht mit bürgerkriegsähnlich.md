---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2023-01-07
topic: Menschenwürde
page_bfv: 321
source: 'www.jungefreiheit.de'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 7.1.2023 veröffentlicht auf: 'www.jungefreiheit.de'
> [!quote] Aussage
>Die Silvester-Krawallnacht mit bürgerkriegsähnlichen Zuständen und staatlichem Kontrollverlust insbesondere in Berlin hat schonungslos die tiefe Verachung bestimmter Migrantenmilieus gegenüber unserem Staat offengelegt. [...] Von den allein in Berlin festgenommenen 145 Gewalttätern waren laut Polizei 100 Ausländer, rund die Hälfte davon Afghanen und Syrer. Viele der 45 deutschen Staatsbürger dürften zudem einen Migrationshintergrund haben. Diese Zahlen machen nicht nur die Folgen einer verantwortungslosen Politik der offenen Grenzen deutlich, sondern auch das Scheitern der Integrationspolitik. Unsere Art zu leben, ist in Gefahr. Unkontrollierte Masseneinwanderung importiert Gewalt, Kriminalität und destabilisiert die Aufnahmegesellschaft. Unser Rechtsstaat, unsere Art zu leben und unsere Werte sind ernsthaft in Gefahr und es wird allerhöchste Zeit, die Dinge jenseits politisch korrekter Sprach- und Denkverbote beim Namen zu nennen: Das realitätsfremde Experiment eines ideologiegetriebenen Multikulturalismus ist gescheitert

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 321

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