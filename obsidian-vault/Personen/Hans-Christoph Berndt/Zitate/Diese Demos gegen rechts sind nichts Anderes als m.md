---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-01-29
topic: Demokratieprinzip
page_bfv: 593
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 29.1.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Diese Demos gegen rechts sind nichts Anderes als minutiös geplante Aufmärsche zur Einschüchterung und zur Demotivation aller, die sich den Kartellparteien heim Abbau unseres Landes und beim Rückbau der Demokratie entgegenstellen - Das schrieb mein Freund Rene Springer und er hat vollkommen recht. [...] Bestätigt sich es, was Tichy berichtet hat, dass der Verfassungsschutz nach Art der Stasi eine privates Treffen in einem Hotel mit Wanzen durchsetzt und mit Spitzeln durchsetzt hat, und dass er im Zusammenspiel mit den informellen Mitarbeitern von Correctiv damit den Anlass für eine Kampagne gegen die Opposition gegeben hat, dann ist nicht nur Erich Haldenwang fällig, dann muss Nancy Faeser weg und die ganze schändliche Ampel auch. [...] Liebe Freunde, die Vorbereitung und die Durchführung dieser Aufmärsche der Regierenden zeigen, dass Deutschland in diesem Jahr 2024 nicht einfach in eine Krise treibt, sondern zielgerichtet von den Regierenden getrieben wird. [...] In dieser Krise steckt auch eine Chance und steckt auch eine Ermutigung. Denn diese Krise gäbe es nicht ohne die rasant gewachsene Kraft der Antiregierungsproteste, der Bürgerbewegung und der Alternative für Deutschland. Die Postdemokraten haben einfach Angst. [...] Allein die Angst vor Machteinbußen verzerrt das Gesicht unserer jetzigen Bonzen und es verzerrt diese Gesichter bis zur Kenntlichkeit und siehe da, [....] die im Reichstag sitzen und sich hinter einem Graben verstecken wollen, sie sehen zum Verwechseln denen ähnlich, die in Wandlitz saßen und sich dort eingemauert haben. [...] Und diejenigen, diejenigen, die Martin Seltner nicht einreisen lassen wollen, sie sehen zum Verwechseln denjenigen ähnlich, die uns nicht ausreisen lassen wollten. Und liebe Freunde, die heute die AfD verbieten wollen, die heute die AfD verbieten wollen, die hätten 1989 beim neuen Deutschland mit unterschrieben, als es hieß: 'Der Minister des Inneren der DDR teilt mit, dass ein von zwei Personen unterzeichneter Antrag zur Bildung einer Vereinigung Neues Forum eingegangen, geprüft und abgelehnt wurde. Ziele und Anliegen der beantragten Vereinigung widersprechen der Verfassung und stellen eine staatsfeindliche Plattform dar.' Zitat Ende. Das ist die Sprache derjenigen, die heute die AfD verbieten wollen. Die Bonzen von damals und heute sehen sich zum Verwechseln ähnlich. Liebe Freunde, [...] 34 Jahre, 34 Jahre nach der Wende wird die BRD mehr und mehr zur Fortsetzung der DDR, zur Fortsetzung der DDR mit raffinierteren Mitteln, aber mit primitiverem Personal. Und liebe Freunde, das gilt in ganz besonderer Weise für die Christlich-Demokratische Union, die heute mehr denn je eine Blockpartei ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 593

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