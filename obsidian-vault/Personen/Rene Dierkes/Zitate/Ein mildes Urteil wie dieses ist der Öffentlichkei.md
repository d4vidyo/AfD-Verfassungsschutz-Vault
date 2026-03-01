---
type: zitat
speaker: "[[Rene Dierkes]]"
date: 2024-10-07
topic: Menschenwürde
page_bfv: 457
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Rene Dierkes]] vom 7.10.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Ein mildes Urteil wie dieses ist der Öffentlichkeit kaum noch zu vermitteln. Weil der Richter nicht ausschließen konnte, dass der afghanische Verbrecher in seiner geistigen Entwicklung einem Jugendlichen gleichstand, hat er das sehr viel mildere Jugendstrafrecht angewendet. Auch beim Strafmaß wurden die Möglichkeiten nicht ausgeschöpft. Wann werden Richter endlich begreifen, dass sie bei eiskalten Tätern, die keinerlei Reue zeigen, auf maximale Abschreckung setzen müssen? Zumal Kriminelle aus muslimischen Ländern ohnehin nicht ,resozialisiert' werden können, da sie nie eine Sozialisierung im westlichen Sinne erlebt haben und Entgegenkommen immer als Schwäche auslegen. Für diesen Tätertyp ist in erster Linie die Abschiebungsoffensive unseres #Remgrationsprogramms gedacht. Solche Kriminellen gehören hart abgeurteilt und nach Verbüßung ihrer Strafe konsequent abgeschoben. Als einzige Fraktion im Bayerischen Landtag zieht die #AfD die notwendigen Schlüsse aus der überbordenden Gewaltkriminalität bestimmter Migrantengruppen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 457

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