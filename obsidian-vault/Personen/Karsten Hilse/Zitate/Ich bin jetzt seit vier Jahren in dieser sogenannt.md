---
type: zitat
speaker: "[[Karsten Hilse]]"
date: 2021-06-25
topic: Demokratieprinzip
page_bfv: 617
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Karsten Hilse]] vom 25.6.2021 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Ich bin jetzt seit vier Jahren in dieser sogenannten geschlossenen Anstalt. Und was ich dort erfahren habe ist natürlich, dass es hier sich nur noch um eine Scheindemokratie handelt. Also um eine Demokratie-Simulation. [...] Wenn wir uns anschauen: Am 18.11. - da hat das Parlament [...] das zweite Mal nach 1933 m seiner Geschichte seine Macht abgegeben an die Regierung. Und an eine Regierung, von der wir sehen können, [...] dass sie teilweise korrupt ist und dass sie sich vor allen Dingen nicht an Recht und Gesetz hält. Seit 2015 zum Beispiel gegen das Grundgesetz verstößt [...]. Denen ist quasi Rechtsstaatlichkeit relativ egal. Und am 18.11. habe ich zu Recht dieses Gesetz, dieses Infektionsschutz- gesetz, Ermächtigungsgesetz genannt, weil es noch nie so einschneidende Maßnahmen gab seit 1949 wie mit diesem Gesetz.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 617

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