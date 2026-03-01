---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-04-27
topic: Demokratieprinzip
page_bfv: 543
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 27.4.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Kriegsrhetorik auf allen regierungsnahen Medien ist unerträglich geworden. Der Krieg in der Ukraine ist schrecklich - aber es ist nicht unser Krieg! Und ich verwehre mich auch dagegen, daß er von den globalistischen Altparteienpolitikern vom Schlage eines Friedrich Merz oder einer Annalena Baerbock zu unserem gemacht wird. Sie tun das nur, weil sie die Statthalter des US-Establishments im Vasallenstaat BRD sind. Es besteht keine moralische Verpflichtung für den deutschen Steuerzahler, die Kosten für diesen aus amerikanischen Eigeninteressen provozierten Krieg zu übernehmen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 543

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