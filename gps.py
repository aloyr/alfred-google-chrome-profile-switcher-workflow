import glob
import json
import os
import sys

prof_dir = os.environ['HOME'] + '/Library/Application Support/Google/Chrome'
if not os.path.exists(prof_dir):
    sys.exit()
if len(sys.argv) > 1:
    args = sys.argv[1]
else:
    args = ''


def get_profiles():
    profiles = glob.glob(prof_dir + '/*/Preferences')
    output = {'items': []}
    for profile in profiles:
        with open(profile, 'r') as f:
            prefs = json.load(f)
        profile_id = profile.split('/')[-2:-1]
        profile_name = prefs['profile']['name']
        if profile_name.lower().find(args.lower()) < 0:
            continue
        profile_new = {'title': profile_name, 'arg': profile_id}
        output['items'].append(profile_new)
    return json.dumps(output)


print(get_profiles())
