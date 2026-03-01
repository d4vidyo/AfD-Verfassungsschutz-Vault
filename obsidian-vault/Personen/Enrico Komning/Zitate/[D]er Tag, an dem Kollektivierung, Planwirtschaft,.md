---
type: zitat
speaker: "[[Enrico Komning]]"
date: 2022-10-03
topic: Demokratieprinzip
page_bfv: 554
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Enrico Komning]] vom 3.10.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>[D]er Tag, an dem Kollektivierung, Planwirtschaft, Willkür, Meinungsdiktat und Gängelung in der Deutschen sogenannten Demokratischen Republik überwunden wurden. So glaubten wir. Und heute ist das alles in ähnlicher Gestalt wieder da. Wie damals unterliegen wir wieder einem Willkürregime, das für sich in Anspruch nimmt, nur das Beste für den Menschen zu wollen und zu tun, das Begriffe wie Demokratie, Toleranz, Vielfalt, neuerdings auch Antifaschismus für sich besetzt, aber für den eigenen Machtgehalt, Machterhalt genau das Gegenteil meint. Bei dem nicht das Interesse und das Wohl des eigenen deutschen Volkes im Vordergrund steht, sondern ein links-grünes Regime, dass Deutschland zum Spielball anderer Weltmächte macht und ohne Rücksicht auf unwiederbringliche Verluste den Ausverkauf und den Niedergang der Deutschen in Kauf nimmt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 554

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