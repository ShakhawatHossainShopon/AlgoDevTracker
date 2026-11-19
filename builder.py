# builder.py
import os
import shutil
from bs4 import BeautifulSoup
from create_curriculum import SHARED_CSS, SHARED_JS
from data_phase1 import P1_TOPICS
from data_phase2 import P2_TOPICS

BASE_DIR = r"C:\Users\Administrator\Desktop\Machine Learning"
P1_BASE = os.path.join(BASE_DIR, "Phase_01_Python_for_Data_Science", "Topics")
P2_BASE = os.path.join(BASE_DIR, "Phase_02_Mathematics_for_Data_Science", "Topics")

def build_study_guide(topic, phase_tag):
    return f"""<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{topic['title_bn']}</title>
    <style>
{SHARED_CSS}
    </style>
</head>
<body>

<div class="container">
    <div class="nav-bar">
        <a href="../../../index.html" class="nav-link">← মাস্টার সিলেবাস ড্যাশবোর্ড</a>
        <a href="./Project/index.html" class="nav-link">🚀 প্রজেক্ট ল্যাব ড্যাশবোর্ড</a>
    </div>

    <header>
        <div class="badge-row">
            <span class="badge">{phase_tag}</span>
            <span class="badge badge-green">Topic {topic['num']}: {topic['title_en']}</span>
        </div>
        <h1>{topic['title_bn']}</h1>
        <p class="subtitle">{topic['scenario']}</p>
    </header>

    <div class="section-card">
        <h2><span class="step-num">০১</span> থিওরি ও মূল কনসেপ্ট</h2>
        {topic['theory_bn']}
    </div>

    <div class="section-card">
        <h2><span class="step-num">০২</span> বাস্তব ট্রেডিং কোড উদাহরণ</h2>
        <div class="code-container">
            <div class="code-header">
                <span class="code-title">trading_example.py</span>
            </div>
            <pre><code>{topic['step1_code']}</code></pre>
        </div>
        <div class="terminal-box">
            <div class="term-title">Terminal Output</div>
            <pre><code>{topic['step1_out']}</code></pre>
        </div>
        <div class="explanation-box">
            <strong>ব্যাখ্যা:</strong> {topic['step1_exp']}
        </div>
    </div>

    <div class="section-card">
        <h2><span class="step-num">০৩</span> মোবাইল রিডিং টেকঅ্যাওয়ে (Key Takeaways)</h2>
        <ul>
            <li><strong>রিয়েল-ওয়ার্ল্ড অ্যাপ্লিকেশন:</strong> {topic['scenario']}</li>
            <li><strong>দক্ষতা অর্জন:</strong> অ্যালগরিদমিক ট্রেডিং সিস্টেমে ডেটার সঠিক আর্কিটেকচার ও গণনা নিশ্চিত করা।</li>
            <li><strong>পরবর্তী পদক্ষেপ:</strong> নিচের বাটনে ট্যাপ করে প্রজেক্ট ল্যাব ড্যাশবোর্ডে গিয়ে ধাপে ধাপে সম্পূর্ণ কোড ওয়াকথ্রু দেখে নিন।</li>
        </ul>
        <a href="./Project/index.html" class="btn-action">প্রজেক্ট ল্যাব ড্যাশবোর্ড খুলুন →</a>
    </div>
</div>

{SHARED_JS}
</body>
</html>
"""

def build_project_walkthrough(topic, phase_tag):
    step_cards = []
    code_parts = []
    out_parts = []

    # Step 1
    if "step1_title" in topic:
        step_cards.append(f"""
    <div class="section-card">
        <h2><span class="step-num">০১</span> {topic['step1_title']}</h2>
        <div class="code-container">
            <div class="code-header">
                <span class="code-title">step_01.py</span>
            </div>
            <pre><code>{topic['step1_code']}</code></pre>
        </div>
        <div class="terminal-box">
            <div class="term-title">Terminal Output</div>
            <pre><code>{topic['step1_out']}</code></pre>
        </div>
        <div class="explanation-box">
            <strong>লাইন-বাই-লাইন বিশ্লেষণ:</strong> {topic['step1_exp']}
        </div>
    </div>
""")
        code_parts.append(f"# 1. {topic['step1_title']}\n{topic['step1_code']}")
        out_parts.append(f"--- Step 1 Output ---\n{topic['step1_out']}")

    # Step 2
    if "step2_title" in topic:
        step_cards.append(f"""
    <div class="section-card">
        <h2><span class="step-num">০২</span> {topic['step2_title']}</h2>
        <div class="code-container">
            <div class="code-header">
                <span class="code-title">step_02.py</span>
            </div>
            <pre><code>{topic['step2_code']}</code></pre>
        </div>
        <div class="terminal-box">
            <div class="term-title">Terminal Output</div>
            <pre><code>{topic['step2_out']}</code></pre>
        </div>
        <div class="explanation-box">
            <strong>লাইন-বাই-লাইন বিশ্লেষণ:</strong> {topic['step2_exp']}
        </div>
    </div>
""")
        code_parts.append(f"# 2. {topic['step2_title']}\n{topic['step2_code']}")
        out_parts.append(f"--- Step 2 Output ---\n{topic['step2_out']}")

    # Step 3
    if "step3_title" in topic:
        step_cards.append(f"""
    <div class="section-card">
        <h2><span class="step-num">০৩</span> {topic['step3_title']}</h2>
        <div class="code-container">
            <div class="code-header">
                <span class="code-title">step_03.py</span>
            </div>
            <pre><code>{topic['step3_code']}</code></pre>
        </div>
        <div class="terminal-box">
            <div class="term-title">Terminal Output</div>
            <pre><code>{topic['step3_out']}</code></pre>
        </div>
        <div class="explanation-box">
            <strong>লাইন-বাই-লাইন বিশ্লেষণ:</strong> {topic['step3_exp']}
        </div>
    </div>
""")
        code_parts.append(f"# 3. {topic['step3_title']}\n{topic['step3_code']}")
        out_parts.append(f"--- Step 3 Output ---\n{topic['step3_out']}")

    full_code = f"# {topic['title_en']}\n\n" + "\n\n".join(code_parts)
    full_out = "\n\n".join(out_parts)
    bengali_digits = ["০১", "০২", "০৩", "০৪", "০৫"]
    final_step_num = bengali_digits[len(step_cards)] if len(step_cards) < len(bengali_digits) else "শেষ ধাপ"

    rendered_steps = "\n".join(step_cards)

    return f"""<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>প্রজেক্ট ল্যাব: {topic['title_bn']}</title>
    <style>
{SHARED_CSS}
    </style>
</head>
<body>

<div class="container">
    <div class="nav-bar">
        <a href="../../../../index.html" class="nav-link">← মাস্টার সিলেবাস</a>
        <a href="../index.html" class="nav-link">📖 থিওরি গাইড</a>
    </div>

    <header>
        <div class="badge-row">
            <span class="badge">{phase_tag}</span>
            <span class="badge badge-green">Project {topic['num']}: Visual Walkthrough</span>
        </div>
        <h1>{topic['title_bn']}</h1>
        <p class="subtitle"><strong>ট্রেডিং প্রেক্ষাপট:</strong> {topic['scenario']}</p>
    </header>

{rendered_steps}

    <div class="section-card">
        <h2><span class="step-num">{final_step_num}</span> সম্পূর্ণ কার্যকর কোড (Full Script)</h2>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.5rem;">
            নিচের কোডটি এক ট্যাপে কপি করে অন্য যেকোনো জায়গায় টেস্ট বা স্টাডি করতে পারেন:
        </p>
        <div class="code-container">
            <div class="code-header">
                <span class="code-title">complete_solution.py</span>
            </div>
            <pre><code>{full_code}</code></pre>
        </div>
        <div class="terminal-box">
            <div class="term-title">Full Terminal Output</div>
            <pre><code>{full_out}</code></pre>
        </div>
        <div class="callout callout-tip">
            <strong>💡 মোবাইল রিডিং টিপস:</strong> উপরের <code>📋 Copy Code</code> বাটন ট্যাপ করে সম্পূর্ণ কোড এবং <code>📋 Copy Output</code> ট্যাপ করে টার্মিনাল রেজাল্ট কপি করতে পারেন।
        </div>
    </div>
</div>

{SHARED_JS}
</body>
</html>
"""

def generate_topic(topic, base_dir, phase_tag):
    topic_dir = os.path.join(base_dir, topic["dir"])
    project_dir = os.path.join(topic_dir, "Project")
    os.makedirs(project_dir, exist_ok=True)

    # Clean any raw files inside project_dir
    for item in os.listdir(project_dir):
        if item != "index.html":
            path = os.path.join(project_dir, item)
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)

    # 1. Study Guide index.html
    study_html = build_study_guide(topic, phase_tag)
    with open(os.path.join(topic_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(study_html)

    # 2. Project Walkthrough index.html
    proj_html = build_project_walkthrough(topic, phase_tag)
    with open(os.path.join(project_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(proj_html)

    print(f"✅ Generated {topic['id']} ({topic['dir']})")

def main():
    print("Generating Phase 1 topics...")
    for t in P1_TOPICS:
        generate_topic(t, P1_BASE, "Phase 01: Python for Data Science")

    print("\nGenerating Phase 2 topics...")
    for t in P2_TOPICS:
        generate_topic(t, P2_BASE, "Phase 02: Mathematics for Data Science")

    print("\nAll topics generated successfully!")

if __name__ == "__main__":
    main()
