import requests
import json


def get_licenses(gem_names):
    licenses = []
    
    with open("ruby_cache/licenses.json") as f:
        cache = json.load(f)
        
    for gem_name in gem_names:
        print(gem_name)
        license = cache.get(gem_name)
        if license:
            licenses.append({gem_name: license})
        else:
            license = fetch_license(gem_name)
            licenses.append({gem_name: license})
            add_gem_to_cache(gem_name, license)
            
    return licenses


def fetch_license(gem_name):
    r = requests.get(
        'https://rubygems.org/api/v1/gems/{}.json'.format(gem_name))
    
    if r.status_code != 200:
        return "error"
    
    data = r.json()
    
    return data.get("licenses", "unknown")


def add_gem_to_cache(gem_name, license):
    with open("ruby_cache/licenses.json",'r+') as file:
        file_data = json.load(file)
        file_data[gem_name] = license
        file.seek(0)
        json.dump(file_data, file, indent = 4)
