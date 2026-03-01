---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-09-07
topic: Demokratieprinzip
page_bfv: 553
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 7.9.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir Deutschen haben die braune Diktatur hinter uns gebracht und überlebt, wir haben die rote Diktatur überlebt. Wir werden auch die bunte Diktatur überleben. Wir werden sie besiegen! [...] Erst die Umerziehung - versteht mich nicht falsch, Frau Müller vom SPIEGEL ist auch hier. Frau Müller, die Umerziehung hatte vielleicht zu Beginn durchaus auch den Sinn, wirkliche Nazis auf den besseren Weg der Demokratie zu bringen. Das will ich gar nicht in Abrede stellt. Aber man hat das Kind mit dem Bade ausgeschüttet, muss ich so einordnen. Am Ende ging es darum, den Deutschen jeden Nationalstolz auszutreiben. [...] Deutschland ist heute im Status eines Landes, das ich als fremdbestimmt einordnen muss. Die Eliten haben nicht nur keine Liebe zu diesem Lande, man hat das Gefühl, sie sind korrumpiert und sie werden aus dem Ausland fremd- und ferngesteuert.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 553

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