---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-09-09
topic: Menschenwürde
page_bfv: 429
source: 'Instgram'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 9.9.2024 veröffentlicht auf: 'Instgram'
> [!quote] Aussage
>Du kannst nicht lesen, schreiben und rechnen? Gut möglich. Die Hälfte der Brandenburger Schüler kann das nicht. Wenn du es kannst, Glückwunsch! Wenn du es nicht kannst, sieht es schlecht aus. Denn wer nicht lesen, rechnen und schreiben kann, der kann auch keinen guten Beruf ergreifen. Und dann muss er mit Mama Merkels Analphabeten um schlecht bezahlte Jobs konkurrieren. Und da hilft es dir auch nicht, wenn du in eine Schule ohne Rassismus über mit viel sexueller Vielfalt gehst. Schluss damit! In der Schule muss wieder gelernt werden. Und damit du auf dem Schulhof nicht ständig von Ali und Hassan belästigt wirst, braucht es vor allem eins: Remigration. Denn du hast eine gute Zukunft in deiner Heimat verdient!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 429

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