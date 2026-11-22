# build_new_phases.py
import os
import shutil
from create_curriculum import SHARED_CSS, SHARED_JS
from data_new_phase1 import P1_TOPICS
from data_new_phase2 import P2_TOPICS

BASE_DIR = r"C:\Users\Administrator\Desktop\Machine Learning"
P1_BASE = os.path.join(BASE_DIR, "Phase_01_Data_Analysis_and_Manipulation", "Topics")
P2_BASE = os.path.join(BASE_DIR, "Phase_02_Data_Visualization_and_Reporting", "Topics")

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

    full_code = "\n\n".join(code_parts)
    full_output = "\n\n".join(out_parts)
    steps_html = "".join(step_cards)

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
            <span class="badge badge-green">Project Lab: Topic {topic['num']}</span>
        </div>
        <h1>{topic['title_bn']} — প্র্যাকটিক্যাল ল্যাব</h1>
        <p class="subtitle">{topic['scenario']}</p>
    </header>

    <div class="callout callout-info">
        <strong>প্রজেক্ট অবজেক্টিভ:</strong> নিচের কোড ব্লকগুলো ধাপে ধাপে পর্যবেক্ষণ করে অ্যালগরিদমটি কীভাবে কাজ করে তা আয়ত্ত করুন। প্রতিটি কোডের জন্য ওয়ান-ট্যাপ কপি বাটন রয়েছে।
    </div>

    {steps_html}

    <div class="section-card">
        <h2><span class="step-num">★</span> সম্পূর্ণ পাইপলাইন স্ক্রিপ্ট (Full Integration)</h2>
        <div class="code-container">
            <div class="code-header">
                <span class="code-title">complete_pipeline.py</span>
            </div>
            <pre><code>{full_code}</code></pre>
        </div>
        <div class="terminal-box">
            <div class="term-title">Full Terminal Output</div>
            <pre><code>{full_output}</code></pre>
        </div>
    </div>
</div>

{SHARED_JS}
</body>
</html>
"""

def generate_phase(topics, base_path, phase_tag):
    os.makedirs(base_path, exist_ok=True)
    for topic in topics:
        topic_dir = os.path.join(base_path, topic["dir_name"])
        project_dir = os.path.join(topic_dir, "Project")
        os.makedirs(project_dir, exist_ok=True)

        # 1. Study Guide
        study_guide_html = build_study_guide(topic, phase_tag)
        with open(os.path.join(topic_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(study_guide_html)

        # 2. Project Walkthrough
        proj_walkthrough_html = build_project_walkthrough(topic, phase_tag)
        with open(os.path.join(project_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(proj_walkthrough_html)

        # 3. Clean raw scripts if any
        for f in os.listdir(project_dir):
            if f.endswith(".py") or f.endswith(".pyc") or f == "__pycache__":
                full_p = os.path.join(project_dir, f)
                if os.path.isdir(full_p):
                    shutil.rmtree(full_p)
                else:
                    os.remove(full_p)

        print(f"✅ Generated {phase_tag} Topic {topic['num']} ({topic['dir_name']})")

if __name__ == "__main__":
    print(f"Generating New Phase 01 ({len(P1_TOPICS)} topics)...")
    generate_phase(P1_TOPICS, P1_BASE, "Phase 01: Data Analysis & Manipulation")

    print(f"\nGenerating New Phase 02 ({len(P2_TOPICS)} topics)...")
    generate_phase(P2_TOPICS, P2_BASE, "Phase 02: Data Visualization & Reporting")

    print("\nAll topics generated successfully!")
