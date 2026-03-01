---
type: zitat
speaker: "[[Christina Baum]]"
date: 2024-08-06
topic: Sonstiges
page_bfv: 785
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 6.8.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Polizei stürmt erneut in voller Montur eine vollständig friedliche Veranstaltung Liebe Polizisten, was ist mit euch los? Seid ihr nur noch Erfüllungsgehilfen dieser deutschlandfeindlichen autoritären Berliner Clique oder habt ihr auch noch ein Gewissen? [...] Der Aktivist Martin Sellner liest aus seinem Buch vor und wird plötzlich durch die Polizei aufgrund von staatlicher Willkür nicht nur des Saales, sondern der Gemeinde verwiesen. Sellner war gerade dabei, die Repression gegenüber der Familie Elsässer zu schildern, als die Truppen den Saal stürmten. Besser als alle Worte dieser Welt kann man der Öffentlichkeit nicht zeigen, welchen autoritären Weg Deutschland unter diese Regierung eingeschlagen hat. [...] Martin Sellner wird gestärkt aus diesem Angriff hervorgehen und die Kritiker dieses Systems werden lauter und stärker werden, bis dieses Berliner Unrecht endlich beendet sein wird. Ich verurteile diese Maßnahme gegen Martin Sellner auf das Schärfste, so wie ich es mit jeder anderen totalitären Maßnahme auch tun würde und ich werde mich immer jeder Form von totalitärer Entwicklung entgegen stellen.

**Parser-Notiz:** Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[Polizei stürmt erneut in voller Montur eine vollst]]

**SPIEGEL-Notiz:** Gutachten Seite: 785

**Verfassungsschutz Kategorisierung:** Sonstiges.

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