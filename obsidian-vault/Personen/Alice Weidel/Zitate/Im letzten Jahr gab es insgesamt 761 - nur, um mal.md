---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2024-09-12
topic: Menschenwürde
page_bfv: 453
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 12.9.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Im letzten Jahr gab es insgesamt 761 - nur, um mal Zahlen zu nennen - 761 Gruppenvergewaltigungen in unserem Land. Das sind mehr als zwei von diesem abscheulichen Verbrechen am Tag. Das sind Phänomene, das Herumgemessere, die Vergewaltigungen, die völlig neu sind in unserem Land. Und ich möchte es Ihnen hier ganz deutlich sagen, weil ihr hier die Klardenker seid und das ohnehin schon wisst: Das, was wir auf den deutschen Straßen erleben, ist der Dschihad. Hier wird ein Glaubenskrieg gegen die deutsche Bevölkerung bereits geführt. Und das ist auch der Grund, warum, sobald wir in der Regierung sitzen wir diese Leute alle achtkantig rausschmeißen, die diese Verbrechen auf unseren Straßen begehen. [...] Seit Jahren stelle ich mir die Frage: Wie kann man sowas machen? Wie kann man diese Menschen reinlassen? [...][Wisst ihr] was bei uns an den Schulen los ist? Was diese - was die Kinder von diesen Leuten, die aber ganz früh Christen- und Einheimischen-Hass eingeimpft bekommen, mit unseren deutschen Kindern auf den Schulhöfen machen? Die werden verprügelt, immer - hier - ins Gesicht, weil sie Nicht-Muslime sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 453

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