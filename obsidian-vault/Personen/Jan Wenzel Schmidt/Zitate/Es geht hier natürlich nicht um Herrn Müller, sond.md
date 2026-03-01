---
type: zitat
speaker: "[[Jan Wenzel Schmidt]]"
date: 2024-01-19
topic: Sonstiges
page_bfv: 784
source: 'Heimatkurier'
status: Unbewertet
---

# Zitat: [[Jan Wenzel Schmidt]] vom 19.1.2024 veröffentlicht auf: 'Heimatkurier'
> [!quote] Aussage
>Es geht hier natürlich nicht um Herrn Müller, sondern um die Partei, die man am Nasenring durch die Manege führen möchte. Ich nehme den Etablierten ihre moralische Entrüstung darüber, dass ich einen ehemaligen und wegen Notwehr gegen linksextreme Angriffe verurteilten IB-Aktivisten im Bundestag beschäftigt, schlichtweg nicht ab. [...] Man will hier das Vorfeld von der Partei isolieren, um es zu zerschlagen. Dieses Spiel sollten wir nicht mitspielen. Wer sich distanziert und linken Hetzkampagnen nachgibt, wird nicht in Ruhe gelassen, sondern immer wieder Ziel solcher Hetzkampagnen, weil die Strategie der Spaltung aufgeht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 784

**Verfassungsschutz Kategorisierung:** Sonstiges.

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