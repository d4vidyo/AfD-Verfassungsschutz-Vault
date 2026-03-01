---
type: zitat
speaker: "[[Hans-Thomas Tillschneider]]"
date: 2023-11-09
topic: Nationalsozialismus
page_bfv: 687
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Hans-Thomas Tillschneider]] vom 9.11.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Brecht gegen Schuldkult! Ich hör die Herrn in Downingstreet noch schelten! Weil Ihr's gelitten, trüget Ihr die Schuld. Wie dem nun sei: Die Herren schelten selten der Völker unerklärliche Geduld. Das sind meine Lieblingsverse von Berthold Brecht. Sie stehen in der Kriegsfibel neben einem Hitlerbild und eignen sich hervorragend, um den herrschenden Schuldkult zu hinterfragen. Die Schuldzuweisung an das deutsche Volk durch die Siegermächte teilt Brecht nicht. Er bezeichnet die Siegermächte eher abfällig als scheltende 'Herren in Downingstreet' und gibt ihre Schuldzuweisung nur im Konjunktiv wieder. Das 'Wie dem nun sei' der dritten Zeile schreibt den Zweifel fest und suspendiert ihn zugleich. Denn das Fazit und Faktum, an dem sich jeder, der an der deutschen Schuld zweifelt, festhalten soll, ist der Umstand, daß die Herren in aller Regel zufrieden damit sind, wenn das Volk keinen Widerstand leistet. So leichtfüßig ist noch kein Dichter mit der deutschen Vergangenheit umgegangen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 687

**Verfassungsschutz Kategorisierung:** Position zum Nationalsozialismus.

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