---
type: zitat
speaker: "[[Oliver Kirchner]]"
date: 2025-02-07
topic: Menschenwürde
page_bfv: 914
source: 'Redebeitrag'
status: Unbewertet
---

# Zitat: [[Oliver Kirchner]] vom 7.2.2025 veröffentlicht auf: 'Redebeitrag'
> [!quote] Aussage
>Wir haben hier noch eigene Straftäter, dann müssen wir nicht noch Straftäter praktisch hiernach Deutschland importieren und wenn ich hier sehe, dass Menschen Frauen und Kinder vor Züge stoßen, die Kinder sterben, die Mütter überleben und die ohne ihre Kinder weiterleben müssen, sowas gab es vor 2015 in Deutschland nicht. Habe ich noch nie gehört, dass es sowas gab. 36.000 Messerangriffe in drei Jahren. 36.000 Messerangriffe in drei Jahren. Das ist der Messer-Dschihad, den die ISIS angekündigt haben, der islamische Staat angekündigt hat und genau das passiert hier auf unseren Straßen. Die messern sich an unserer Aufnahmegesellschaft ab und wir bezahlen den ganzen Spaß. [...] Wie gesagt, Schlauchboot-Fachkräfte und Balkanrouten-Wissenschaftler, da habe ich die Nase voll von. Von Messer-Fachmännern natürlich auch.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 914

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