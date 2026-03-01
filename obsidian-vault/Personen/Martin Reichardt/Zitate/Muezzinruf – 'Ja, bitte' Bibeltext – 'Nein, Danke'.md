---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2022-11-02
topic: Menschenwürde
page_bfv: 247
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 2.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Muezzinruf – 'Ja, bitte' Bibeltext – 'Nein, Danke' Im Koalitionsvertrag hat die Ampel festgelegt, dass die 'Vielfalt' und 'multikulturelle Gesellschaft' in Deutschland gefördert werden soll. Auch im Migrationspakt ist dies festgeschrieben. Diese Förderung bedeutet für unsere Regierung, die Bekämpfung von Traditionen und Werten. Die Bekämpfung unserer nationalen Identität. Jetzt bekämpft Claudia Roth das goldene Kreuz und die Zitate aus der Bibel, die auf der Kuppel des Berliner Stadtschloss zu sehen sind. Diese widersprächen, so Frau Roth, der 'Weltoffenheit'. Es wird an einem 'Kunstprojekt' gearbeitet, dass die Bibelverse überblenden sollen. Schon im Vorwege ist die Stiftung Huboldtforum, vor den Deutschlandzerstörern auf die Knie gegangen. [...] Die Bibel wird geschliffen, der Islam aber, der tatsächlich einen Alleingültigkeits- und Herrschaftsanspruch hat, wird gefördert, der Muezzinruf, darf in Köln erschallen. [...] Die Deutschlandzerstörer sind an der Macht, sie zerstören unsere wirtschaftliche Zukunft, unsere Kultur, unsere Heimat, unsere Identität. Wir dürfen nicht nachlassen, in unseren politischen Kampf für unsere Heimat. Jeden Montag werden wir mehr! Holen wir uns unser Land zurück!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 247

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