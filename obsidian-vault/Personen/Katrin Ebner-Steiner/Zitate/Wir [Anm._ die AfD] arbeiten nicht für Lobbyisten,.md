---
type: zitat
speaker: "[[Katrin Ebner-Steiner]]"
date: 2023-02-22
topic: Menschenwürde
page_bfv: 514
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Katrin Ebner-Steiner]] vom 22.2.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir [Anm.: die AfD] arbeiten nicht für Lobbyisten, Globalisten und Finanzeliten. Denn diese Leute verfolgen mit dem Allparteienkartell den Great Reset. [...] Jetzt kommt mit mir auf eine Zeitreise. Ich nehme euch mit in eine Zukunft des Jahres 2040, nach dem Rot, Schwarz, Grün und Gelb noch weitere 17 Jahre regiert haben. Doch da müsst ihr jetzt durch. Die Bundesrepublik Deutschland wurde umbenannt in 'Bunte Republik - nie wieder Deutschland' und der Bundestag in 'Bunter Tag'. Das ist sowieso egal, denn die Regierungsgeschäfte werden jetzt direkt aus Brüssel und Washington erledigt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 514

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

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