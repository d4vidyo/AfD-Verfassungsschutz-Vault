---
type: zitat
speaker: "[[Martin Renner]]"
date: 2022-06-11
topic: Demokratieprinzip
page_bfv: 599
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 11.6.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Höchste Zeit, umzudenken und zu kämpfen. Die NED (Neue Einheitspartei Deutschlands) führt unseren Staat, unsere Nation und unsere Gesellschaft geplant und willentlich in den Abgrund. Aus reiner Machtgewinnungs- und Machternaltungsabsicht und aus Opportunitätsgründen zerstören diese Politiker der NED alles, was die Grundlagen unseres gemeinschaftlichen Lebens ausmachen. Nation. Freiheit. Demokratie. Rechtsstaat. Wohlstand. [...] Diese Politiker planen sehenden Auges, dass die Gemeinschaft unserer Bürger - vornehmlich die unteren und die mittleren Bürgerschichten - völlig verarmen, um sie dadurch widerstandslos kollektivieren zu können. [...] Es geht um den grundsätzlichen Widerstand (selbstverständlich demokratisch) gegen die freiheitszerstörende, demokratieschwächende, rechtsstaatsverachtende und wohlstandsvernichtende Politik der NED-Parteien. Und ja, meinetwegen soll der instrumentalisierte Verfassungsschutz eine solche, eben getätigte, Positionsbeschreibung unserer alternativen politischen Aufgabe als 'staatsdelegitimierende' Verlautbarung einstufen. Zur Not gehe ich wegen meiner hier gemachten Aussagen auch in einen der zukünftig neu eingerichteten Gulags.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 599

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