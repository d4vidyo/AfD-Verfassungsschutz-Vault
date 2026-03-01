---
type: zitat
speaker: "[[Sven Tritschler]]"
date: 2025-01-11
topic: Menschenwürde
page_bfv: 938
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Sven Tritschler]] vom 11.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Ich rede aus dem Grund, weil ich Kölner Abgeordneter bin. Und jeden Morgen, wenn ich zur Arbeit fahre, fahre ich an der Großmoschee in Ehrenfeld vorbei. Das ist Ihnen vielleicht ein Begriff. Und für mich ist das eine Machtdemonstration. Und den Bürgern wurde damals versprochen: 'Ja ihr kriegt jetzt diese Moschee, aber es wird nie der Muezzin von da rufen. Und vor zwei Jahren hat Frau Reker, die ist Ihnen vielleicht bekannt. Das ist die Dame mit der 'Armlänge Abstand', ein - hat dann den Muezzinruf gestattet. Und sowas erleben wir immer mehr, in immer mehr Städten. Ich weiß, dass das nicht in allen Bereichen in Deutschland im Moment so akut ist. Aber für uns in Nordrhein-Westfalen mit dem Ballungszentrum, mit dem Ruhrgebiet, ist es ein Problem. Und wir möchten diese muslimischen Machtdemonstrationen nicht in unseren Städten haben. Das gehört nicht in unser Land. Das heißt nicht, dass irgendjemand seine Religion nicht frei ausüben kann. Aber wir wollen keine Landnahme, keine Machtdemonstration mitten in unseren Städten. Wir sehen, wo das hinführt. Das führt zu Parallelgesellschaften, das führt zur Spaltung unserer Gesellschaft. Das lehnen wir ab. Unsere Leitkultur muss vorherrschen. Und die heißt nun mal: Kein Muezzinruf und keine Großmoscheen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 938

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