import json
from tkinter import filedialog
from pathlib import Path
import re
import os


# Bundesland-Kürzel ausschreiben und dabei die '&shy;' Artefakte entfernen.
def resolveState(state):
    long_state = d["meta"]["dictionary"]["state_long"].get(state)
    return long_state.replace("&shy;", "")

# String von Sonderzeichen die nicht in Dateinamen erlaubt sind bereinigen.
def cleanWindowsFilename(filename):    
    invalid_chars = r'[#<>:"/\\|?*\x00-\x1F]'
    clean_name = re.sub(invalid_chars, '_', filename)
    return clean_name 

# Datum Format vereinheitlichen
def cleanDate(date_str):
    if not date_str:
        return "Nicht Verfügbar", 2

    date_str = str(date_str).strip()

    if "." in date_str:
        teile = date_str.split(".")
        if len(teile) == 3:
            tag = teile[0].zfill(2)
            monat = teile[1].zfill(2)
            jahr = teile[2]
            return f"{jahr}-{monat}-{tag}", 0

    monate = {
        "Januar": "01", "Februar": "02", "März": "03", "April": "04",
        "Mai": "05", "Juni": "06", "Juli": "07", "August": "08",
        "September": "09", "Oktober": "10", "November": "11", "Dezember": "12"
    }
    
    for monat_name, monat_zahl in monate.items():
        if monat_name in date_str:
            teile = date_str.split()
            if len(teile) >= 2:
                jahr = teile[-1]
                return f"{jahr}-{monat_zahl}-01", 1

    return date_str, 3

# Filename mit Zähler versehen falls gleichnamige Datei existiert
def getUniqueFilename(filepath):
    base, ext = os.path.splitext(filepath)
    counter = 1
    new_filepath = filepath
    
    while os.path.exists(new_filepath):
        counter += 1
        new_filepath = f"{base}_{(counter)}{ext}"
        
    return new_filepath, counter


file_path = filedialog.askopenfilename(title="Quelldatei vom Spiegel auswählen")
if not file_path:
    exit()
    
folder_path = filedialog.askdirectory(title="Zielordner der extraktion auswählen")
if not folder_path:
    exit()

with open(file_path, encoding="utf-8") as f:
    d = json.load(f)["json_output"]
    
    
# Personen-Dateien erstellen
with open("Person_template.md", encoding="utf-8") as f:
    TEMPLATE_person = f.read()
    
with open("Person_ranking.json", encoding="utf-8") as f:
    person_ranking = json.load(f)
    
ranking_lookup = { ranking["name"]: ranking["relevance"] for ranking in person_ranking }    
    
for speaker in d["speakers"]:
    speaker_path=f"{folder_path}/Personen/{speaker['name']}"
    Path(f"{speaker_path}/Zitate").mkdir(parents=True, exist_ok=True)
    
    person_content = TEMPLATE_person.replace(">>description<<", speaker["description"])
    person_content = person_content.replace(">>id<<", speaker["id"])
    person_content = person_content.replace(">>name<<", speaker["name"])
    person_content = person_content.replace(">>state<<", resolveState(speaker["state"]))
    person_content = person_content.replace(">>relevance<<", str(ranking_lookup[speaker["name"]]))
    
    if speaker["gender"] == "m":
        person_content = person_content.replace(">>gender<<", "male")
    elif speaker["gender"] == "f":
        person_content = person_content.replace(">>gender<<", "female")
    
    if speaker["is_still_member"] == "y":
        person_content = person_content.replace(">>is_still_member<<", "true")
        person_content = person_content.replace(">>noch_mitglied<<", "Ja")
    else:
        person_content = person_content.replace(">>is_still_member<<", "false")
        person_content = person_content.replace(">>noch_mitglied<<", "Nein")
            
    with open(f"{speaker_path}/{speaker['name']}.md", "w", encoding="utf-8") as f:
        f.write(person_content)


# Zitat-Dateien erstellen
with open("Quote_template.md", encoding="utf-8") as f:
    TEMPLATE_quote = f.read()

speaker_lookup = { speaker['id']: speaker['name'] for speaker in d['speakers'] }
topic_lookup = {topic['id']: topic['name'] for topic in d['topics'] }

for quote in d["quotes"]:
    name = speaker_lookup[quote["speaker"]]    
    date, d_error = cleanDate(quote["date"])
    
    quote_content = TEMPLATE_quote.replace(">>date_normalized<<", date)
    quote_content = quote_content.replace(">>date<<", str(quote["date"]))
    quote_content = quote_content.replace(">>main_topic<<", topic_lookup[quote["main_topic"]])
    quote_content = quote_content.replace(">>page<<", str(quote["page"]))
    quote_content = quote_content.replace(">>quote<<", quote["quote"].replace('>', '\>').replace('<', '\<'))
    quote_content = quote_content.replace(">>source<<", f"'{str(quote['source']).replace(':', ';')}'")
    quote_content = quote_content.replace(">>speaker<<", name)
    
    spiegel_note = f"Gutachten Seite: {str(quote['page'])}"
    if quote["note"]:
        q = quote['note'].replace('>', '\>').replace('<', '\<')
        spiegel_note = f"{spiegel_note}. {q}"
        
    quote_content = quote_content.replace(">>note<<", spiegel_note)
        
    match topic_lookup[quote["main_topic"]]:
        case "Menschenwürde":
            topic_long = "Verstoß gegen die Menschenwürde."
        case "Demokratieprinzip":
            topic_long = "Verstoß gegen das Demokratieprinzip."
        case "Rechtsstaatsprinzip":
            topic_long = "Verstoß gegen das Rechtsstaatsprinzip."
        case "Nationalsozialismus":
            topic_long = "Position zum Nationalsozialismus."
        case "Sonstiges":
            topic_long = "Sonstiges."
        case _:
            topic_long = topic_lookup[quote["main_topic"]]
    quote_content = quote_content.replace(">>topic_long<<", topic_long)
    
    parse_note = None    
    if d_error == 1:
        parse_note = f"Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: {str(quote['date'])}"

    
    fname = cleanWindowsFilename(quote['quote'])
    l = min(len(fname), 50)    
    fname = fname[:l].strip()
    filename, count = getUniqueFilename(f"{folder_path}/Personen/{name}/Zitate/{fname}.md")
    if count > 1:
        if parse_note:
            parse_note = f"{parse_note}\nEs handelt sich möglicherweiße um ein Duplikat von dem Zitat: [[{fname}]]"
        else:
            parse_note = f"Es handelt sich möglicherweise um ein Duplikat von dem Zitat: [[{fname}]]"
        
    quote_content = quote_content.replace(">>parse_note<<", parse_note or "Keine")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(quote_content)
        
    