---
type: zitat
speaker: "[[Christina Baum]]"
date: 2024-08-06
topic: Rechtsstaatsprinzip
page_bfv: 663
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 6.8.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Polizei stürmt erneut in voller Montur eine vollständig friedliche Veranstaltung Liebe Polizisten, was ist mit euch los? Seid ihr nur noch Erfüllungsgehilfen dieser deutschlandfeindlichen autoritären Berliner Clique oder habt ihr auch noch ein Gewissen? [...] Der Aktivist Martin Sellner liest aus seinem Buch vor und wird plötzlich durch die Polizei aufgrund von staatlicher Willkür nicht nur des Saales, sondern der Gemeinde verwiesen. Sellner war gerade dabei, die Repression gegenüber der Familie Elsässer zu schildern, als die Truppen den Saal stürmten. Besser als alle Worte dieser Welt kann man der Öffentlichkeit nicht zeigen, welchen autoritären Weg Deutschland unter diese Regierung eingeschlagen hat. [...] Ich verurteile diese Maßnahme gegen Martin Sellner auf das Schärfste, so wie ich es mit jeder anderen totalitären Maßnahme auch tun würde und ich werde mich immer jeder Form von totalitärer Entwicklung entgegen stellen. Allen Polizisten gebe ich das Zitat von Angela Merkel mit auf dem Weg, das aus einer Rede zum Feierlichen Gelöbnis der Bundeswehr, am 20. Juli 2019 in Berlin, stammt: 'Es gibt Momente, in denen Ungehorsam eine Pflicht sein kann – Momente, in denen man nur dann Anstand und Menschlichkeit wahrt, wenn man sich gegen einen Befehl, gegen den Druck von Vorgesetzten oder auch den Druck der Masse auflehnt und gegenhält. Es gibt Momente, in denen der Einzelne die moralische Pflicht hat, zu widersprechen und sich zu widersetzen...'

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 663

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Rechtsstaatsprinzip.

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