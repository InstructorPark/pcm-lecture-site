import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We will replace the brand section with a custom test container to showcase both options
test_brand_section = """
      <!-- Option 1: Full transparent logo.png -->
      <a href="#hero" class="brand test-option-1" aria-label="박찬민 강사 홈으로 이동" style="margin-right: 40px;">
        <img src="assets/logo_transparent.png" alt="박찬민 강사" class="brand-logo" style="height: 48px; width: auto; object-fit: contain;" />
      </a>

      <!-- Option 2: Cropped square bird icon in circle, keeping text -->
      <a href="#hero" class="brand test-option-2" aria-label="박찬민 강사 홈으로 이동">
        <span class="brand-mark" aria-hidden="true" style="display: grid; place-items: center; width: 48px; height: 48px; border: 1px solid var(--muted); border-radius: 50%; background: var(--white); position: relative;">
          <img src="assets/logo_icon.png" alt="PCM" class="brand-icon" style="width: 28px; height: 28px; object-fit: contain; display: block; margin: auto;" />
        </span>
        <span class="brand-text">
          <strong>Park Chan-Min</strong>
          <em>Digital &amp; AI Learning</em>
        </span>
      </a>
"""

# Replace the brand section in header
old_brand = """      <a href="#hero" class="brand" aria-label="박찬민 강사 홈으로 이동">
        <span class="brand-mark" aria-hidden="true">PCM</span>
        <span class="brand-text">
          <strong>Park Chan-Min</strong>
          <em>Digital &amp; AI Learning</em>
        </span>
      </a>"""

new_html = html.replace(old_brand, test_brand_section)

with open('index_test.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created index_test.html")
