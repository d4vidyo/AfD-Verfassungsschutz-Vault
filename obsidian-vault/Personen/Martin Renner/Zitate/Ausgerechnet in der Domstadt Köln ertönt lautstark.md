---
type: zitat
speaker: "[[Martin Renner]]"
date: 2022-10-15
topic: Menschenwürde
page_bfv: 470
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 15.10.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ausgerechnet in der Domstadt Köln ertönt lautstark seit Freitag einmal wöchentlich der ,Ruf des Muezzin' aus der Ehrenfelder DITIB-Zentralmoschee. Muslime sollen das Gefühl bekommen, ,dass auch sie ihre Religionspraxis ausüben können', so ein Vertreter der DITIB. Das ist doch wohl nur der erste Schritt? Und ist der zweite Schritt in der Ausübung der Religionspraxis – auch als Scharia zu bezeichnen – dann die handgreifliche Züchtigung bis hin zur Steinigung von Frauen? Und ist der dritte - finale - Schritt dann der ,Adhan-Gebetsaufruf' vom Muezzin aus den Höhen der zukünftig umgewidmeten und islamkonform umbenannten ,Hohen Domkirche Sankt Petrus zu Köln'? [...] Der Ruf ,Allah ist größer' ist nichts weniger als eine Machtdemonstration des Islam. Ein Postulat der bedingungslosen Inbesitznahme eines Landes, das eigentlich den sofortigen und unmissverständlichen Einsatz des Verfassungsschutzes auf den Plan rufen müsste. Sei es drum! Fast überflüssig zu erwähnen, dass diese bewusste Abkehr von unserer christlichen und abendländischen Zivilisation – die eigene freiwillige Unterwerfung und genau das fordert und meint der Begriff ,Islam' – auch noch feierlich live im TV übertragen wurde. Buntheit, Toleranz, Akzeptanz, Vielfalt sind – falsch verstanden – die Komponenten des Bösen. [...] Dies alles ist der links-dystopische Irrsinn unserer Zeit. Geboren aus einem über die Jahrzehnte zelebrierten Erb-Schuld-Denken, das nach dem Willen linksextremer Weltverbesserer niemals enden darf.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 470

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