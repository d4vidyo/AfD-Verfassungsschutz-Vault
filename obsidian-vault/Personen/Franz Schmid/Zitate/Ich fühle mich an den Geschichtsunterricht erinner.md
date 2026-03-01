---
type: zitat
speaker: "[[Franz Schmid]]"
date: 2024-10-19
topic: Sonstiges
page_bfv: 786
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Franz Schmid]] vom 19.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ich fühle mich an den Geschichtsunterricht erinnert. In der sogenannten Vormärz-Zeit terrorisierten absolutistische Fürsten patriotisch-freiheitliche Bürger. Heute sind es keine demokratiefeindlichen Monarchen, sondern Machthaber der Kartellparteien, wie Katrin Albsteiger und ihre Antifa-Helfer, die friedliche Aktivisten unterdrücken. Ich werde mein Recht als Abgeordneter nutzen und der Söder-Regierung unangenehme Fragen zu der Schande von Neu-Ulm stellen: Wie oft in der Vergangenheit wurden Versammlungen durch vermummte Polizisten gesprengt, angeblich weil keine Schanklizenz vorlag und wie verhältnismäßig ist ein solches Vorgehen des Staates? Widerstand gegen das drohende Ende der Meinungsfreiheit ist Pflicht!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 786

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