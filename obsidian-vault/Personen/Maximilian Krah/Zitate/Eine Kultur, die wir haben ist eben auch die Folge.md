---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2023-10-12
topic: Menschenwürde
page_bfv: 170
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 12.10.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Eine Kultur, die wir haben ist eben auch die Folge dessen, was wir über die Geschichte geworden sind und wir sind es auch geworden, weil wir an einem bestimmten Ort leben. [...] Das heißt nicht, dass jeder Syrer es nicht kann, das heißt aber, dass er schwerer hat. Warum? Weil er als Produkt seiner Geschichte, seiner Eltern, seiner Prägung natürlich nicht auf das vorbereitet ist was wir sind, denn wir sind perfekt angepasst eben an ein Leben in diesen geographischen Breiten an diesem Ort, den wir Heimat nennen. Wir sollten also begreifen, dass wenn wir übers Volk reden, reden wir [...] tatsächlich über eine Gemeinschaft der Ähnlichen und diese Ähnlichkeit ist entstanden über sehr, sehr viele Jahrhunderte, durch eine perfekte Adaption von Menschen an den Ort wo sie leben und aneinander. [...] Das wollen wir erstmal erhalten. Wir wollen es nicht deshalb erhalten, weil wir die anderen geringschätzen, sondern weil wir uns selbst schätzen und wir schätzen uns selbst, weil wir unsere Vorfahren ehren und weil wir das eigentlich ganz gut finden, wie wir hier sind, mit allen Einschränkungen, die wir haben. Und insofern ist der Begriff des Volkes natürlich eine extreme Herausforderung für Leute, die nur als Individuum denken, die überhaupt nicht begreifen was eine Gemeinschaft ist, die meinen, man könne beliebig Menschen von Ort A nach Ort B umsetzen und alles sei gut und die glauben, das Zusammenleben in unserem Land hänge allein am Gesetz und eben nicht an diesen tiefsitzenden kulturellen Übereinstimmungen, die dazu führen, dass wir uns instinktiv erkennen, in der Regel instinktiv mögen [...]. Das ist der Kernbegriff des Volkes, nämlich eine Beheimatung in einer Gemeinschaft. […] Sie werden also reinkommen und bleiben Afrikaner, Mittel-Araber und so weiter. Das sind sicherlich in Afrika und Arabien wunderbare Völker, aber sie bringen das genau mit und sie werden sich mit Ihresgleichen sammeln. Sie werden dann am Ende einen Stadtteil übernehmen und der wird innerhalb von wenigen Jahren aussehen, wie es eben in Afrika und Arabien aussieht. [...] Und insofern: Wenn wir vom Volk reden – das ist weit mehr als irgendeine politische oder rechtliche Kategorie. Es ist eine natürliche biologisch nachprüfbare Realität. Wenn ihr einen Bluttest einschickt, kann man euch mit hoher Wahrscheinlichkeit nachsagen, wo eure Vorfahren herkommen. Es ist also kein soziales Konstrukt, es ist etwas, was in den Genen ist. Und jetzt ist es so, dass wir das – weil wir diese Gemeinschaft bilden – ein gewisses Vertrauen haben; heißt: wir sind imstande zu überlegen, was gut für euch ist, ist gut für uns alle. [...] Ein Araber wird eine andere Vorstellung von dem haben, was ein Wohl ist als wir. [...] Zwischen uns und den Tschechen – ja vielleicht ist die Zeit, wo man mit dem Bier trinken anfängt in der Arbeitswoche in Tschechien eine Stunde nach vorn gerückt im Vergleich zu Sachsen, aber ich glaube das sind Petitessen. Aber eben mit der arabischen Welt und mit Afrika ist was Anderes. Das heißt also eine Zuwanderung, die uns sehr nahe ist oder auch eine Überschneidung, die uns sehr nahe ist, wird in der Regel nicht so problematisch sein und wird sich auch nach ein, zwei Generationen überwinden lassen, wenn es sein muss. [...] Das, was für uns individuell gilt, gilt für uns als Gruppe. Wir sind ein Volk der Ähnlichen und das ist über die Jahrhunderte gewachsen. [...] Aber wenn Leute sich hinstellen, die meinen sie könnten am Reißbrett neue Völker schaffen. 200.000 – nee 400.000 pro Jahr und dann am besten noch Englisch als zweite Amtssprache, weil dann kriegen wir auch mehr und leichter. Das ist O-Ton eines Mitglieds des Sachverständigen-Rates der Bundesregierung für die gesamtwirtschaftliche Lage. Wer so anfängt in Tausender-Blöcken Menschen zu verschieben, weil er irgendwelche ökonomischen Bedingungen erfüllen will, nein. Das ist Wahnsinn und das werde ich in Zukunft auch wieder ganz offen Umvolkung nennen, egal was man mir dafür nachsagt. Das ist nicht akzeptabel.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 170

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