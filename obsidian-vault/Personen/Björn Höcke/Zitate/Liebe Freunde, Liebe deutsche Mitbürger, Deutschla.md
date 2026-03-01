---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-03-29
topic: Menschenwürde
page_bfv: 504
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 29.3.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Liebe Freunde, Liebe deutsche Mitbürger, Deutschland ist ein besetztes und unterwandertes Land. Das ist das Erste, was er [Anm.: Otto von Bismarck] diagnostizieren würde. Ein besetztes und unterwandertes und fremdbestimmtes Land. [...] Die Freunde – in Anführungszeichen – die uns regieren, die sind in eine Schule gegangen, wo sie mit anderen Ideen konfrontiert worden sind, als dem eigenen Land zu dienen. Nein, diese Menschen, die uns regieren, liebe Freunde, das sind keine deutschen Patrioten. Das sind globalistische Sprechpuppen. Die machen deswegen auch keine deutsche Interessenpolitik, sondern sie machen eine Interessenpolitik für amerikanische Großkonzerne und für globalistische Strippenzieher.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 504

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