---
type: zitat
speaker: "[[Marc Jongen]]"
date: 2022-07-13
topic: Demokratieprinzip
page_bfv: 639
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Marc Jongen]] vom 13.7.2022 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Seit vielen Jahren arbeiten die deutschen Regierungen, die per Amtseid das Wohl des deutschen Volkes mehren sollen, systematisch gegen das eigene Land und das eigene Volk. Und die Ampel hat das noch intensiviert, und zum Teil wissen diese Leute ja gar nicht mehr, dass ein deutsches Volk überhaupt existiert. Oder sie schämen sich dafür. [...] Wir wollen ein souveränes, ein selbstbewusstes, ein blühendes Deutschland, das seine Interessen vertritt und das seiner Bürger in Frieden mit der Welt, aber eben nicht zu untertänigen Diensten der ganzen Welt. Und es liegt allein an uns, und das müssen wir uns immer wieder bewusst machen, allein an der Alternative für Deutschland, diese bessere Zukunft herbeizuführen und das Ruder noch herumzureißen. Und deshalb, liebe Freunde, dürfen wir uns doch nicht selbst streiten, uns selbst zerfleischen und lähmen. Damit betreiben wir das Geschäft unserer Gegner, denn die wollen uns vernichten, die deutschen demokratischen Parteien, wie sie sich nennen und indem sie Grundgesetz und Demokratie mit Füßen treten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 639

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