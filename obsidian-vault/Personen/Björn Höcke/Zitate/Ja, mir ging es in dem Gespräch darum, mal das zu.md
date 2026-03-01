---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-07-26
topic: Menschenwürde
page_bfv: 429
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 26.7.2024 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Ja, mir ging es in dem Gespräch darum, mal das zu tun, was das Establishment ja tagtäglich tut, nämlich Begriffe zu entkontextualisieren und mal umzudrehen. Also die Remigration mal ganz bewusst in den Kontext reinzustellen: Passt mal auf, Leute, denkt mal nach. Wir haben in den letzten 30 Jahren 1,5 Millionen Auswanderer aus Deutschland gehabt und die sind überwiegend nachweislich Hochqualifizierte gewesen. [...] Es geht natürlich auch darum, das eigene schlechte Bild, das die Medien von mir gemacht haben, zu korrigieren. [...] Natürlich ist es Taktik. Das muss ich frank und frei gestehen. Als Politiker, muss ich das eingestehen. Das ist natürlich Taktik. Das heißt, nein, ich bin so. Ich bin ein Mensch, der Gefühle hat und ich bin eigentlich ein sehr warmherziger Mensch. Und da will man einfach anschlussfähig sein. Man will auch dem Westdeutschen, mit Verlaub, der in die tagesschau guckt, und der noch nicht so aufgewacht ist wie wir im Osten, will man zeigen, das ist ein ganz normaler Mensch, der sorgt sich um sein Land und der versucht, sich Gedanken zu machen, wie es in Zukunft weitergeht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 429. Interview mit Paul Brandenburg

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