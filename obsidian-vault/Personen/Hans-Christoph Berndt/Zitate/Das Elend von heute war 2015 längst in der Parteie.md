---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-04-06
topic: Demokratieprinzip
page_bfv: 640
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 6.4.2024 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Das Elend von heute war 2015 längst in der Parteienherrschaft angelegt. Das Elend von heute ist ja das Ergebnis der jahrzehntelangen Herrschaft der Staatsparteien SPD, CDU, FDP, Linke und Grüne, Parteien, die das Volk verneinen und die nicht Deutschland verpflichtet sind, sondern gewissenlosen Weltverbesserern in Davos. Liebe Freunde, deshalb hat unser Freund Lars Hünich mit seiner Kritik am Parteienstaat vollkommen recht. [...] Zum Ende der Wahlperiode ist Woidke länger Minister oder Ministerpräsident, als Erich Honecker Generalsekretär der SED war. Und das merkt man, liebe Freunde. Woidke ist der personifizierte Parteienstaat, den wir überwinden müssen, um endlich wieder frei atmen zu können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 640

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