#!/usr/bin/env python3
"""Build a single self-contained HTML file with JSZM + Zork inlined."""

import os

ROOT = '/home/user/workspace/Liquid_SDK_Test/Liquid_SDK_Test'

# JSZM: prefer the in-repo copy, fall back to /tmp
jszm_path = os.path.join(ROOT, 'web', 'jszm.js')
if not os.path.exists(jszm_path):
    jszm_path = '/tmp/jszm.js'
with open(jszm_path, 'r') as f:
    jszm = f.read()

# Story file base64: prefer in-repo copy
b64_path = os.path.join(ROOT, 'web', 'zork1.z5.b64')
if not os.path.exists(b64_path):
    b64_path = '/tmp/zork1.b64'
with open(b64_path, 'r') as f:
    story_b64 = f.read().strip()

# World JSON (parsed ZIL source); embedded as raw JSON inside a <script type="application/json">
world_path = os.path.join(ROOT, 'web', 'zork-world.json')
with open(world_path, 'r') as f:
    world_json = f.read().strip()
# Avoid breaking the <script> tag if the JSON ever contains </script>
world_json = world_json.replace('</', '<\\/')

# Read HTML template
with open(os.path.join(ROOT, 'web', '_template.html'), 'r') as f:
    template = f.read()

out = template.replace('/*INLINE_JSZM*/', jszm)
out = out.replace('INLINE_STORY_B64', story_b64)
out = out.replace('INLINE_WORLD_JSON', world_json)

with open(os.path.join(ROOT, 'web', 'zork-chat.html'), 'w') as f:
    f.write(out)

# Also keep web/index.html in sync for GitHub Pages
with open(os.path.join(ROOT, 'web', 'index.html'), 'w') as f:
    f.write(out)

print(f"Built zork-chat.html and index.html: {len(out):,} chars")
