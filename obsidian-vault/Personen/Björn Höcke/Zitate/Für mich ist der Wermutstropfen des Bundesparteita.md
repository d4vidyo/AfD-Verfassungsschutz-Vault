---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-13
topic: Sonstiges
page_bfv: 869
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 13.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Für mich ist der Wermutstropfen des Bundesparteitages die Entscheidung zur JA. Dabei will ich betonen, daß auch ich die stärkere Integration der JA in die Mutterpartei befürwortet habe. Aber das jetzt beschlossene Vorgehen verläuft nicht in Richtung "Juso-Modell". Ich will es kurz machen: Sowohl der Antrag des Bundesvorstandes als auch jener der JA waren noch etwas unausgegoren. Ersterer atmete zu viel Funktionärsgeist. Hier schien es so, als wollte man die jungen Leute zu sehr an die Kandare nehmen, auch um den Preis, die Innovationsfähigkeit der Jugend über Gebühr zu beschneiden. Und beim JA-Antrag hatte man das Gefühl, daß den jungen Fohlen nicht bewußt genug ist, daß auch die weitläufigste Weide nicht ohne Zaun auskommt. Daß zwei gegensätzliche Anträge auf der Tagesordnung zu finden waren, weist daraufhin, daß der Prozeß der Konsensfindung noch Zeit gebraucht hätte. Vielleicht war er nicht lang genug, vielleicht war er nicht breit genug angelegt, vielleicht hatte er nur die falsche Sukzession? Ich weiß es nicht, aber ich bin sicher, daß mit etwas mehr Ruhe ein Konsens hätte erzielt werden können, der in einen gemeinsamen Antrag beim nächsten Parteitag gemündet wäre und keine Verlierer produziert hätte. [...] Nun gilt es in der Lage zu leben, die die Entscheidung nach sich zieht. Die Defizite des beschlossenen Antrages werden zu Nachjustierungen führen müssen, so meine Vermutung. In Thüringen wird sich am guten Verhältnis zu unserer Jugend nichts ändern, das versichere ich. Hier geht es nicht um Formalien, sondern um den Geist, den wir leben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 869

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