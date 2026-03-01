---
type: zitat
speaker: "[[Hannes Gnauck]]"
date: 2022-01-31
topic: Demokratieprinzip
page_bfv: 611
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hannes Gnauck]] vom 31.1.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Und wir sagen 'Nein' zur Aushöhlung unserer Demokratie und dem Abdriften dieser Regierung in ein totalitäres Regime. Und gleichzeitig, liebe Freunde, sind wir heute hier, um 'Ja' zu sagen. Wir sagen 'Ja' zur Volksherrschaft, zu wahrer Demokratie. [...] Die Älteren unter euch – ich bin jetzt ein junger Mann, der nach der Wende geboren ist – aber die Älteren unter euch werden sich noch erinnern: War das vielleicht nicht auch mal das Versprechen der Wiedervereinigung? Rechtsstaat, Demokratie, Meinungsfreiheit, keine Medien mehr, die jeden Protest zum Putsch umdichten und kein Geheimdienst mehr, der friedliche Spaziergänger als Staatsfeinde diffamiert. Man schaue sich mittlerweile heute an, wo wir, man möchte fast sagen, leider wieder stehen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 611

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