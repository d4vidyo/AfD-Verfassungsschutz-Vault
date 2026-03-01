---
type: zitat
speaker: "[[Christine Anderson]]"
date: 2025-01-11
topic: Demokratieprinzip
page_bfv: 958
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Christine Anderson]] vom 11.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Unser Antrag wurde fristgerecht eingereicht, aber versehentlich hat er keinen Eingang in das Antragsbuch gefunden, weswegen ihn wir jetzt als Saalantrag stellen. Die Antragssteller, als da wären: meine Wenigkeit, der KV Fulda, Andreas Lichert, Jan Nolte, Uwe Schulz, Pierre Lamely, Nicole Hess, Anja und Arno Arndt, beantragen, in unser Wahlprogramm die Abschaffung des §188 StGB - im Volksmund als "Majestätsbeleidigung" bekannt - aufzunehmen. Der Punkt ist einfach der, liebe Freunde. Der Bundeswirtschaftsminister Robert Habeck hört ja nun nicht auf, ein Schwachkopf zu sein, nur weil er diese, wie ich finde, doch sehr zutreffende Bezeichnung strafrechtlich sanktionieren lässt. Nein, es macht es schlimmer. Es macht ihn zu einem totalitären Schwachkopf. Liebe Freunde, ein freiheitlicher Rechtsstaat, der strafrechtliche Normen missbraucht, um Bürger wegen Kritik an Regierungsmitgliedern zu schikanieren, zu verfolgen und zu kriminalisieren, hört eben auf, ein freiheitlicher Rechtsstaat zu sein. Durch die Aufnahme dieser Forderung unterstreichen wir einmal mehr, dass einzig und allein die AfD für den freiheitlichen Rechtsstaat einsteht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 958

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