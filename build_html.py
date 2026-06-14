#!/usr/bin/env python3
"""Build a single self-contained HTML file with JSZM + Zork inlined."""

with open('/tmp/jszm.js', 'r') as f:
    jszm = f.read()

with open('/tmp/zork1.b64', 'r') as f:
    story_b64 = f.read().strip()

# Read HTML template
with open('/home/user/workspace/Liquid_SDK_Test/Liquid_SDK_Test/web/_template.html', 'r') as f:
    template = f.read()

out = template.replace('/*INLINE_JSZM*/', jszm)
out = out.replace('INLINE_STORY_B64', story_b64)

with open('/home/user/workspace/Liquid_SDK_Test/Liquid_SDK_Test/web/zork-chat.html', 'w') as f:
    f.write(out)

print(f"Built zork-chat.html: {len(out):,} chars")
