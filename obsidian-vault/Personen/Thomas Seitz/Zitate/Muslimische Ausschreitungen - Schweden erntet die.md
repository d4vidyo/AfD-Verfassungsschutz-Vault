---
type: zitat
speaker: "[[Thomas Seitz]]"
date: 2022-04-20
topic: Menschenwürde
page_bfv: 450
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Thomas Seitz]] vom 20.4.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Muslimische Ausschreitungen - Schweden erntet die Früchte einer naiven Einwanderungspolitik Von der Migrationshochburg Malmö ausgehend breiten sich seit einer Woche in Schweden schwere Krawalle aus, bei denen bereits zahlreiche Polizisten verletzt und mehrere Polizeifahrzeuge zerstört wurden. [...] Auslöser dieser Proteste war die Ankündigung eines islamkritischen Politikers, bei einer Kundgebung einen Koran anzünden zu wollen. [...] Was in Schweden gerade geschieht, ist die Folge einer naiven Einwanderungspolitik und kann auch in Frankreich, den Niederlanden oder bei uns in Deutschland jederzeit passieren. Es braucht nur geringe Anlässe, um den muslimischen Furor zu wecken, auch bei bereits in Europa Geborenen. Die Gewaltbereitschaft vieler Anhänger des Propheten Mohammed war und ist eine der größten Bedrohungen für Sicherheit und Freiheit weltweit.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 450

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