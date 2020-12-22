# Synchronizes new keys in English to other languages while keeping the previous keys untouched.

#import os

ref_language = 'english'
languages = [
    "braz_por",
    "french",
    "german",
    "polish",
    "russian",
    "simp_chinese",
    "spanish",
]

file_location = "./../localisation/"
file_extension = ".yml"
files = [
    "pw_ambitions_l_",
    "pw_armies_l_",
    "pw_ascension_perks_l_",
    "pw_buildings_l_",
    "pw_decisions_l_",
    "pw_messages_l_",
    "pw_policies_l_"
    "pw_pop_jobs_l_",
    "pw_solipsist_debate_events_"
    "pw_static_modifiers_l_",
    "pw_tech_l_",
    "pw_wonder_events_l_",
]

#Test settings:
# languages = ["other"]
# file_location = './tests/'
# file_extension = ".yml"
# files = ['test_1_l_', 'test_2_l_']

def getLocalisationKeys(ref_file_path):
    '''
        Returns a dictionary with the localisation
        keys as keys and the localisation
        content as values.
    '''
    local_map = {}

    try:
        with open(ref_file_path) as ref_file:
            next(ref_file) #Skips first line
            for line in ref_file:
                line = line.lstrip() #Clears whitespaces
                if line and not line.startswith('#'):
                    split_line = line.split(':', 1)
                    local_map[split_line[0]] = split_line[1]
    except FileNotFoundError:
        print("File Not Found: ", ref_file_path)
        raise

    return local_map

def appendLocalisationKeys(file_path, localisationMap):
    '''
        Appends a dictionary with the localisation
        keys and content to a file.
    '''

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write('\n')
        for key in localisationMap:
            file.write('    {0}:{1}'.format(key, localisationMap[key]))
            print("Added {0} key to {1}".format(key, file_path))

def getDiffDict(ref_dict, comp_dict):
    '''
        Return a distionary with the missing items from comp_dict
        using ref_dict as reference.
    '''

    ref_keys = ref_dict.keys()  # retrieve keys of the reference dictionary
    comp_keys = comp_dict.keys()  # retrieve keys of the other dictionary
    missing_keys = [key for key in ref_keys if key not in comp_keys]

    result_dict = {}
    for key in missing_keys:
        result_dict[key] = ref_dict[key]

    return result_dict


def createNewLanguageFile(file_path, language):
    '''
        Creates a new file in the specified path with the header:
        l_[language passed]:
    '''
    print("Creating new file: ", file_path)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('l_{0}:\n\n    '.format(language))

for file in files:
    try:
        ref_keys = getLocalisationKeys(
            file_location + ref_language + '/' + file + ref_language + file_extension)
    except:
        print("Skipping file: ", file_location + ref_language +
              '/' + file + ref_language + file_extension)
        continue
    for language in languages:
        file_path = file_location + language + '/' + file + language + file_extension
        try:
            current_keys = getLocalisationKeys(file_path)
        except FileNotFoundError: #No file for the current language
            createNewLanguageFile(file_path, language)
            current_keys = {}
        missing_keys = getDiffDict(ref_keys, current_keys)
        if (missing_keys):
            appendLocalisationKeys(file_path, missing_keys)
