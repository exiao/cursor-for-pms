#!/usr/bin/env python3
"""Run with python3 test-site.py; needs only Python, bash, and Node."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from html.parser import HTMLParser
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def check_assets(page):
    for tag, attrs in page.tags:
        for key in ('href', 'src'):
            value = attrs.get(key, '')
            url = urlsplit(value)
            if value and not url.scheme and not value.startswith(('#', '//')):
                assert (ROOT / url.path).is_file(), value


def check_builds():
    # The old service settings must not restore the retired brand on either domain.
    for domain, old_title, old_image in [
        ('cursorpm.com', 'Cursor for Product Managers', 'og-cursor.png'),
        ('claudecodepm.com', 'Claude Code for Product Managers', 'og-claude.png'),
    ]:
        with tempfile.TemporaryDirectory(prefix='course-site-', dir=os.environ.get('TMPDIR')) as tmp:
            for name in ('index.html', 'build.sh'):
                shutil.copy2(ROOT / name, tmp)
            env = dict(os.environ, SITE_URL='https://' + domain, OG_TITLE=old_title, OG_IMAGE=old_image)
            subprocess.run(['bash', 'build.sh'], cwd=tmp, env=env, check=True, capture_output=True)
            text = (Path(tmp) / 'index.html').read_text()
            assert not re.search(r'__(SITE_URL|OG_IMAGE|OG_TITLE)__', text)
            tags = Page(text).tags
            meta = {a.get('property', a.get('name')): a.get('content') for t, a in tags if t == 'meta'}
            assert meta['og:url'] == 'https://' + domain
            for key in ('og:title', 'twitter:title'):
                assert meta[key] == 'Claude Code and Codex for Product Managers', (domain, key, meta[key])
            for key in ('og:image', 'twitter:image'):
                assert meta[key] == 'https://' + domain + '/assets/og-claude.png'
                assert (ROOT / urlsplit(meta[key]).path.lstrip('/')).is_file()
            assert any(t == 'link' and a.get('rel') == 'icon' and a.get('href') == 'assets/favicon-terminal.svg' for t, a in tags)
            check_assets(Page(text))
            print('PASS built metadata and local assets:', domain)


def check_scripts(text):
    scripts = [s for s in re.findall(r'<script\b[^>]*>(.*?)</script>', text, re.S) if s.strip()]
    for script in scripts:
        subprocess.run(['node', '--check'], input=script, text=True, check=True, capture_output=True)
    rollover = next(s for s in scripts if "querySelectorAll('[data-live-until]')" in s)
    # Execute the shipped script with a controlled clock and minimal DOM boundary.
    harness = r'''
const assert = require('node:assert/strict');
const vm = require('node:vm');
const script = SCRIPT;
const end = Date.parse('2026-11-13T18:00:00Z');
for (const start of [end - 1, end, end + 1]) {
    let now = start, removed = false;
    const timers = [];
    const label = {textContent: 'Save your spot', dataset: {liveLabel: 'Watch the recording'}};
    const badge = {dataset: {liveUntil: '2026-11-13T18:00:00Z'},
        closest: () => ({querySelector: () => label}), remove: () => {removed = true;}};
    vm.runInNewContext(script, {
        Date: {now: () => now, parse: Date.parse},
        document: {querySelectorAll: () => removed ? [] : [badge]},
        setTimeout: (fn, delay) => timers.push({fn, delay}),
    });
    if (start < end) {
        assert.equal(removed, false);
        assert.equal(label.textContent, 'Save your spot');
        assert.ok(timers.length, 'An open page must roll over without a reload');
        now = end;
        timers.shift().fn();
    }
    assert.equal(removed, true);
    assert.equal(label.textContent, 'Watch the recording');
}
console.log('PASS lesson rollover: before, exactly at, after, and open-page transition');
'''
    import json
    subprocess.run(['node'], input=harness.replace('SCRIPT', json.dumps(rollover)), text=True, check=True)
    print('PASS inline JavaScript syntax:', len(scripts), 'scripts')


if __name__ == '__main__':
    source = (ROOT / 'index.html').read_text()
    check_builds()
    check_scripts(source)
