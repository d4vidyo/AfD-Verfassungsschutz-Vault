---
type: zitat
speaker: "[[Christina Baum]]"
date: 2023-03-20
topic: Menschenwürde
page_bfv: 473
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 20.3.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Deutschland muss deutsch bleiben Nach der massenhaften Einwanderung von arabischen Männern sprießen Moscheen mit Minaretten aus dem Boden und sogar der Muezzin-Ruf ertönt mittlerweile in einigen Städten. Deshalb ist es nur folgerichtig, auch gleich die Straßen mit arabischen Namen zu versehen, damit sich die vielen Neubürger in unserem Land auch wie Zuhause fühlen. Nein, lieber Herr Charchira von den Grünen, das nennt man nicht Inklusion, sondern das ist arabisch-muslimische Landnahme! Wir, die Deutschen, werden zur Minderheit im eigenen Land und dies in einer Geschwindigkeit, das einem schwindlig wird. Vom deutschen Schuldkult psychisch/ seelisch geschwächt und jahrzehntelang umerzogen, wird weiter darauf hin gearbeitet, unser Volk, unsere Kultur, unsere Sprache und unsere Traditionen langsam verschwinden zu lassen. Doch wir werden uns mit Händen und Füßen dagegen wehren. Die AfD ist die einzige Partei, die sich dieser Abschaffung der Deutschen auf ihrem eigenen Staatsgebiet mit allen ihr zur Verfügung stehenden Mitteln entgegen stemmt. Deutschland soll nicht zu Arabien werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 473

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