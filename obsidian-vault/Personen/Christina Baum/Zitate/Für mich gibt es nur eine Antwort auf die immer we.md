---
type: zitat
speaker: "[[Christina Baum]]"
date: 2021-10-28
topic: Menschenwürde
page_bfv: 446
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 28.10.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Für mich gibt es nur eine Antwort auf die immer weiter fortschreitende von einzelnen Gesellschaftsgruppen bewusst herbeigeführte Zerstörung unserer kulturellen Identität: Wir brauchen dringend einen Kulturvorbehalt. Er besagt nichts Anderes, als dass unser kulturelles Erbe, das seit vielen Jahrhunderten von Generation zu Generation weitergegeben wurde und neben der Sprache die wichtigste verbindende Grundlage des Zusammenlebens der Deutschen darstellt, immer Vorrang vor allen anderen kulturellen, besonders aber auch religiösen Einflüssen haben muß. Ganz einfach gesagt: Das Kreuz, die Kirchenglocken oder die Weihnachtsmärkte bleiben - Moscheen, der Muezzin Ruf oder die Burka haben in Deutschland jedoch nichts zu suchen. Jeder Migrant, ,Flüchtling' oder Asylant, der zu uns kommt, weiß genau, dass wir ein christlich geprägtes Land sind. Wer also seine eigene Religion ausleben möchte, darf sich deshalb gerne ein Kultur- und religionsnahes Land für seine Entfaltung aussuchen. Die bewußte Entscheidung der vorwiegend muslimischen Migranten für Deutschland kann deshalb nur eines bedeuten: wir sollen unterwandert und unterworfen werden. Wer das nicht erkennt, hat anscheinend jede Wahrnehmung verloren. Für uns Deutsche, aber auch für alle anderen europäischen Völker, die in ähnlicher Weise islamisiert werden sollen, bleibt allein die Frage: wollen wir es einfach hinnehmen er wollen wir uns endlich dagegen auflehnen?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 446

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