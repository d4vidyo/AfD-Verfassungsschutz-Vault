---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2022-11-25
topic: Menschenwürde
page_bfv: 331
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 25.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>An jedem dritten Tag wird in Deutschland eine Frau ermordet. An jedem einzelnen Tag werden im Durchschnitt zwei Mädchen oder Frauen in Deutschland on Männergruppen vergewaltigt. Jeder zweite Tatverdächtige hat keine deutsche Staatsangehörigkeit. Am häufigsten kommen die Männer aus islamischen Ländern: Afghanistan, Syrien, Irak. Diese Taten werden verharmlost, als Einzelfälle abgetan, die Nationalität der Täter nicht mehr erwähnt. Die Gründe für die Rückkehr primitiver Frauenverachtung liegen auf der Hand: Wir haben eine Masseneinwanderung aus Regionen in denen Frauen wie Dreck behandelt werden. Sie sind verfügbare Sklavinnen, Menschen zweiter Klasse, die man im Kindesalter zwangsverheiraten kann, die man auch mal aus Gründen der Ehre ermorden darf. [...] Die Sicherheit von Frauen im öffentlichen Raum ist schon lange nicht mehr gewährleistet. Aber auch die Opfer häuslicher Gewalt kommen aus den genannten frauenfeindlichen Kulturraum. [...] Es sind die Regierungen der letzten Jahre, die mit ihrer falschen und tödlichen Toleranz, die archaische Vorstellungen und die Unterdrückung der Frau millionenfach nach Deutschland holen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 331

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