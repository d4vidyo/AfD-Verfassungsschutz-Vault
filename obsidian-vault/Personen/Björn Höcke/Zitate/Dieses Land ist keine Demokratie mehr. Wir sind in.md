---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2021-09-13
topic: Demokratieprinzip
page_bfv: 564
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 13.9.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Dieses Land ist keine Demokratie mehr. Wir sind in einem Übergangsstadium Richtung einem sanften Totalitarismus. Die Kartellparteien haben das Land heruntergewirtschaftet [...] Und gleichzeitig arbeiten sie daran, dieses globale Establishment und seine Dienstklasse hier in der Bundesrepublik Deutschland, die Kartellparteien, allmählich einen Überwachungsstaat aufzubauen. Sie [die USA] marschieren ein, sie zerstören, sie besiegen, sie besetzen, dann wird die Regierung des besetzten Landes beseitigt und dem Land wird eine neue Regierung aufgezwungen, eine neue Staatsform aufgezwungen. Meistens eine sogenannte parlamentarische Demokratie, eine Herrschaftsform, eine Staatsform, die man von außen wunderbar kontrollieren kann. [...] Liebe Freunde, wir kennen dieses Vorgehen und diese Einschätzung der Amerikaner in Afghanistan auch aus der deutschen Geschichte. Nach dem Zweiten Weltkrieg, da sollten auch wir umerzogen werden. Und diese Umerziehung war eine wissenschaftlich-psychologisch geplante Maßnahme, ein wissenschaftlich exakt geplantes, psychologisch ausgeklügeltes Verfahren und Programm.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 564

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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