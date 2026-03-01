---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-07-03
topic: Menschenwürde
page_bfv: 351
source: 'TikTok'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 3.7.2023 veröffentlicht auf: 'TikTok'
> [!quote] Aussage
>Multikulturell ist multikriminell. Seit Tagen brennen die französischen Vorstädte und jetzt greift es auch auf Brüssel über. Es sind Einwanderer und Einwandererkinder aus dem Nahen Osten und Nordafrika, die hier Rabatz machen, weil es Ärger mit der Polizei gibt. Das ist kein Vorwurf an sie selbst, es ist ein Vorwurf an die, die sie hergeholt haben. Sie sind hier fremd, sie kommen mit der Rechtsordnung nicht klar und dem geben sie Ausdruck. Jeder ist da am besten, wo er hingehört. Einwanderung funktioniert nicht. Niemand ersetzt fehlende Kinder eines Volkes. Dieses Volk stirbt aus. Wir wollen nicht aussterben, also brauchen wir keine Einwanderung, sondern Kinder. Denn Einwanderung ist multikulti und multikulturell ist multikriminell.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 351

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