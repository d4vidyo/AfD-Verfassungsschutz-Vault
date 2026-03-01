---
type: zitat
speaker: "[[Fabian Küble]]"
date: 2022-07-20
topic: Menschenwürde
page_bfv: 145
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Fabian Küble]] vom 20.7.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Ampel will Deutschland mit einer weiteren Masseneinwanderungswelle fluten. Um dieses Ziel zu erreichen propagiert die neue afrikanisch-bundesrepublikanische Staatsministerin der Grünen in Schleswig-Holstein Toure offen die Umvolkung (zu englisch: Resettlement). Zugleich soll alles und jeder nach kürzester Zeit bedingungslos eingebürgert werden. Die Antideutschen hören nicht auf, bevor Deutschland vollständig entdeutscht ist. Das ehemals als Deutschland bekannte kulturelle Herz Europas soll als Migrantistan zum offenen Siedlungsgebiet für alle Welt umgewandelt werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 145

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