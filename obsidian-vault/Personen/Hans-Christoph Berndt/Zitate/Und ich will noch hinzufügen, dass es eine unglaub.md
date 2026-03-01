---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-08-21
topic: Menschenwürde
page_bfv: 122
source: 'Interview mit AUF1'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 21.8.2024 veröffentlicht auf: 'Interview mit AUF1'
> [!quote] Aussage
>Und ich will noch hinzufügen, dass es eine unglaubliche Wegmarke wäre, wenn es uns gelingen würde, in einem, zwei oder drei Ländern im Osten unter all dem Druck, unter dem wir, seitdem wir existieren, stehen, unter diesen ganzen Kampagnen dieses Jahres, unter all der Repressionen, stärkste Kraft zu werden. Das wäre ein moralischer Sieg und der würde uns allen für die nächsten Jahre unglaublich viel Auftrieb geben. Und ich bin fest überzeugt, solange wir noch 20, 30, 40 Millionen Deutsche im Land sind, haben wir die Kraft und haben wir die Möglichkeiten, die Dinge zum Besseren zu wenden. Und wenn es dann mit einer Regierung 2024 nicht klappt, dann kommt es 2025 oder 2026. Am Ende ist auch nicht die Regierung das Entscheidende, sondern dass sich die Politik ändert. Wir wollen ja nicht einfach an den Trog wie die anderen. Wir wollen, dass es anders zugeht in Deutschland. Wir wollen, dass das Eigene wieder respektiert wird, dass in Deutschland wieder Politik für die Deutschen gemacht wird und nicht, wie es die Altparteien machen, die die Deutschen für das Letzte halten. Wir sind für die nur noch dazu da, Steuern zu zahlen, damit die immer noch mehr Flüchtlinge ins Land holen können. Wir wollen, dass sich diese Anomalie ändert und das werden wir auch erreichen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 122

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