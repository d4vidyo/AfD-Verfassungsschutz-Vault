---
type: zitat
speaker: "[[Birgit Bessin]]"
date: 2023-04-16
topic: Demokratieprinzip
page_bfv: 540
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Birgit Bessin]] vom 16.4.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Was wir auch klar formulieren nach fast 80 Jahren Ende des Zweiten Weltkrieges und über 30 Jahren nach der Wiedervereinigung Deutschlands: Wir verlangen die Neuverhandlung der Souveränität Deutschlands. Wir verlangen den Abzug aller alliierten Truppen aus Deutschland, inklusive aller ihrer Waffen und Atomwaffen. Damit Deutschland endlich wieder eigene Souveränität hat. Denn gerade durch die fehlende Souveränität Deutschlands werden doch die Grundlinien unserer Außen- und Sicherheitspolitik durch die EU und durch die NATO entschieden. Und sie dienen äußerst selten unseren eigenen Interessen. Deswegen, liebe Freunde, lasst mich enden mit der Forderung, dass Deutschland seinen Kurs der Unterwerfung unter die Interessen raumfremder Mächte beenden muss und sich seiner nationalen Identität wieder bewusst werden muss!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 540

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