import json
import argparse


parser = argparse.ArgumentParser(description="Add plugin version to repo index")

parser.add_argument("plugin_id", help="Plugin ID")
parser.add_argument("version", help="Plugin version (e.g. 0.2.1)")
parser.add_argument("app_version", help="Required app version (e.g. >=0.4.2)")
parser.add_argument("hash", help="SHA256 hash of plugin.zip")
parser.add_argument("url", help="Download URL")

args = parser.parse_args()

with open('com.github.funpayhub.repo.json', 'r', encoding='utf-8') as f:
    REPO = json.load(f)


def add_plugin_version(
    plugin_id: str,
    version: str,
    app_version: str,
    hash: str,
    url: str,
):
    if plugin_id not in REPO['plugins']:
        raise ValueError(f'Plugin {plugin_id} not found in repo.')

    REPO['plugins'][plugin_id][version] = {
        'hash': hash,
        'app_version': app_version,
        'url': url,
    }

    with open('com.github.funpayhub.repo.json', 'w', encoding='utf-8') as f:
        json.dump(REPO, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    add_plugin_version(
        args.plugin_id,
        args.version,
        args.app_version,
        args.hash,
        args.url,
    )
