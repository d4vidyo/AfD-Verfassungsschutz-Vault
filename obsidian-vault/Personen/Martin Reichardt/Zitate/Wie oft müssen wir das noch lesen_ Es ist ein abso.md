---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2022-12-07
topic: Menschenwürde
page_bfv: 300
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 7.12.2022 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Wie oft müssen wir das noch lesen? Es ist ein absolut sinnloses #Verbrechen an einem jungen #Mädchen, das einfach auf dem Weg zur #Schule war. \<xxx\> ist nur 14 Jahre alt geworden. Ermordet von einem Mann aus #Eritrea. Dem überlebenden Mädchen wurde auch ihr Leben genommen, denn sie wird ihr ganzes Leben mit den Folgen dieses Verbrechens zu kämpfen haben. Das Geschrei bei Politikern und in den #Medien war 2018 groß, als Alice Weidel von 'Messermännern' sprach. Der Täter ist einer dieser 'Messermänner‘.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 300. Der im Original erwähnte Name wurde durch den SPIEGEL mit \<xxx\> ersetzt.

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