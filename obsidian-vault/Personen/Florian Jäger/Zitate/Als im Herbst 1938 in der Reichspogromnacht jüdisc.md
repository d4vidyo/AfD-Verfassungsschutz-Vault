---
type: zitat
speaker: "[[Florian Jäger]]"
date: 2021-12-06
topic: Menschenwürde
page_bfv: 524
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Florian Jäger]] vom 6.12.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Als im Herbst 1938 in der Reichspogromnacht jüdische Geschäfte geplündert, Synagogen in Brand gesteckt und Juden misshandelt und ermordet wurden, sprach die nationalsozialistische Propaganda davon, dass sich in dieser Nacht ja der Volkszorn, der berechtigte Volkszorn gegen die Juden, spontan entzündet hätte. Es war relativ klar, dass dieser so genannte Volkszorn weitaus weniger spontan war, als die nationalsozialistische Propaganda verkündet hat. Und es war sehr schnell in der Geschichte, dann vom organisierten Volkszorn die Rede. [...] Wer sich ein wenig in der Geschichte auskennt, der er erinnert sich an Joseph Goebbels, der, der einst mitgeteilt hat: 'Unsere Geduld mit den Juden geht zu Ende. Wir werden ihn bald das freche Lügenmaul stopfen.' Reden wir über Markus Söder- Markus Söder wird nicht müde, von einer Pandemie der Ungeimpften zu reden. [...] Natürlich wissen wir, dass der Ungeimpfte an der Pandemie genauso wenig schuld war wie früher die Juden daran schuld waren, dass das Reich in einer wirtschaftlich desolaten Verfassung war. Aber die Politik ist damals wie heute am Ende. [...] Es gibt für diese Politiker kein Zurück mehr. Also muss ein Schuldiger gefunden werden. Und dieser Schuldige ist für Markus Söder natürlich nicht Markus Söder. Es muss der Ungeimpfte sein. Und das ist genau die Methode, mit der ein so genannter Volkszorn erzeugt wird. [...] All diese Dinge, dann ist der Schritt von der klassischen Diskriminierung bis zu tatsächlich gewalttätigen Ausbrüchen nicht mehr groß.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 524

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