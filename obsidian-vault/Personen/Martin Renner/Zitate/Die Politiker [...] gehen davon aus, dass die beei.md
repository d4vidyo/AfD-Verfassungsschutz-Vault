---
type: zitat
speaker: "[[Martin Renner]]"
date: 2023-03-23
topic: Demokratieprinzip
page_bfv: 600
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 23.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Politiker [...] gehen davon aus, dass die beeinflussenden Medien genau die Botschaften ausstrahlen, die die Unterstützung der jetzigen Altparteien auf Dauer realisieren. [...] Die Altparteien, das sag ich gar nicht mehr, sondern ich sag': die einzelnen Parteien der neuen Einheitspartei NED. Klingt ähnlich wie SED. Das ist auch gewollt. Ja, das ist eine Einheitspartei und da tut man sich natürlich als einzige Oppositionskraft schon relativ schwer, überhaupt zu Gehör zu kommen. Aber die Politiker glauben, sie brauchen sich nicht mehr rückzuversichern, weil eben die Medien ihnen diese Arbeit abnehmen und die Medien sich einfach von der Rolle der Kontrolleure der politischen Macht, denn, das sind sie, die Kontrolleure der politischen Macht nach der Definition auch in unserem Grundgesetz, haben sich entwickelt zu Herolden der politisch Mächtigen. [...] Welche Staatsform wollen wir bewahren? Autoritativ? Totalitär? Ich habe den Eindruck, dass wir ins Totalitäre abgleiten in unserem Land. [...] Und jetzt sage ich zum Abschluss noch mal ein richtig derbes endgültiges Wort. Wir haben eine Entwicklung hin, unsere Drei-Gewaltenteilung - Exekutive, Legislative, Judikative - die untereinander von sich getrennt und unabhängig sein sollen und müssen. Sollen und müssen. Haben wir aber im Bereich der Exekutive, Legislative, Judikative die Entwicklung hin zu einer von der Drei-Gewaltenteilung zu einer Drei-Gewalten-Einheits-Tyrannis. Wenn ein Verfassungsrichter aus dem Kreis der Legislative gewählt wird, um dem Verfassungsgericht vorzustehen, der aber gleichzeitig auch der Buddy von der Frau Merkel war, also der Exekutive, dann kann man nicht mehr von einem Drei-Gewaltenteilung sprechen. Das ist eine Drei-Gewalten-Einheits-Tyrannis. Und wenn da die Medien sich noch damit hinsetzen, da haben wir nicht mehr eine Drei-Gewalten-Einheits-Tyrannis, sondern eine Vier-Gewalten-Einheits-Tyrannis. Und genau das ist der Zustand unserer heutigen politischen Bundesrepublik. Und das müssen wir ändern, wenn wir eine Zukunft haben wollen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 600

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