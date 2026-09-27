#!/usr/bin/env python3
"""Publish this homepage with the GitHub CLI after signing into e-fei."""
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = 'e-fei/e-fei.github.io'
GH = shutil.which('gh')
if not GH:
    raise SystemExit('Install GitHub CLI from https://cli.github.com/, then run gh auth login.')

def run(*args, capture=False):
    return subprocess.run(args, cwd=ROOT, check=True, text=True,
                          stdout=subprocess.PIPE if capture else None).stdout

login = run(GH, 'api', 'user', '--jq', '.login', capture=True).strip()
if login != 'e-fei':
    raise SystemExit('Please sign into the e-fei GitHub account first.')
# Do not overwrite an existing repository or rely on an ambiguous 404.
repos = json.loads(run(GH, 'repo', 'list', 'e-fei', '--limit', '1000',
                     '--json', 'nameWithOwner', capture=True))
if any(r['nameWithOwner'].lower() == REPO.lower() for r in repos):
    raise SystemExit('The repository already exists. Inspect it before updating; no files were pushed.')
if not (ROOT / '.git').exists():
    run('git', 'init', '-b', 'main')
remotes = run('git', 'remote', capture=True).split()
if 'origin' in remotes:
    current = run('git', 'remote', 'get-url', 'origin', capture=True).strip()
    if current != 'https://github.com/' + REPO + '.git':
        raise SystemExit('Unexpected origin; no remote was modified.')
else:
    run('git', 'remote', 'add', 'origin', 'https://github.com/' + REPO + '.git')
run('git', 'add', '.')
if subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=ROOT).returncode:
    run('git', '-c', 'user.name=e-fei', '-c', 'user.email=e-fei@users.noreply.github.com',
        'commit', '-m', 'Set up academic homepage based on WowPage')
run(GH, 'repo', 'create', REPO, '--public', '--description', 'Academic personal homepage',
    '--homepage', 'https://e-fei.github.io')
run(GH, 'auth', 'setup-git')
run('git', 'push', '-u', 'origin', 'main')
run(GH, 'api', '--method', 'POST', 'repos/' + REPO + '/pages',
    '-f', 'source[branch]=main', '-f', 'source[path]=/')
print('Repository created and Pages build requested. Verify the deployment status before sharing the website.')
