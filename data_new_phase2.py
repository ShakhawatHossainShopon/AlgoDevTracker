# data_new_phase2.py
# Phase 02: Data Visualization & Reporting (15 Topics)

P2_TOPICS = [
    {
        "num": "01",
        "dir_name": "01_Matplotlib_Fundamentals",
        "title_en": "Matplotlib Fundamentals",
        "title_bn": "টপিক ০১: Matplotlib ফান্ডামেন্টালস ও ফিন্যান্সিয়াল চার্টিং",
        "scenario": "অ্যালগো ট্রেডিংয়ের হিস্টোরিক্যাল ইকুইটি কার্ভ ও প্রাইস সিরিজ এক্সপোর্ট করার জন্য অবজেক্ট-ওরিয়েন্টেড Matplotlib আর্কিটেকচার সেটআপ।",
        "theory_bn": """
            <p><strong>Matplotlib</strong> হলো পাইথনের সবচেয়ে শক্তিশালী এবং নির্ভরযোগ্য ভিজ্যুয়ালাইজেশন লাইব্রেরি। এর দুটি ইন্টারফেস রয়েছে: <code>pyplot</code> (MATLAB স্টাইল স্টেট-মেশিন) এবং <strong>Object-Oriented API</strong> (<code>fig, ax = plt.subplots()</code>)। প্রফেশনাল ফিন্যান্সিয়াল চার্টিংয়ের জন্য অবজেক্ট-ওরিয়েন্টেড পদ্ধতি ব্যবহার করা অপরিহার্য কারণ এতে প্রতিটি সাবপ্লট ও অ্যাক্সিস নিখুঁতভাবে কাস্টমাইজ করা যায়।</p>
        """,
        "step1_title": "অবজেক্ট-ওরিয়েন্টেড ফিগার ও অ্যাক্সিস তৈরি",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

# সিন্থেটিক ট্রেডিং দিন ও পোর্টফোলিও ব্যালেন্স
days = np.arange(1, 6)
portfolio_equity = np.array([10000, 10250, 10180, 10600, 10850])

fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
ax.plot(days, portfolio_equity, color="#2563eb", linewidth=2, marker="o", label="Equity Curve")

ax.set_title("Trading Portfolio Growth Trajectory", fontsize=12, fontweight="bold")
ax.set_xlabel("Trading Day")
ax.set_ylabel("Portfolio Value ($)")
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()

print("Figure and Axes Initialized Successfully.")
print("Final Equity Value: $", portfolio_equity[-1])""",
        "step1_out": """Figure and Axes Initialized Successfully.
Final Equity Value: $ 10850""",
        "step1_exp": "plt.subplots() দিয়ে ফিগার ও অ্যাক্সিস অবজেক্ট তৈরি করে লাইন প্লট, গ্রিড ও লিজেন্ড যোগ করা হয়েছে।",

        "step2_title": "হাই-রেজোলিউশন চার্ট এক্সপোর্ট (savefig)",
        "step2_code": """# ফিন্যান্সিয়াল রিপোর্টের জন্য হাই-ডিপিআই পিএনজি বা ভেক্টর এসভিজি এক্সপোর্ট
# fig.savefig("equity_curve.png", dpi=300, bbox_inches="tight")
print("Chart Render Settings:")
print("- Resolution: 300 DPI")
print("- Layout Bounding Box: Tight")
print("- Format: PNG / SVG Vector Ready")""",
        "step2_out": """Chart Render Settings:
- Resolution: 300 DPI
- Layout Bounding Box: Tight
- Format: PNG / SVG Vector Ready""",
        "step2_exp": "bbox_inches='tight' ব্যবহার করলে চার্টের কোনো লেবেল বা অ্যাক্সিস কাটবে না এবং ক্রিস্প ভেক্টর রেজোলিউশন পাওয়া যাবে।",

        "step3_title": "স্টাইলিং ও থিম কনফিগারেশন",
        "step3_code": """print("Default Matplotlib Styles Available:", len(plt.style.available))
print("Popular Financial Styles:", [s for s in plt.style.available if "seaborn" in s or "dark" in s][:3])""",
        "step3_out": """Default Matplotlib Styles Available: 28
Popular Financial Styles: ['dark_background', 'seaborn-v0_8', 'seaborn-v0_8-bright']""",
        "step3_exp": "বিল্ট-ইন স্টাইল শিট ব্যবহার করে যেকোনো চার্টে সহজে ডার্ক বা লাইট প্রাতিষ্ঠানিক থিম প্রয়োগ করা যায়।"
    },
    {
        "num": "02",
        "dir_name": "02_Figure_and_Axes",
        "title_en": "Figure and Axes Architecture",
        "title_bn": "টপিক ০২: মাল্টি-প্যানেল চার্ট আর্কিটেকচার (Price + Volume)",
        "scenario": "প্রাইস অ্যাকশন এবং ট্রেডিং ভলিউমের জন্য শেয়ার্ড এক্স-অ্যাক্সিসসহ প্রফেশনাল টু-প্যানেল চার্ট আর্কিটেকচার গঠন।",
        "theory_bn": """
            <p>ট্রেডিং টার্মিনালে প্রাইস এবং ভলিউম কখনো একটি অ্যাক্সিসে আঁকা হয় না। <code>gridspec_kw</code> বা <code>plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]})</code> ব্যবহার করে উপরের প্যানেলে বড় প্রাইস চার্ট এবং নিচের প্যানেলে ছোট ভলিউম বার তৈরি করা হয়।</p>
        """,
        "step1_title": "শেয়ার্ড এক্স-অ্যাক্সিস টু-প্যানেল সাবপ্লট",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

time_bars = np.arange(1, 6)
prices = np.array([67000, 67200, 67150, 67450, 67600])
volumes = np.array([120, 240, 95, 310, 450])

fig, (ax_price, ax_vol) = plt.subplots(
    nrows=2, ncols=1, figsize=(8, 6), sharex=True,
    gridspec_kw={'height_ratios': [3, 1]}
)

# টপ প্যানেল: প্রাইস লাইন
ax_price.plot(time_bars, prices, color="#10b981", linewidth=2, label="BTC Price")
ax_price.set_ylabel("Price ($)")
ax_price.grid(True, alpha=0.3)
ax_price.legend()

# বটম প্যানেল: ভলিউম বার
ax_vol.bar(time_bars, volumes, color="#64748b", alpha=0.7, label="Volume")
ax_vol.set_ylabel("Volume")
ax_vol.set_xlabel("Bar Index")
ax_vol.grid(True, alpha=0.3)

print("Dual Panel Layout Configured:")
print("Price Height Ratio: 3 | Volume Height Ratio: 1")""",
        "step1_out": """Dual Panel Layout Configured:
Price Height Ratio: 3 | Volume Height Ratio: 1""",
        "step1_exp": "sharex=True ব্যবহারের ফলে প্রাইস জুম বা প্যান করলে ভলিউম চার্টের টাইমলাইন স্বয়ংক্রিয়ভাবে একসাথে সিঙ্ক থাকবে।",

        "step2_title": "টুইন অ্যাক্সিস (Twinx) প্রয়োগ",
        "step2_code": """# একটি প্যানেলেই দুই ভিন্ন স্কেলের ডেটা (যেমন Price & RSI)
fig_single, ax1 = plt.subplots(figsize=(8, 3))
ax2 = ax1.twinx()

ax1.plot(time_bars, prices, 'g-', label="Close Price")
ax2.plot(time_bars, [45, 52, 48, 68, 74], 'b--', label="RSI")

ax1.set_ylabel("Price ($)", color='g')
ax2.set_ylabel("RSI (0-100)", color='b')

print("Twin Axes Created: Independent Y-Scales for Single Subplot")""",
        "step2_out": """Twin Axes Created: Independent Y-Scales for Single Subplot""",
        "step2_exp": "twinx() মেথড একই এক্স-অ্যাক্সিসের ওপর ডানে আরেকটি স্বতন্ত্র স্কেলের ওয়াই-অ্যাক্সিস তৈরি করে।",

        "step3_title": "অ্যাক্সিস স্পাইন ও লেবেল ফরম্যাটিং",
        "step3_code": """ax_price.spines['top'].set_visible(False)
ax_price.spines['right'].set_visible(False)
print("Upper and Right Spines Hidden for Modern Minimalist Look")""",
        "step3_out": """Upper and Right Spines Hidden for Modern Minimalist Look""",
        "step3_exp": "চার্টের অপ্রয়োজনীয় বর্ডার বক্সের স্পাইন হাইড করে পরিষ্কার মডার্ন লুক তৈরি করা হয়েছে।"
    },
    {
        "num": "03",
        "dir_name": "03_Line_Charts",
        "title_en": "Line Charts & Moving Average Crossovers",
        "title_bn": "টপিক ০৩: লাইন চার্ট ও মুভিং অ্যাভারেজ গোল্ডেন ক্রস",
        "scenario": "হিস্টোরিক্যাল প্রাইসের সাথে ৫০ ও ২০০ পিরিয়ডের সিম্পল মুভিং অ্যাভারেজ (SMA) ক্রসওভার ভিজ্যুয়ালাইজেশন ও সিগন্যাল মার্কিং।",
        "theory_bn": """
            <p><strong>Line Chart</strong> হলো কোয়ান্ট ফিন্যান্সের প্রাথমিক চার্ট। যখন ৫০ পিরিয়ড মুভিং অ্যাভারেজ ২০০ পিরিয়ড মুভিং অ্যাভারেজকে নিচ থেকে উপরের দিকে ক্রস করে, তাকে <em>Golden Cross</em> (বুলিশ) বলে। চার্টে লাইন প্লটিং এবং <code>fill_between</code> ব্যবহার করে সিগন্যাল রিজিয়ন হাইলাইট করা যায়।</p>
        """,
        "step1_title": "মুভিং অ্যাভারেজ লাইন প্লটিং",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

periods = np.arange(1, 11)
price = np.array([100, 102, 105, 107, 106, 110, 114, 118, 122, 125])
sma_fast = np.array([np.nan, np.nan, 102.3, 104.7, 106.0, 107.7, 110.0, 114.0, 118.0, 121.7])
sma_slow = np.array([np.nan, np.nan, np.nan, np.nan, 104.0, 106.0, 108.4, 111.0, 114.4, 117.8])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(periods, price, label="Close Price", color="#94a3b8", alpha=0.6)
ax.plot(periods, sma_fast, label="SMA 3 (Fast)", color="#2563eb", linewidth=2)
ax.plot(periods, sma_slow, label="SMA 5 (Slow)", color="#ea580c", linewidth=2)

ax.set_title("SMA Crossover Strategy Visualization")
ax.legend()
ax.grid(True, linestyle=":", alpha=0.6)

print("SMA Fast and Slow Lines Plotted.")""",
        "step1_out": """SMA Fast and Slow Lines Plotted.""",
        "step1_exp": "বিভিন্ন উইন্ডোর মুভিং অ্যাভারেজকে ভিন্ন রঙের লাইনে প্লট করে ট্রেন্ড আইডেন্টিফাই করা হয়েছে।",

        "step2_title": "fill_between দিয়ে বুলিশ জোন ফিলিং",
        "step2_code": """# ফাস্ট এসএমএ যখন স্লো এসএমএ-র ওপরে তখন গ্রিন শেড
bullish_cond = sma_fast >= sma_slow
ax.fill_between(periods, sma_fast, sma_slow, where=bullish_cond, color="#10b981", alpha=0.2, label="Bullish Regime")

print("Regime Fill Applied: Green Shading between Curves.")""",
        "step2_out": """Regime Fill Applied: Green Shading between Curves.""",
        "step2_exp": "fill_between মেথড দিয়ে দুটি লাইনের মধ্যকার স্পেস শর্ত অনুযায়ী স্বয়ংক্রিয়ভাবে রঙে পূর্ণ করা যায়।",

        "step3_title": "মার্কার ও অ্যানোটেশন যোগ",
        "step3_code": """# ক্রসওভার পয়েন্টে গোল্ডেন ক্রস অ্যারো
ax.annotate("Golden Cross", xy=(6, 108), xytext=(4, 115),
            arrowprops=dict(facecolor="#10b981", shrink=0.05, width=1, headwidth=6))
print("Golden Cross Annotation Marker Configured.")""",
        "step3_out": """Golden Cross Annotation Marker Configured.""",
        "step3_exp": "annotate() মেথডের সাহায্যে নির্দিষ্ট কোঅর্ডিনেটে তীর চিহ্নসহ টেক্সট নোট বসানো হয়েছে।"
    },
    {
        "num": "04",
        "dir_name": "04_Bar_Charts",
        "title_en": "Bar Charts & Monthly Strategy Returns",
        "title_bn": "টপিক ০৪: বার চার্ট ও মাসিক স্ট্র্যাটেজি PnL রিটার্নস",
        "scenario": "অ্যালগরিদম ব্যাকটেস্টিংয়ের পর প্রতি মাসের প্রফিট/লস (PnL) ধনাত্মক হলে সবুজ এবং ঋণাত্মক হলে লাল বারে উপস্থাপন করা।",
        "theory_bn": """
            <p><strong>Bar Chart</strong> ক্যাটাগরিক্যাল এবং নির্দিষ্ট ডিসক্রিট ইন্টারভ্যালের পারফরম্যান্স মূল্যায়নে ব্যবহৃত হয়। কোয়ান্টাম রিপোর্টে ১২ মাসের রিটার্নস তুলনা করার সময় কালার কন্ডিশনিং (Positive = Green, Negative = Red) দিয়ে এক নজরে লাভ-ক্ষতির অনুপাত দেখা যায়।</p>
        """,
        "step1_title": "কন্ডিশনাল কালার বার চার্ট তৈরি",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_returns = np.array([4.2, -1.8, 6.5, -3.2, 5.1, 2.8, -0.9, 7.4, -4.1, 8.2, 3.6, -1.5])

# রিটার্ন অনুযায়ী কালার অ্যারে
bar_colors = ["#10b981" if r >= 0 else "#ef4444" for r in monthly_returns]

fig, ax = plt.subplots(figsize=(9, 4))
bars = ax.bar(months, monthly_returns, color=bar_colors, edgecolor="#1e293b", linewidth=0.8)

ax.axhline(0, color="#0f172a", linewidth=1)
ax.set_title("Monthly Trading Strategy Returns (%)", fontsize=12, fontweight="bold")
ax.set_ylabel("Return (%)")
ax.grid(axis="y", linestyle="--", alpha=0.4)

print("Positive Months Count:", sum(monthly_returns > 0))
print("Negative Months Count:", sum(monthly_returns < 0))""",
        "step1_out": """Positive Months Count: 7
Negative Months Count: 5""",
        "step1_exp": "লিস্ট কম্প্রিহেনশনের মাধ্যমে ধনাত্মক রিটার্নে সবুজ এবং ঋণাত্মক রিটার্নে লাল রঙের বার প্লট করা হয়েছে।",

        "step2_title": "বারে টেক্সট ভ্যালু লেবেলিং (bar_label)",
        "step2_code": """# প্রতিটি বারের ওপরে রিটার্নের সংখ্যা বসানো
ax.bar_label(bars, fmt="%.1f%%", padding=3, fontsize=8)
print("Data Labels Added on Top of Each Bar.")""",
        "step2_out": """Data Labels Added on Top of Each Bar.""",
        "step2_exp": "bar_label মেথড প্রতিটি বারের উপরে বা নিচে সুনির্দিষ্ট সংখ্যা স্বয়ংক্রিয়ভাবে প্রদর্শন করে।",

        "step3_title": "হরাইজন্টাল বার চার্ট (barh)",
        "step3_code": """fig_h, ax_h = plt.subplots(figsize=(6, 3))
ax_h.barh(months[:4], monthly_returns[:4], color=bar_colors[:4])
ax_h.set_xlabel("Return (%)")
print("Horizontal Bar Chart Configured for Top Months.")""",
        "step3_out": """Horizontal Bar Chart Configured for Top Months.""",
        "step3_exp": "barh() মেথড ব্যবহার করে আড়াআড়ি বার চার্ট তৈরি করা হয়েছে।"
    },
    {
        "num": "05",
        "dir_name": "05_Histograms",
        "title_en": "Histograms & Distribution Analysis",
        "title_bn": "টপিক ০৫: হিস্টোগ্রাম ও রিটার্ন ডিস্ট্রিবিউশন অ্যানালাইসিস",
        "scenario": "ঐতিহাসিক ডেইলি রিটার্নসের হিস্টোগ্রাম প্লট করে নরমাল বেল কার্ভের সাথে তুলনা এবং আউটলায়ার টেল সনাক্তকরণ।",
        "theory_bn": """
            <p><strong>Histogram</strong> হলো ডেটার ফ্রিকোয়েন্সি ডিস্ট্রিবিউশন দেখার গ্রাফ। ফিন্যান্সিয়াল রিটার্ন নরমাল নাকি লেপ্টোকার্টিক (উঁচু চূড়া ও মোটা লেজযুক্ত ফ্যাট-টেলস) তা হিস্টোগ্রামে বিন্স (bins) সাজিয়ে এবং গাউসিয়ান বেল কার্ভ ওভারলে করে নিশ্চিত হওয়া যায়।</p>
        """,
        "step1_title": "রিটার্ন হিস্টোগ্রাম প্লটিং",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

# ১০০০ দিনের র্যান্ডম রিটার্ন (Fat-tailed Student-t ডিস্ট্রিবিউশন)
np.random.seed(42)
returns = np.random.standard_t(df=5, size=1000) * 0.015

fig, ax = plt.subplots(figsize=(8, 4))
counts, bins, patches = ax.hist(returns * 100, bins=40, density=True, color="#3b82f6", alpha=0.7, edgecolor="white")

ax.set_title("Asset Daily Returns Frequency Distribution", fontweight="bold")
ax.set_xlabel("Daily Return (%)")
ax.set_ylabel("Probability Density")
ax.grid(True, linestyle="--", alpha=0.3)

print("Histogram Bins Count:", len(bins) - 1)
print("Min Return (%):", round(returns.min() * 100, 2))
print("Max Return (%):", round(returns.max() * 100, 2))""",
        "step1_out": """Histogram Bins Count: 40
Min Return (%): -6.74
Max Return (%): 7.39""",
        "step1_exp": "density=True দিয়ে প্রোবাবিলিটি ডেনসিটিতে হিস্টোগ্রাম প্লট করা হয়েছে যাতে তাত্ত্বিক কার্ভের সাথে মেলানো যায়।",

        "step2_title": "নরমাল ডিস্ট্রিবিউশন কার্ভ ওভারলে",
        "step2_code": """from scipy.stats import norm

# রিটার্নের গড় ও স্ট্যান্ডার্ড ডেভিয়েশন
mu = (returns * 100).mean()
sigma = (returns * 100).std()

x_vals = np.linspace(bins[0], bins[-1], 200)
pdf = norm.pdf(x_vals, mu, sigma)

ax.plot(x_vals, pdf, color="#ef4444", linewidth=2, label="Normal Bell Curve Overlay")
ax.legend()

print("Normal Bell Curve Plotted.")
print(f"Fitted Normal: Mean={mu:.3f}%, Sigma={sigma:.3f}%")""",
        "step2_out": """Normal Bell Curve Plotted.
Fitted Normal: Mean=-0.007%, Sigma=1.921%""",
        "step2_exp": "scipy.stats.norm.pdf দিয়ে তাত্ত্বিক নরমাল কার্ভ হিস্টোগ্রামের ওপর বসিয়ে ফ্যাট টেইলস যাচাই করা হয়েছে।",

        "step3_title": "রিস্ক থ্রেশহোল্ড (VaR 95%) ভার্টিক্যাল লাইন",
        "step3_code": """var_line = np.percentile(returns * 100, 5)
ax.axvline(var_line, color="#dc2626", linestyle="--", linewidth=1.5, label=f"95% VaR ({var_line:.2f}%)")
ax.legend()
print(f"95% Value-at-Risk Threshold: {var_line:.2f}%")""",
        "step3_out": """95% Value-at-Risk Threshold: -3.07%""",
        "step3_exp": "axvline দিয়ে ৫% ঝুঁকি সীমানা (VaR) লাল ড্যাশড লাইনে চিহ্নিত করা হয়েছে।"
    },
    {
        "num": "06",
        "dir_name": "06_Scatter_Plots",
        "title_en": "Scatter Plots & Beta Regression",
        "title_bn": "টপিক ০৬: স্ক্যাটার প্লট ও রিস্ক-রিটার্ন বিটা রিগ্রেশন",
        "scenario": "মার্কেটের বেঞ্চমার্কের (S&P 500) বিপরীতে নির্দিষ্ট স্টকের রিটার্ন স্ক্যাটার প্লট করে বেটা ($\beta$) স্লোপ লাইন আঁকা।",
        "theory_bn": """
            <p><strong>Scatter Plot</strong> দুটি কন্টিনিউয়াস ভ্যারিয়েবলের সম্পর্ক (Correlation) দেখতে ব্যবহৃত হয়। ক্যাপিটাল অ্যাসেট প্রাইসিং মডেলে (CAPM) স্টকের রিটার্ন বনাম মার্কেট রিটার্ন প্লট করে রিগ্রেশন লাইনের যে ঢাল পাওয়া যায় তাই হলো <em>Beta</em> ($\beta$)—যা মার্কেটের প্রতি অ্যাসেটটির সংবেদনশীলতা নির্দেশ করে।</p>
        """,
        "step1_title": "মার্কেট বনাম স্টক রিটার্ন স্ক্যাটার প্লট",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
sp500_ret = np.random.normal(0.0005, 0.012, 100)
# স্টক বিটা = 1.35 + নয়েজ
stock_ret = 1.35 * sp500_ret + np.random.normal(0.0, 0.006, 100)

fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(sp500_ret * 100, stock_ret * 100, color="#2563eb", alpha=0.6, edgecolors="none", label="Daily Return Points")

ax.set_title("Asset vs Benchmark (S&P 500) Sensitivity", fontweight="bold")
ax.set_xlabel("S&P 500 Return (%)")
ax.set_ylabel("Asset Return (%)")
ax.grid(True, linestyle=":", alpha=0.5)

print("Scatter Plot Rendered with 100 Observation Points.")""",
        "step1_out": """Scatter Plot Rendered with 100 Observation Points.""",
        "step1_exp": "ax.scatter() মেথড প্রতিটি ট্রেডিং দিনের বেঞ্চমার্ক ও স্টক রিটার্ন ডট আকারে প্লট করেছে।",

        "step2_title": "লিনিয়ার রিগ্রেশন বেটা ($\beta$) ফিটিং (np.polyfit)",
        "step2_code": """# ১ ডিগ্রির পলিনোমিয়াল ফিট (y = mx + c)
beta, alpha = np.polyfit(sp500_ret, stock_ret, 1)

x_line = np.linspace(sp500_ret.min(), sp500_ret.max(), 50)
y_line = beta * x_line + alpha

ax.plot(x_line * 100, y_line * 100, color="#dc2626", linewidth=2, label=f"CAPM Beta = {beta:.2f}")
ax.legend()

print(f"Calculated Beta Slope: {beta:.3f}")
print(f"Calculated Alpha Intercept: {alpha:.5f}")""",
        "step2_out": """Calculated Beta Slope: 1.385
Calculated Alpha Intercept: -0.00034""",
        "step2_exp": "np.polyfit ব্যবহার করে সরাসরি বেটা ঢাল (১.৩৮৫) ও আলফা ইন্টারসেপ্ট বের করে রিগ্রেশন লাইন আঁকা হয়েছে।",

        "step3_title": "ভলিউম সাইজিং দিয়ে বাবল চার্ট (Bubble Plot)",
        "step3_code": """volumes = np.random.uniform(50, 400, 100)
fig_b, ax_b = plt.subplots(figsize=(6, 4))
ax_b.scatter(sp500_ret[:20]*100, stock_ret[:20]*100, s=volumes[:20], alpha=0.5, color="#059669")
ax_b.set_title("Volume Weighted Returns (Bubble Plot)")
print("Bubble Size Mapped to Traded Volume.")""",
        "step3_out": """Bubble Size Mapped to Traded Volume.""",
        "step3_exp": "scatter() এর s প্যারামিটারে ভলিউম পাস করে বাবল চার্ট তৈরি করা হয়েছে।"
    },
    {
        "num": "07",
        "dir_name": "07_Box_Plots",
        "title_en": "Box Plots & Session Volatility",
        "title_bn": "টপিক ০৭: বক্স প্লট ও ট্রেডিং সেশন ভোলাটিলিটি তুলনা",
        "scenario": "টোকিও, লন্ডন এবং নিউইয়র্ক সেশনের রিটার্ন ও স্প্রেড বক্স-প্লটের মাধ্যমে পাশাপাশি তুলনা করে আউটলায়ার শনাক্তকরণ।",
        "theory_bn": """
            <p><strong>Box Plot (Tukey Box & Whisker)</strong> ডেটার পাঁচটি প্রধান সারাংশ (Minimum, Q1 25%, Median 50%, Q3 75%, Maximum) এবং আউটলায়ার প্রকাশ করে। ইন্টারকোয়ার্টাইল রেঞ্জের ($IQR = Q3 - Q1$) ১.৫ গুণের বেশি দূরবর্তী পয়েন্টগুলোকে ডট আকারে আউটলায়ার হিসেবে দেখানো হয়।</p>
        """,
        "step1_title": "ট্রেডিং সেশন ভিত্তিক বক্স প্লট",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

np.random.seed(7)
tokyo_ret = np.random.normal(0.001, 0.005, 80)
london_ret = np.random.normal(0.003, 0.015, 80)
ny_ret = np.random.normal(0.002, 0.022, 80)

data_to_plot = [tokyo_ret * 100, london_ret * 100, ny_ret * 100]

fig, ax = plt.subplots(figsize=(7, 5))
box = ax.boxplot(data_to_plot, patch_artist=True, labels=["Tokyo", "London", "New York"])

# বক্সের কালার কাস্টমাইজেশন
colors = ["#93c5fd", "#86efac", "#fca5a5"]
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title("Return Volatility Across Global Trading Sessions", fontweight="bold")
ax.set_ylabel("Return Distribution (%)")
ax.grid(True, linestyle="--", alpha=0.4)

print("Box Plot Generated for 3 Sessions.")""",
        "step1_out": """Box Plot Generated for 3 Sessions.""",
        "step1_exp": "টোকিও সেশন সবচেয়ে শান্ত এবং নিউইয়র্ক সেশন সবচেয়ে বেশি স্প্রেড ও ভোলাটাইল তা বক্সের সাইজ দেখে পরিষ্কার বোঝা যাচ্ছে।",

        "step2_title": "মিডিয়ান ও হুইস্কার কাস্টমাইজেশন",
        "step2_code": """for median in box['medians']:
    median.set(color='#0f172a', linewidth=2)

for flier in box['fliers']:
    flier.set(marker='o', color='#dc2626', alpha=0.6)

print("Median Line and Outlier Fliers Styled.")""",
        "step2_out": """Median Line and Outlier Fliers Styled.""",
        "step2_exp": "হুইস্কারের বাইরের আউটলায়ার পয়েন্টগুলো লাল মার্কার দিয়ে স্পষ্ট করা হয়েছে।",

        "step3_title": "হরাইজন্টাল ও নচড বক্স প্লট (Notched)",
        "step3_code": """fig_n, ax_n = plt.subplots(figsize=(6, 3))
ax_n.boxplot(data_to_plot, notch=True, vert=False, labels=["TYO", "LDN", "NYC"])
ax_n.set_xlabel("Return (%)")
print("Notched Horizontal Box Plot Rendered.")""",
        "step3_out": """Notched Horizontal Box Plot Rendered.""",
        "step3_exp": "নচড বক্স প্লট মিডিয়ান মানের ৯৫% কনফিডেন্স ইন্টারভাল প্রদর্শন করে।"
    },
    {
        "num": "08",
        "dir_name": "08_Distribution_Visualization",
        "title_en": "Advanced Distribution Visualization (KDE & Violin)",
        "title_bn": "টপিক ০৮: কার্নেল ডেনসিটি (KDE) ও ভায়োলিন প্লট",
        "scenario": "হিস্টোগ্রামের ধাপযুক্ত বিন্সের সীমাবদ্ধতা দূর করে স্মুথ কার্নেল ডেনসিটি এস্টিমেশন ও ভায়োলিন প্লটে ট্রেড PnL বিশ্লেষণ।",
        "theory_bn": """
            <p><strong>Kernel Density Estimation (KDE)</strong> বিচ্ছিন্ন বিন্সের ওপর নির্ভর না করে নন-প্যারামেট্রিক পদ্ধতিতে স্মুথ প্রোবাবিলিটি ডেনসিটি কার্ভ তৈরি করে। অন্যদিকে <strong>Violin Plot</strong> বক্স প্লটের সুবিধার পাশাপাশি প্রতিটি পয়েন্টের ডেনসিটি একসাথে প্রদর্শন করে।</p>
        """,
        "step1_title": "KDE ডেনসিটি কার্ভ প্লটিং",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

np.random.seed(99)
strategy_pnl = np.concatenate([
    np.random.normal(150, 40, 200),  # নিয়মিত ছোট উইন
    np.random.normal(-300, 100, 50)  # মাঝেমধ্যে বড় ড্রডাউন
])

density = gaussian_kde(strategy_pnl)
xs = np.linspace(-600, 300, 300)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(xs, density(xs), color="#2563eb", linewidth=2.5, label="KDE Density")
ax.fill_between(xs, density(xs), color="#93c5fd", alpha=0.4)

ax.set_title("Strategy Trade PnL Density Estimation (KDE)", fontweight="bold")
ax.set_xlabel("Profit / Loss per Trade ($)")
ax.set_ylabel("Density")
ax.axvline(0, color="#ef4444", linestyle="--", label="Breakeven ($0)")
ax.legend()

print("KDE Curve Rendered with Bimodal/Asymmetric Shape.")""",
        "step1_out": """KDE Curve Rendered with Bimodal/Asymmetric Shape.""",
        "step1_exp": "KDE দিয়ে দেখা যাচ্ছে বেশিরভাগ ট্রেড +$১৫০ প্রফিটে ক্লাস্টার হলেও বামে দীর্ঘ লস টেল রয়েছে।",

        "step2_title": "ভায়োলিন প্লট (Violin Plot)",
        "step2_code": """fig_v, ax_v = plt.subplots(figsize=(6, 4))
parts = ax_v.violinplot([strategy_pnl], showmeans=True, showmedians=True)

ax_v.set_title("Trade PnL Violin Distribution")
ax_v.set_ylabel("PnL ($)")

print("Violin Plot Rendered: Shows Median, Mean and Density Shape.")""",
        "step2_out": """Violin Plot Rendered: Shows Median, Mean and Density Shape.""",
        "step2_exp": "ভায়োলিন প্লট এক পলকে ডেনসিটির পেট এবং গড়/মিডিয়ান প্রদর্শন করেছে।",

        "step3_title": "কিউমুলেটিভ ডেনসিটি ফাংশন (CDF)",
        "step3_code": """sorted_pnl = np.sort(strategy_pnl)
cdf = np.arange(len(sorted_pnl)) / float(len(sorted_pnl))

fig_c, ax_c = plt.subplots(figsize=(6, 3))
ax_c.plot(sorted_pnl, cdf, color="#059669", linewidth=2)
ax_c.set_title("Empirical CDF of Trade PnL")
ax_c.set_ylabel("Cumulative Probability")
print("CDF Plotted: Easily Find Probability of Losing Money.")""",
        "step3_out": """CDF Plotted: Easily Find Probability of Losing Money.""",
        "step3_exp": "CDF কার্ভ দেখে যেকোনো PnL এর চেয়ে কম বা বেশি হওয়ার সম্ভাবনা তাৎক্ষণিকভাবে বোঝা যায়।"
    },
    {
        "num": "09",
        "dir_name": "09_Correlation_Heatmaps",
        "title_en": "Correlation Heatmaps",
        "title_bn": "টপিক ০৯: কোরিলেশন হিটম্যাপ ও ডাইভারসিফিকেশন ম্যাট্রিক্স",
        "scenario": "৮টি ভিন্ন ফাইন্যান্সিয়াল অ্যাসেটের রিটার্ন কোরিলেশন কালার গ্রেডিয়েন্ট হিটম্যাপে প্লট করে হেজিং পেয়ার নির্বাচন।",
        "theory_bn": """
            <p><strong>Heatmap</strong> হলো 2D ম্যাট্রিক্সের সেলগুলোর সংখ্যাগত মানকে রঙের তীব্রতায় রূপান্তর করা। পোর্টফোলিও ম্যানেজমেন্টে দুটি অ্যাসেটের কোরিলেশন -১ থেকে +১ এর মধ্যে থাকে। +১ হলে পারফেক্ট পজিটিভ, ০ হলে আনকোরিলেটেড এবং -১ হলে পারফেক্ট হেজিং পেয়ার।</p>
        """,
        "step1_title": "Matplotlib imshow দিয়ে কোরিলেশন হিটম্যাপ",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

assets = ["BTC", "ETH", "SOL", "GOLD", "US30", "OIL"]

# সিন্থেটিক কোরিলেশন ম্যাট্রিক্স (6 x 6)
corr_matrix = np.array([
    [ 1.00,  0.88,  0.78,  0.12,  0.35,  0.22],
    [ 0.88,  1.00,  0.82,  0.15,  0.38,  0.25],
    [ 0.78,  0.82,  1.00,  0.08,  0.29,  0.18],
    [ 0.12,  0.15,  0.08,  1.00, -0.15,  0.05],
    [ 0.35,  0.38,  0.29, -0.15,  1.00,  0.42],
    [ 0.22,  0.25,  0.18,  0.05,  0.42,  1.00]
])

fig, ax = plt.subplots(figsize=(6, 5))
cax = ax.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)

ax.set_xticks(range(len(assets)))
ax.set_yticks(range(len(assets)))
ax.set_xticklabels(assets)
ax.set_yticklabels(assets)

fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)
ax.set_title("Cross-Asset Return Correlation Heatmap", fontweight="bold")

print("Correlation Heatmap Rendered.")""",
        "step1_out": """Correlation Heatmap Rendered.""",
        "step1_exp": "ax.imshow() মেথড এবং coolwarm কালারম্যাপ ব্যবহার করে -১ (ঠান্ডা/নীল) থেকে +১ (উষ্ণ/লাল) স্কেলে হিটম্যাপ তৈরি করা হয়েছে।",

        "step2_title": "হিটম্যাপের প্রতিটি সেলে টেক্সট অ্যানোটেশন",
        "step2_code": """for i in range(len(assets)):
    for j in range(len(assets)):
        val = corr_matrix[i, j]
        text_color = "white" if abs(val) > 0.6 else "black"
        ax.text(j, i, f"{val:.2f}", ha="center", va="center", color=text_color, fontsize=9)

print("Correlation Coefficients Annotated Inside Cells.")""",
        "step2_out": """Correlation Coefficients Annotated Inside Cells.""",
        "step2_exp": "প্রতিটি সেলের মাঝখানে সঠিক কোরিলেশন সংখ্যা প্রিন্ট করা হয়েছে।"
    },
    {
        "num": "10",
        "dir_name": "10_Time_Series_Visualization",
        "title_en": "Time Series Underwater Drawdown Charts",
        "title_bn": "টপিক ১০: আন্ডারওয়াটার ড্রডাউন ও ক্র্যাশ ভিজ্যুয়ালাইজেশন",
        "scenario": "পিক-টু-ট্রাফ ক্যাপিটাল ড্রডাউন আন্ডারওয়াটার চার্ট আকারে প্রদর্শন করে সবচেয়ে দীর্ঘস্থায়ী রিকভারি পিরিয়ড চিহ্নিত করা।",
        "theory_bn": """
            <p><strong>Underwater Chart</strong> হলো পোর্টফোলিওর অল-টাইম পিক (High Water Mark) থেকে বর্তমান মূলধনের পতন শতকরা হারে নিচের দিকে প্লট করা (০% থেকে -৩০% ইত্যাদি)। এতে এক নজরে দেখা যায় কৌশলটি কতদিন ড্রডাউনের নিচে ছিল (Drawdown Duration)।</p>
        """,
        "step1_title": "আন্ডারওয়াটার ড্রডাউন এরিয়া প্লট",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

periods = np.arange(1, 13)
equity = np.array([100, 105, 103, 98, 95, 99, 102, 108, 104, 101, 109, 115])

# অল টাইম পিক
peak = np.maximum.accumulate(equity)
drawdown_pct = (equity - peak) / peak * 100

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(periods, drawdown_pct, color="#dc2626", linewidth=1.8, label="Underwater Drawdown")
ax.fill_between(periods, drawdown_pct, 0, color="#ef4444", alpha=0.3)

ax.set_title("Strategy Underwater Drawdown Curve (%)", fontweight="bold")
ax.set_ylabel("Drawdown from Peak (%)")
ax.set_xlabel("Time Period")
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend()

print("Max Drawdown (%):", round(drawdown_pct.min(), 2))""",
        "step1_out": """Max Drawdown (%): -9.52""",
        "step1_exp": "সর্বোচ্চ ক্ষতি (-৯.৫২%) লাল শেডে পানির নিচের অংশ হিসেবে দৃশ্যমান হয়েছে।",

        "step2_title": "রিকভারি পিরিয়ড হাইলাইট",
        "step2_code": """# যেখানে ড্রডাউন ০% হয়েছিল সেই পিক পয়েন্টগুলো
recovery_points = np.where(drawdown_pct == 0)[0] + 1
ax.scatter(recovery_points, np.zeros_like(recovery_points), color="#10b981", s=60, zorder=5, label="New Equity Highs")
ax.legend()
print("New Peak Equity Points:", list(recovery_points))""",
        "step2_out": """New Peak Equity Points: [1, 2, 8, 11, 12]""",
        "step2_exp": "যেসব সময়ে অ্যাকাউন্ট পুরনো ক্ষতি কাটিয়ে নতুন শীর্ষে পৌঁছেছে সেগুলো সবুজ পয়েন্টে দেখানো হয়েছে।"
    },
    {
        "num": "11",
        "dir_name": "11_Statistical_Visualization",
        "title_en": "Statistical Visualization & QQ-Plots",
        "title_bn": "টপিক ১১: স্ট্যাটিস্টিক্যাল কিউ-কিউ (QQ) প্লট ও নরমালিটি টেস্ট",
        "scenario": "রিটার্নস ডেটা নরমাল ডিস্ট্রিবিউশন মেনে চলে কিনা তা Quantile-Quantile (QQ) প্লটের মাধ্যমে ভিজ্যুয়ালি পরীক্ষা করা।",
        "theory_bn": """
            <p><strong>QQ-Plot (Quantile-Quantile Plot)</strong> হলো ডেটার পার্সেন্টাইলগুলোকে তাত্ত্বিক নরমাল ডিস্ট্রিবিউশনের পার্সেন্টাইলের বিপরীতে প্লট করা। ডেটা যদি পুরোপুরি ৪৫-ডিগ্রি সরলরেখার ওপর পড়ে তবে তা নরমাল। ফিন্যান্সিয়াল ডেটাতে সাধারণত দুই প্রান্তে সরলরেখা থেকে পয়েন্টগুলো ছিটকে যায়—যা ফ্যাট-টেইল রিস্কের প্রমাণ।</p>
        """,
        "step1_title": "scipy.stats probplot দিয়ে QQ প্লট",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

np.random.seed(55)
# নন-নরমাল ফিন্যান্সিয়াল রিটার্ন
heavy_tail_returns = np.random.standard_t(df=3, size=250)

fig, ax = plt.subplots(figsize=(6, 5))
res = stats.probplot(heavy_tail_returns, dist="norm", plot=ax)

ax.get_lines()[0].set_markerfacecolor("#2563eb")
ax.get_lines()[0].set_markersize(5)
ax.get_lines()[1].set_color("#dc2626")
ax.get_lines()[1].set_linewidth(2)

ax.set_title("Normal Q-Q Plot of Asset Returns", fontweight="bold")
ax.grid(True, alpha=0.3)

print("QQ Plot Rendered: Curvature at Extremes Indicates Fat Tails.")""",
        "step1_out": """QQ Plot Rendered: Curvature at Extremes Indicates Fat Tails.""",
        "step1_exp": "দুই প্রান্তে লাল লাইন থেকে নীল ডটগুলোর বিচ্যুতি নির্দেশ করছে চরম মার্কেট মুভমেন্ট স্বাভাবিক সম্ভাবনার চেয়ে বেশি ঘটে।",

        "step2_title": "হিস্টোগ্রাম বনাম কিউ-কিউ ডায়াগনস্টিক",
        "step2_code": """skew = stats.skew(heavy_tail_returns)
kurt = stats.kurtosis(heavy_tail_returns)

print(f"Empirical Skewness: {skew:.3f}")
print(f"Empirical Excess Kurtosis: {kurt:.3f} (Significant Fat-Tails)")""",
        "step2_out": """Empirical Skewness: 0.281
Empirical Excess Kurtosis: 4.892 (Significant Fat-Tails)""",
        "step2_exp": "কার্টোসিস ৪.৮৯২ হওয়ার কারণে কিউ-কিউ প্লটে দুই প্রান্তের বিচ্যুতির গাণিতিক সত্যতা পাওয়া গেছে।"
    },
    {
        "num": "12",
        "dir_name": "12_Interactive_Visualization",
        "title_en": "Interactive Visualization Concepts",
        "title_bn": "টপিক ১২: ইন্টারেক্টিভ ক্যান্ডেলস্টিক চার্টিং ও জুমিং",
        "scenario": "মোবাইল ও ড্যাশবোর্ডে ক্যান্ডেলস্টিক চার্ট জুম, প্যান ও ক্রসহেয়ার দিয়ে প্রতিটি বারের বিশদ তথ্য ইন্টারেক্টিভলি দেখার আর্কিটেকচার।",
        "theory_bn": """
            <p>স্ট্যাটিক ইমেজ চার্টের চেয়ে ব্রাউজারে ইন্টারেক্টিভ চার্ট (যেমন Plotly, Lightweight Charts বা Canvas) অনেক বেশি তথ্যবহ। ব্যবহারকারী মাউস ওভার বা আঙুল দিয়ে স্পর্শ করলে ওএইচএলসি, টাইমস্ট্যাম্প ও ভলিউম টুলটিপ আকারে ভেসে ওঠে।</p>
        """,
        "step1_title": "ক্যান্ডেলস্টিক উইক ও বডি জ্যামিতি",
        "step1_code": """# ম্যাটপ্লটলিব বা ক্যানভাসে ক্যান্ডেল জ্যামিতি কনফিগারেশন
candle = {"Open": 67200, "High": 67450, "Low": 67100, "Close": 67400}

is_bullish = candle["Close"] >= candle["Open"]
body_top = max(candle["Open"], candle["Close"])
body_bottom = min(candle["Open"], candle["Close"])
body_height = body_top - body_bottom

print("Candle Direction:", "Bullish (Green)" if is_bullish else "Bearish (Red)")
print("Upper Shadow Length:", candle["High"] - body_top)
print("Real Body Height:", body_height)
print("Lower Shadow Length:", body_bottom - candle["Low"])""",
        "step1_out": """Candle Direction: Bullish (Green)
Upper Shadow Length: 50
Real Body Height: 200
Lower Shadow Length: 100""",
        "step1_exp": "ক্যান্ডেলস্টিক চার্ট রেন্ডার করার জন্য রিয়েল বডি এবং আপার/লোয়ার শ্যাডোর গাণিতিক দৈর্ঘ্য বের করা হয়েছে।",

        "step2_title": "ইন্টারেক্টিভ টুলটিপ ডেটা পে-লোড প্রস্তুত",
        "step2_code": """tooltip_payload = {
    "time": "2026-10-01 10:00:00",
    "open": candle["Open"],
    "high": candle["High"],
    "low": candle["Low"],
    "close": candle["Close"],
    "change_pct": round((candle["Close"] / candle["Open"] - 1) * 100, 2)
}
print("Interactive Tooltip JSON:\\n", tooltip_payload)""",
        "step2_out": """Interactive Tooltip JSON:
 {'time': '2026-10-01 10:00:00', 'open': 67200, 'high': 67450, 'low': 67100, 'close': 67400, 'change_pct': 0.3}""",
        "step2_exp": "ইন্টারেক্টিভ গ্রাফে মাউস হোভারে দ্রুত দেখানোর জন্য JSON ফরম্যাটে বার ইনফরমেশন প্রস্তুত রাখা হয়েছে।"
    },
    {
        "num": "13",
        "dir_name": "13_Dashboard_Fundamentals",
        "title_en": "Dashboard Fundamentals & GridSpec",
        "title_bn": "টপিক ১৩: গ্রিডস্পেক (GridSpec) ড্যাশবোর্ড আর্কিটেকচার",
        "scenario": "একই ক্যানভাসে প্রাইস, আরএসআই (RSI), ইকুইটি কার্ভ এবং কি-স্ট্যাটিস্টিকস কার্ডের মাল্টিপল উইজেট গ্রিড তৈরি করা।",
        "theory_bn": """
            <p><strong>GridSpec</strong> হলো Matplotlib-এর অ্যাডভান্সড সাবপ্লট ম্যানেজার যা দিয়ে অসমান আকারের গ্রিড লেআউট বানানো যায়। যেমন ৩টি রো ও ২টি কলামের গ্রিডে প্রথম উইজেটটি পুরো উপরের রো দখল করতে পারে, আর নিচের সারিতে ২টি আলাদা ছোট চার্ট থাকতে পারে।</p>
        """,
        "step1_title": "৩-প্যানেল গ্রিডস্পেক লেআউট গঠন",
        "step1_code": """import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 6))
gs = GridSpec(nrows=3, ncols=2, figure=fig, height_ratios=[3, 1, 1.5])

# টপ ফুল-উইডথ প্রাইস চার্ট (রো ০, সব কলাম)
ax_main = fig.add_subplot(gs[0, :])
# মিডল লেফট: RSI (রো ১, কলাম ০)
ax_rsi = fig.add_subplot(gs[1, 0])
# মিডল রাইট: ভলিউম (রো ১, কলাম ১)
ax_vol = fig.add_subplot(gs[1, 1])
# বটম ফুল-উইডথ: ইকুইটি কার্ভ (রো ২, সব কলাম)
ax_eq = fig.add_subplot(gs[2, :])

ax_main.set_title("Master Quant Research Dashboard", fontweight="bold")
ax_main.text(0.5, 0.5, "Primary Price Chart", ha="center")
ax_rsi.text(0.5, 0.5, "RSI (14)", ha="center")
ax_vol.text(0.5, 0.5, "Volume Bars", ha="center")
ax_eq.text(0.5, 0.5, "Strategy Equity Curve", ha="center")

plt.tight_layout()
print("GridSpec Layout Successfully Configured with 4 Distinct Widgets.")""",
        "step1_out": """GridSpec Layout Successfully Configured with 4 Distinct Widgets.""",
        "step1_exp": "GridSpec ব্যবহার করে জটিল মাল্টি-লেআউট ড্যাশবোর্ড নিখুঁতভাবে তৈরি করা হয়েছে।"
    },
    {
        "num": "14",
        "dir_name": "14_Data_Storytelling",
        "title_en": "Data Storytelling & Visual Hierarchy",
        "title_bn": "টপিক ১৪: ডেটা স্টোরিটেলিং ও ভিজ্যুয়াল হায়ারার্কি",
        "scenario": "প্রাতিষ্ঠানিক ইনভেস্টর ও স্টেকহোল্ডারদের কাছে স্ট্র্যাটেজির ড্রডাউন ও প্রফিটাবিলিটি কার্যকর রঙের মনস্তত্ত্ব ও ফোকাসিংয়ে তুলে ধরা।",
        "theory_bn": """
            <p><strong>Data Storytelling</strong> হলো চার্টকে অর্থবহ গল্পে রূপান্তর করা। অপ্রয়োজনীয় রং বা অতিরিক্ত গ্রিডলাইন (Chart Junk) দূর করে মূল ফোকাস পয়েন্ট যেমন ব্রেকআউট বা বিগ ড্রডাউনে দর্শকের দৃষ্টি আকর্ষণ করানো হয়। কালার কন্ট্রাস্ট ও ক্লান্তিহীন ভিজ্যুয়াল ফ্লো বজায় রাখা এর প্রধান উদ্দেশ্য।</p>
        """,
        "step1_title": "কন্ট্রাস্ট ও ফোকাসড হাইলাইটিং",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

periods = np.arange(1, 8)
bench = np.array([100, 102, 101, 103, 102, 104, 105])
strat = np.array([100, 104, 108, 112, 110, 116, 122])

fig, ax = plt.subplots(figsize=(8, 4))
# ব্যাকগ্রাউন্ড বেঞ্চমার্ক মৃদু ধূসর
ax.plot(periods, bench, color="#cbd5e1", linewidth=1.5, label="Market Benchmark (Passive)")
# আমাদের কৌশল গাঢ় বোল্ড নীল
ax.plot(periods, strat, color="#2563eb", linewidth=2.5, marker="o", label="Alpha Algorithm (Active)")

ax.set_title("Significant Outperformance: Alpha Strategy vs Benchmark", fontweight="bold")
ax.legend(frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

print("Visual Hierarchy Established: Strategy Stands Out over Benchmark.")""",
        "step1_out": """Visual Hierarchy Established: Strategy Stands Out over Benchmark.""",
        "step1_exp": "বেঞ্চমার্ককে হালকা ধূসর এবং স্ট্র্যাটেজিকে গাঢ় নীল রঙে ফোকাস করে সরাসরি ভিজ্যুয়াল সুপিরিওরিটি দেখানো হয়েছে।"
    },
    {
        "num": "15",
        "dir_name": "15_Reporting_and_Insights",
        "title_en": "Reporting & Tear-Sheet Export",
        "title_bn": "টপিক ১৫: কোয়ান্টাম স্ট্র্যাটেজি টিয়ার-শীট ও পারফরম্যান্স রিপোর্ট",
        "scenario": "সিএজিআর (CAGR), শার্প রেশিও, ম্যাক্স ড্রডাউন ও উইন রেট সম্বলিত প্রাতিষ্ঠানিক ওয়ান-পেজ টিয়ার-শীট রিপোর্ট তৈরি করা।",
        "theory_bn": """
            <p><strong>Tear-Sheet</strong> হলো একটি অ্যালগো স্ট্র্যাটেজির কমপ্লিট হেলথ রিপোর্ট। এতে একটি সারসংক্ষেপ টেবিল থাকে যাতে CAGR, Annualized Volatility, Sharpe Ratio, Sortino Ratio, Calmar Ratio এবং Maximum Drawdown এক নজরে উপস্থাপন করা হয়।</p>
        """,
        "step1_title": "টিয়ার-শীট কি-মেট্রিক্স টেবিল ও ইকুইটি প্লট",
        "step1_code": """import matplotlib.pyplot as plt
import numpy as np

# পারফরম্যান্স মেট্রিক্স ডিকশনারি
metrics = {
    "CAGR": "24.5 %",
    "Sharpe Ratio": "1.85",
    "Sortino Ratio": "2.40",
    "Max Drawdown": "-8.2 %",
    "Win Rate": "62.4 %",
    "Profit Factor": "1.92"
}

fig, (ax_chart, ax_tbl) = plt.subplots(1, 2, figsize=(10, 4), gridspec_kw={'width_ratios': [2, 1]})

# ইকুইটি গ্রাফ
ax_chart.plot([1, 2, 3, 4], [10000, 10800, 11400, 12450], color="#10b981", linewidth=2)
ax_chart.set_title("Equity Curve ($10k -> $12.45k)", fontweight="bold")
ax_chart.grid(True, alpha=0.3)

# মেট্রিক্স টেবিল
table_data = [[k, v] for k, v in metrics.items()]
ax_tbl.axis("off")
table = ax_tbl.table(cellText=table_data, colLabels=["Metric", "Score"], loc="center", cellLoc="center")
table.scale(1, 1.4)
table.set_fontsize(10)

print("Institutional Strategy Tear-Sheet Compiled Successfully.")""",
        "step1_out": """Institutional Strategy Tear-Sheet Compiled Successfully.""",
        "step1_exp": "গ্রাফ এবং সুন্দর মেট্রিক্স টেবিল সমন্বয়ে এক পৃষ্ঠার প্রাতিষ্ঠানিক টিয়ার-শীট প্রস্তুত করা হয়েছে।"
    }
]
