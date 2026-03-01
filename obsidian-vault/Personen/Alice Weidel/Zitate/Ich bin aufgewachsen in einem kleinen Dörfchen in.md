---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2023-10-31
topic: Menschenwürde
page_bfv: 452
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 31.10.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Ich bin aufgewachsen in einem kleinen Dörfchen in Ostwestfalen, also Harsewinkel Und dort habe ich die Erfahrung gemacht, mit einem Dörfchen, was durch fremde Kulturen, vorrangig der muslimischen, völlig überfordert gewesen ist. Ich hab' das selbst als kleines Mädchen mitbekommen, auch in der Schule, dann auch im Freibad. Ich habe als Mädchen und als Jugendliche eigentlich die ganzen Themen schon mitbekommen, wenn man von jungen Horden dort angemacht wird, umringt wird im Wasser. Und da wusste ich eigentlich schon gleich, dass das alles kulturell nicht so zusammenpasst. Also dass wir uns mit dem Influx von kulturfremden Leuten uns ein massives gesellschaftspolitisches Problem schaffen, was entgegen unserer freiheitlichen demokratischen Grundordnung ist. Das war mir ehrlich gesagt schon recht früh klar - und das eigentlich schon in der Grundschule. Es passt nicht zusammen. Also ich habe als kleines Mädchen darunter gelitten [...] und andere auch. [...] Uns wurde verboten im Dunkeln mit Dem Fahrrad nach Hause zu fahren. Durch den Stadtpark zu fahren [...], weil es permanent solche Zwischenfälle im Dunkeln, oder auf Heimwegen mit diesen Leuten gegeben hat, wenn man Schützenfeste hatte, wenn wir mal in eine Kneipe gegangen sind so als Teenager. Da wurd‘s ein bisschen später und da mussten wjr immer bestimmte Wege, die dunkel waren, meiden, weil es permanent in irgendeiner Art und Weise Probleme mit diesen Personenkreisen gegeben hat, die zu Millionen ab 2015 in unser Land gelassen wurden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 452

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