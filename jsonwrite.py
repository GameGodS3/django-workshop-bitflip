import json
import os.path
import os
json_string = """
{
  "entries": [
    {
      "title": "This is a sample title",
      "description": "Sample description"
    }
  ]
}
"""

json_string = json.loads(json_string)


def CreateJson(title, description):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('jsonfile.json', 'r') as f:
        js = json.load(f)
        data = js['entries']
        data.append(dict({'title': title, 'description': description}))
        js.update({'entries': data})
        f.close()

    with open('jsonfile.json', 'w') as f:
        json.dump(js, f, indent=4)
        f.close()
