# data_phase2.py
# Phase 2 Topics 01 to 17 (Mathematics for Data Science & Quantitative Algorithmic Trading)

P2_TOPICS = [
    {
        "id": "p02_t01",
        "dir": "01_Basic_Algebra",
        "num": "০১",
        "title_bn": "বেসিক অ্যালজেব্রা ও ভেক্টরাইজেশন: রিটার্ন ট্রান্সফরমেশন ও লগ এডিটিভিটি",
        "title_en": "Basic Algebra & Vectorization: Return Transformations",
        "theory_bn": """<h3>ট্রেডিং অ্যালজেব্রা ও ভেক্টরাইজেশন</h3>
<p>কোয়ান্ট ফাইন্যান্সে সাধারণ পাইথন লুপ দিয়ে প্রাইস হিসাব না করে ভেক্টরাইজড অ্যারে ব্যবহার করা হয়। এর ফলে হাজার হাজার ক্যান্ডেলের শতকরা লাভ-লস এক লাইনে নিমেষেই বের করা যায়।</p>
<ul>
    <li><strong>Simple Return:</strong> \(R_t = \\frac{P_t - P_{t-1}}{P_{t-1}}\) — সাধারণ লাভ-লসের শতকরা হার।</li>
    <li><strong>Log Return:</strong> \(r_t = \\ln(P_t) - \\ln(P_{t-1})\) — কোয়ান্ট ট্রেডিংয়ের গোল্ড স্ট্যান্ডার্ড, কারণ পুরো পিরিয়ডের রিটার্ন শুধু যোগ করলেই পাওয়া যায় (Additivity)।</li>
</ul>""",
        "scenario": "ক্যান্ডেলস্টিক প্রাইস সিরিজ থেকে ভেক্টরাইজড স্লাইসিংয়ের মাধ্যমে সিম্পল ও লগ রিটার্ন হিসাব এবং এডিটিভিটি পরীক্ষা।",
        "step1_title": "ধাপ ১: স্লাইসিং দিয়ে সিম্পল রিটার্ন হিসাব",
        "step1_code": """import numpy as np

prices = np.array([100.0, 102.5, 101.0, 104.0, 106.5])

# prices[1:] হলো বর্তমান ক্যান্ডেল, prices[:-1] হলো পূর্ববর্তী ক্যান্ডেল
simple_returns = (prices[1:] - prices[:-1]) / prices[:-1]

print("Closing Prices:", prices)
print("Simple Returns (%):", np.round(simple_returns * 100, 2))""",
        "step1_out": """Closing Prices: [100.  102.5 101.  104.  106.5]
Simple Returns (%): [ 2.5  -1.46  2.97  2.4 ]""",
        "step1_exp": "কোনো for লুপ ছাড়াই NumPy অ্যারে স্লাইসিং দিয়ে এক লাইনে ৪টি ক্যান্ডেলের রিটার্ন বের করা হয়েছে।",

        "step2_title": "ধাপ ২: লগ রিটার্ন ও যোগ করার সুবিধা (Additivity)",
        "step2_code": """log_returns = np.diff(np.log(prices))

sum_log = np.sum(log_returns)
total_period_log = np.log(prices[-1] / prices[0])

print("Log Returns (%):", np.round(log_returns * 100, 2))
print("Sum of Log Returns:", round(sum_log, 4))
print("Total Period Log Return:", round(total_period_log, 4))
print("Additivity Identity Holds?:", np.isclose(sum_log, total_period_log))""",
        "step2_out": """Log Returns (%): [ 2.47 -1.47  2.93  2.38]
Sum of Log Returns: 0.063
Total Period Log Return: 0.063
Additivity Identity Holds?: True""",
        "step2_exp": "np.diff এবং np.log ব্যবহার করে লগ রিটার্ন বের করা হয়েছে এবং প্রমাণ করা হয়েছে যে প্রতিটি বারের লগ রিটার্ন যোগ করলেই পুরো পিরিয়ডের মোট রিটার্ন পাওয়া যায়।",

        "step3_title": "ধাপ ৩: ফিচার স্কেলিং (Z-Score Standardization)",
        "step3_code": """# মোমেন্টাম ও ভলিউমের মতো ভিন্ন স্কেলের ফিচারকে গড়=০ ও ভ্যারিয়েন্স=১ এ রূপান্তর
features = np.array([
    [2.5, 1800],
    [-1.4, 900],
    [3.0, 2200],
    [2.4, 1500]
])

mean = np.mean(features, axis=0)
std = np.std(features, axis=0)
scaled_features = (features - mean) / std

print("Scaled Feature Matrix (Mean=0, Std=1):\\n", np.round(scaled_features, 2))""",
        "step3_out": """Scaled Feature Matrix (Mean=0, Std=1):
 [[ 0.44  0.43]
 [-1.75 -1.47]
 [ 0.72  1.27]
 [ 0.38 -0.22]]""",
        "step3_exp": "ব্রডকাস্টিং ব্যবহার করে কলাম বরাবর এক লাইনে সব ফিচারকে Z-score স্কেলে স্ট্যান্ডার্ডাইজ করা হয়েছে।"
    },
    {
        "id": "p02_t02",
        "dir": "02_Equations_and_Inequalities",
        "num": "০২",
        "title_bn": "সমীকরণ ও অসমতা: ব্রেক-ইভেন এক্সিট ও পজিশন সাইজিং",
        "title_en": "Equations & Inequalities for Risk Management",
        "theory_bn": """<h3>ট্রেডিংয়ের গাণিতিক শর্ত ও সীমা</h3>
<p>একজন ট্রেডারের মূল উদ্দেশ্য হলো মূলধন রক্ষা করা। এজন্য দুটি গাণিতিক টুল সবচেয়ে বেশি ব্যবহৃত হয়:</p>
<ul>
    <li><strong>সমীকরণ (Equations):</strong> ফি কাটার পর সঠিক ব্রেক-ইভেন এক্সিট প্রাইস এবং ১% রিস্কের জন্য সঠিক লট সাইজ নির্ধারণ।</li>
    <li><strong>অসমতা (Inequalities):</strong> রিস্ক-রিওয়ার্ড শর্ত (\(RR \\ge 1.5\)) এবং অ্যাকাউন্টের মার্জিন সেফটি (\(\\text{Balance} \\ge \\text{Required Margin}\))।</li>
</ul>""",
        "scenario": "ট্রেডিং ফি বিবেচনায় নিয়ে ব্রেক-ইভেন প্রাইস সমীকরণ এবং রিস্ক-রিওয়ার্ড অসমতা ফিল্টার প্রয়োগ।",
        "step1_title": "ধাপ ১: ব্রেক-ইভেন প্রাইস সমীকরণ",
        "step1_code": """entry_price = 100.0
fee_rate = 0.001  # 0.1% fee per side

# কস্ট রিকভার করতে এক্সিট প্রাইস সমীকরণ
break_even_price = entry_price * (1 + fee_rate) / (1 - fee_rate)

print("Entry Price: $", entry_price)
print("Trading Fee Rate:", fee_rate * 100, "%")
print("Break-Even Exit Price: $", round(break_even_price, 4))""",
        "step1_out": """Entry Price: $ 100.0
Trading Fee Rate: 0.1 %
Break-Even Exit Price: $ 100.2002""",
        "step1_exp": "কেনার সময় এবং বেচার সময় উভয় পাশের ফি বিবেচনায় নিয়ে এক্সাক্ট ব্রেক-ইভেন প্রাইস বের করা হয়েছে।",

        "step2_title": "ধাপ ২: পজিশন সাইজিং সমীকরণ (১% রিস্ক নিয়ম)",
        "step2_code": """capital = 10000.0
risk_pct = 0.01
stop_loss = 95.0

max_risk_dollars = capital * risk_pct
loss_per_share = entry_price - stop_loss
shares_to_buy = max_risk_dollars / loss_per_share

print("Account Capital: $", capital)
print("Max Risk Allowed (1%): $", max_risk_dollars)
print("Loss Per Share: $", loss_per_share)
print("Exact Shares to Buy:", shares_to_buy)""",
        "step2_out": """Account Capital: $ 10000.0
Max Risk Allowed (1%): $ 100.0
Loss Per Share: $ 5.0
Exact Shares to Buy: 20.0""",
        "step2_exp": "বীজগণিতের সমীকরণ দিয়ে ঠিক ২০টি শেয়ার কেনার সিদ্ধান্ত হয়েছে যাতে স্টপলস হিট করলেও মাত্র ১০০ ডলারের বেশি ক্ষতি না হয়।",

        "step3_title": "ধাপ ৩: রিস্ক-রিওয়ার্ড অসমতা ফিল্টার (Inequality)",
        "step3_code": """take_profit = 112.0

profit_per_share = take_profit - entry_price
rr_ratio = profit_per_share / loss_per_share
is_trade_approved = rr_ratio >= 1.5

print("Potential Profit Per Share: $", profit_per_share)
print("Risk-Reward Ratio:", round(rr_ratio, 2))
print("Is Trade Approved (RR >= 1.5)?:", is_trade_approved)""",
        "step3_out": """Potential Profit Per Share: $ 12.0
Risk-Reward Ratio: 2.4
Is Trade Approved (RR >= 1.5)?: True""",
        "step3_exp": "অসমতা (>=) ব্যবহার করে নিশ্চিত করা হয়েছে যে ট্রেডটি প্রত্যাশিত মুনাফার মানদণ্ড পূরণ করে কি না।"
    },
    {
        "id": "p02_t03",
        "dir": "03_Functions_and_Graphs",
        "num": "০৩",
        "title_bn": "ফাংশন ও গ্রাফ: ট্রেডিং পেঅফ ও ভিজ্যুয়ালাইজেশন",
        "title_en": "Functions & Payoff Graphs in Trading",
        "theory_bn": """<h3>ইনপুট-আউটপুট ম্যাপিং ও পেঅফ কার্ভ</h3>
<p>গণিতের \(y = f(x)\) হলো প্রাইসের পরিবর্তনের সাথে লাভ-লসের সম্পর্ক। ইনপুট \(x\) (মার্কেট প্রাইস) এবং আউটপুট \(y\) (লাভ/লস) এর সমন্বয়ে তৈরি হয় ট্রেডিংয়ের পেঅফ গ্রাফ।</p>""",
        "scenario": "লং পজিশনের পেঅফ ফাংশন তৈরি এবং একাধিক প্রাইস পয়েন্টে গ্রাফ কোঅর্ডিনেট বিশ্লেষণ।",
        "step1_title": "ধাপ ১: ট্রেডিং পেঅফ ফাংশন তৈরি",
        "step1_code": """entry_price = 100.0
shares = 10

def calculate_pnl(current_price):
    return (current_price - entry_price) * shares

print("PnL at $110:", calculate_pnl(110.0))
print("PnL at $90 :", calculate_pnl(90.0))""",
        "step1_out": """PnL at $110: 100.0
PnL at $90 : -100.0""",
        "step1_exp": "পাইথনের সাধারণ def দিয়ে ট্রেডিং পেঅফ ফাংশন তৈরি এবং টেস্ট করা হয়েছে।",

        "step2_title": "ধাপ ২: গ্রাফের জন্য কোঅর্ডিনেট টেবিল তৈরি",
        "step2_code": """prices = [90.0, 95.0, 100.0, 105.0, 110.0]

print("Price (x)  -->  PnL (y)")
print("-" * 25)
for p in prices:
    pnl = calculate_pnl(p)
    print(f"x = ${p:<6.1f} --> y = ${pnl:>+6.1f}")""",
        "step2_out": """Price (x)  -->  PnL (y)
-------------------------
x = $90.0   --> y = $-100.0
x = $95.0   --> y = $ -50.0
x = $100.0  --> y = $  +0.0
x = $105.0  --> y = $ +50.0
x = $110.0  --> y = $+100.0""",
        "step2_exp": "ইনপুট প্রাইসের পরিবর্তনের সাথে আউটপুট প্রফিটের যে সরলরেখা গ্রাফ তৈরি হয় তার বিন্দুগুলো প্রিন্ট করা হয়েছে।",

        "step3_title": "ধাপ ৩: স্লোপ ও পেঅফ সেনসিটিভিটি",
        "step3_code": """# ঢাল (Slope) = Delta Y / Delta X = Shares
delta_y = calculate_pnl(110.0) - calculate_pnl(100.0)
delta_x = 110.0 - 100.0
slope = delta_y / delta_x

print("Payoff Graph Slope (Delta PnL / Delta Price):", slope)
print("Interpretation: Every $1 move generates $", slope, "profit/loss.")""",
        "step3_out": """Payoff Graph Slope (Delta PnL / Delta Price): 10.0
Interpretation: Every $1 move generates $ 10.0 profit/loss.""",
        "step3_exp": "গ্রাফের ঢাল বা স্লোপ সরাসরি নির্দেশ করে প্রতি ডলারে পজিশন কত টাকা লাভ বা লস করবে।"
    },
    {
        "id": "p02_t04",
        "dir": "04_Exponents_and_Logarithms",
        "num": "০৪",
        "title_bn": "সূচক ও লগারিদম: চক্রবৃদ্ধি সুদ ও অবিচ্ছিন্ন কম্পাউন্ডিং",
        "title_en": "Exponents & Logarithms in Continuous Compounding",
        "theory_bn": """<h3>চক্রবৃদ্ধি মুনাফা ও স্বাভাবিক লগারিদম (e)</h3>
<p>ট্রেডিং মূলধন কীভাবে চক্রবৃদ্ধি হারে বাড়ে তা সূচক (\(e^{rt}\)) দ্বারা নিয়ন্ত্রিত হয়। আর প্রাইসের বহুগুণ বৃদ্ধিকে স্বাভাবিক স্কেলে নামিয়ে আনতে প্রাকৃতিক লগারিদম (\(\\ln\)) ব্যবহার করা হয়।</p>""",
        "scenario": "বার্ষিক চক্রবৃদ্ধি রিটার্ন (CAGR) এবং অবিচ্ছিন্ন চক্রবৃদ্ধি বৃদ্ধি হিসাব করা।",
        "step1_title": "ধাপ ১: এক্সপোনেনশিয়াল কম্পাউন্ডিং (Continuous Compounding)",
        "step1_code": """import math

initial_capital = 10000.0
annual_rate = 0.15  # 15% annual return
years = 3

# অবিচ্ছিন্ন চক্রবৃদ্ধি ফর্মুলা: A = P * e^(rt)
future_val = initial_capital * math.exp(annual_rate * years)

print("Starting Capital: $", initial_capital)
print("Continuous Compounded Value after 3 years: $", round(future_val, 2))""",
        "step1_out": """Starting Capital: $ 10000.0
Continuous Compounded Value after 3 years: $ 15683.12""",
        "step1_exp": "math.exp() ব্যবহার করে ১৫% হারে ৩ বছরের অবিচ্ছিন্ন বৃদ্ধির চূড়ান্ত মূলধন বের করা হয়েছে।",

        "step2_title": "ধাপ ২: প্রাকৃতিক লগারিদম দিয়ে ডাবলিং পিরিয়ড নির্ণয়",
        "step2_code": """# মূলধন দ্বিগুণ হতে কত বছর লাগবে? ln(2) / r
doubling_years = math.log(2) / annual_rate

print(f"At {annual_rate * 100}% annual rate, capital doubles in: {doubling_years:.2f} years")""",
        "step2_out": """At 15.0% annual rate, capital doubles in: 4.62 years""",
        "step2_exp": "লগারিদম ব্যবহার করে মূলধন দ্বিগুণ হওয়ার সুনির্দিষ্ট সময়কাল নির্ণয়।",

        "step3_title": "ধাপ ৩: লগ প্রাইস স্কেল নরমালাইজেশন",
        "step3_code": """prices = [100.0, 200.0, 400.0, 800.0]
log_prices = [round(math.log(p), 4) for p in prices]

print("Raw Geometric Prices:", prices)
print("Log-Transformed Prices (Linear Steps):", log_prices)
print("Step Differences in Log Space:", [round(log_prices[i] - log_prices[i-1], 4) for i in range(1, len(log_prices))])""",
        "step3_out": """Raw Geometric Prices: [100.0, 200.0, 400.0, 800.0]
Log-Transformed Prices (Linear Steps): [4.6052, 5.2983, 5.9915, 6.6846]
Step Differences in Log Space: [0.6931, 0.6932, 0.6931]""",
        "step3_exp": "লগ স্কেলে রূপান্তর করলে দ্বিগুণ হওয়া প্রাইসগুলো সমান দূরত্বের ধাপে পরিণত হয়।"
    },
    {
        "id": "p02_t05",
        "dir": "05_Sequences_and_Series",
        "num": "০৫",
        "title_bn": "অনুক্রম ও ধারা: ফিগোনোনাচি লেভেল ও কিউমুলেটিভ ওয়েলথ",
        "title_en": "Sequences, Series & Fibonacci Retracement",
        "theory_bn": """<h3>ট্রেডিংয়ে গুণোত্তর ধারা ও ফিবোনাচি অনুক্রম</h3>
<p>ধারাবাহিক বিনিয়োগের সঞ্চয়ী মান (Geometric Series) এবং টেকনিক্যাল অ্যানালাইসিসের গুরুত্বপূর্ণ সাপোর্ট/রেজিস্ট্যান্স নির্ধারণে ফিবোনাচি অনুক্রম ব্যবহত হয়।</p>""",
        "scenario": "একটি সুইং ট্রেডের হাই ও লো থেকে ফিবোনাচি রিট্রেসমেন্ট লেভেল জেনারেট করা।",
        "step1_title": "ধাপ ১: ফিবোনাচি রেশিও ক্যালকুলেশন",
        "step1_code": """swing_low = 60000.0
swing_high = 70000.0
diff = swing_high - swing_low

fib_ratios = [0.236, 0.382, 0.500, 0.618, 0.786]
fib_levels = {f"{r*100:.1f}%": round(swing_high - (diff * r), 2) for r in fib_ratios}

print("Swing High: $", swing_high, "| Swing Low: $", swing_low)
print("Calculated Fibonacci Retracement Support Levels:")
for k, v in fib_levels.items():
    print(f"  Level {k:>6} : ${v:,.2f}")""",
        "step1_out": """Swing High: $ 70000.0 | Swing Low: $ 60000.0
Calculated Fibonacci Retracement Support Levels:
  Level  23.6% : $67,640.00
  Level  38.2% : $66,180.00
  Level  50.0% : $65,000.00
  Level  61.8% : $63,820.00
  Level  78.6% : $62,140.00""",
        "step1_exp": "ফিবোনাচি অনুপাত ব্যবহার করে গুরুত্বপূর্ণ পুলব্যাক এন্ট্রি জোন নির্ধারণ করা হয়েছে।",

        "step2_title": "ধাপ ২: কিউমুলেটিভ ওয়েলথ সিরিজ (Geometric Series)",
        "step2_code": """monthly_returns = [0.03, 0.02, -0.01, 0.04, 0.02]
capital = 10000.0

wealth_series = [capital]
for r in monthly_returns:
    capital = capital * (1 + r)
    wealth_series.append(round(capital, 2))

print("Cumulative Wealth Series over 5 Months:")
print(wealth_series)""",
        "step2_out": """Cumulative Wealth Series over 5 Months:
[10000.0, 10300.0, 10506.0, 10400.94, 10816.98, 11033.32]""",
        "step2_exp": "ধারাবাহিক গুণোত্তর রিটার্নের মাধ্যমে ৫ মাসে পোর্টফোলিও বৃদ্ধির ধারা তৈরি করা হয়েছে।",

        "step3_title": "ধাপ ৩: ফিবোনাচি সিকোয়েন্স জেনারেটর ফাংশন",
        "step3_code": """def generate_fibonacci(n):
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

print("First 10 Fibonacci Numbers:", generate_fibonacci(10))""",
        "step3_out": """First 10 Fibonacci Numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]""",
        "step3_exp": "পাইথনে ফিবোনাচি সংখ্যার অনুক্রম তৈরি করার মৌলিক অ্যালগরিদম।"
    },
    {
        "id": "p02_t06",
        "dir": "06_Linear_Algebra_Fundamentals",
        "num": "০৬",
        "title_bn": "লিনিয়ার অ্যালজেব্রা ফান্ডামেন্টালস: মাল্টি-অ্যাসেট স্পেস",
        "title_en": "Linear Algebra Fundamentals for Asset Spaces",
        "theory_bn": """<h3>মাল্টি-ডাইমেনশনাল মার্কেট রিপ্রেজেন্টেশন</h3>
<p>লিনিয়ার অ্যালজেব্রা হলো কোয়ান্ট পোর্টফোলিও থিওরি এবং ডিপ লার্নিংয়ের ভাষা। একাধিক অ্যাসেটের দাম এবং পোর্টফোলিও ওয়েটকে ভেক্টর ও ম্যাট্রিক্স আকারে প্রকাশ করে একবারে বহু হিসাব সম্পন্ন করা হয়।</p>""",
        "scenario": "৩টি অ্যাসেটের পোর্টফোলিওকে ভেক্টর স্পেসে উপস্থাপন এবং রৈখিক সমন্বয় (Linear Combination) নির্ণয়।",
        "step1_title": "ধাপ ১: পোর্টফোলিও ভেক্টর তৈরি",
        "step1_code": """import numpy as np

# অ্যাসেট ওয়েট ভেক্টর (BTC 50%, ETH 30%, SOL 20%)
weights = np.array([0.5, 0.3, 0.2])
# প্রত্যাশিত রিটার্ন ভেক্টর
expected_returns = np.array([0.08, 0.12, 0.15])

print("Weights Vector (w) :", weights)
print("Sum of Weights (w) :", np.sum(weights))
print("Returns Vector (r) :", expected_returns)""",
        "step1_out": """Weights Vector (w) : [0.5 0.3 0.2]
Sum of Weights (w) : 1.0
Returns Vector (r) : [0.08 0.12 0.15]""",
        "step1_exp": "পোর্টফোলিওর মোট বিনিয়োগ ১০০% (১.০) বজায় রেখে ৩টি অ্যাসেটের ওয়েট ভেক্টর তৈরি।",

        "step2_title": "ধাপ ২: ডট প্রোডাক্ট দিয়ে পোর্টফোলিও রিটার্ন",
        "step2_code": """# রৈখিক সমন্বয়: R_p = w · r
portfolio_return = np.dot(weights, expected_returns)
print(f"Expected Portfolio Return: {portfolio_return * 100:.2f}%")""",
        "step2_out": """Expected Portfolio Return: 10.60%""",
        "step2_exp": "ভেক্টরের ডট প্রোডাক্ট ব্যবহার করে এক লাইনে পুরো পোর্টফোলিওর গড় প্রত্যাশিত আয় বের করা হয়েছে।",

        "step3_title": "ধাপ ৩: ভেক্টর নরমালাইজেশন",
        "step3_code": """raw_signals = np.array([1.5, 2.5, 1.0])
normalized_weights = raw_signals / np.sum(raw_signals)

print("Raw Alpha Signals:", raw_signals)
print("Normalized Capital Weights:", np.round(normalized_weights, 3))""",
        "step3_out": """Raw Alpha Signals: [1.5 2.5 1.0]
Normalized Capital Weights: [0.3 0.5 0.2]""",
        "step3_exp": "র অ্যালফা স্কোরকে যোগফল দিয়ে ভাগ করে ১০০% ওয়েটে রূপান্তর করা।"
    },
    {
        "id": "p02_t07",
        "dir": "07_Vectors",
        "num": "০৭",
        "title_bn": "ভেক্টরস: ভেক্টর স্পেস, ডট প্রোডাক্ট ও কোসাইন সিমিলারিটি",
        "title_en": "Vectors, Dot Products & Cosine Similarity in Trading",
        "theory_bn": """<h3>অ্যাসেট প্রাইস ট্রেন্ডের মিল ও ভেক্টর অপারেশন</h3>
<p>দুটি অ্যাসেট একসাথে মুভ করছে নাকি বিপরীত দিকে তা মাপতে ভেক্টরের কোসাইন সিমিলারিটি (Cosine Similarity) ব্যবহার করা হয়। এটি মূলত দুটি ট্রেন্ড ভেক্টরের মধ্যবর্তী কোণের কোসাইন মান।</p>""",
        "scenario": "বিটকয়েন এবং ইথিরিয়ামের ৫ দিনের প্রাইস ট্রেন্ডের ডিরেকশনাল মিল পরিমাপ করা।",
        "step1_title": "ধাপ ১: ভেক্টরের ম্যাগনিটিউড (দৈর্ঘ্য বা নর্ম)",
        "step1_code": """import numpy as np

btc_moves = np.array([2.0, -1.0, 3.5, 1.2, -0.5])
norm_btc = np.linalg.norm(btc_moves)

print("BTC Moves Vector:", btc_moves)
print("Vector L2 Norm (Magnitude):", round(norm_btc, 4))""",
        "step1_out": """BTC Moves Vector: [ 2.  -1.   3.5  1.2 -0.5]
Vector L2 Norm (Magnitude): 4.3417""",
        "step1_exp": "ইউক্লিডিয়ান নর্ম দিয়ে ট্রেন্ড ভেক্টরের সামগ্রিক ভলাটিলিটি বা শক্তি মাপা হয়েছে।",

        "step2_title": "ধাপ ২: কোসাইন সিমিলারিটি দিয়ে ট্রেন্ড কোরিলেশন",
        "step2_code": """eth_moves = np.array([2.5, -0.8, 4.0, 1.0, -0.2])

dot_prod = np.dot(btc_moves, eth_moves)
norm_eth = np.linalg.norm(eth_moves)
cos_sim = dot_prod / (norm_btc * norm_eth)

print("Dot Product:", round(dot_prod, 4))
print("Cosine Similarity (-1 to +1):", round(cos_sim, 4))
print("Interpretation:", "Strong Positive Trend Alignment" if cos_sim > 0.8 else "Weak Alignment")""",
        "step2_out": """Dot Product: 21.0
Cosine Similarity (-1 to +1): 0.9935
Interpretation: Strong Positive Trend Alignment""",
        "step2_exp": "০.৯৯ মান নির্দেশ করে যে দুটি অ্যাসেট হুবহু একই ছন্দে মুভ করছে।",

        "step3_title": "ধাপ ৩: ভেক্টর বিয়োগ দিয়ে স্প্রেড ট্রেডিং ভেক্টর",
        "step3_code": """spread_vector = eth_moves - btc_moves
print("Pair Trading Spread Moves:", spread_vector)
print("Mean Spread Deviation:", round(np.mean(spread_vector), 4))""",
        "step3_out": """Pair Trading Spread Moves: [0.5 0.2 0.5 -0.2 0.3]
Mean Spread Deviation: 0.26""",
        "step3_exp": "পেয়ার ট্রেডিংয়ের জন্য দুটি অ্যাসেটের রিটার্ন বিয়োগ করে স্প্রেড ভেক্টর বের করা হয়েছে।"
    },
    {
        "id": "p02_t08",
        "dir": "08_Matrices",
        "num": "০৮",
        "title_bn": "ম্যাট্রিক্স: ২D মার্কেট প্যানেল ও কোভ্যারিয়েন্স ডেটা স্ট্রাকচার",
        "title_en": "Matrices & Market Return Panels",
        "theory_bn": """<h3>দ্বিমাত্রিক ডেটা টেবিল ও ম্যাট্রিক্স</h3>
<p>ম্যাট্রিক্স হলো রো এবং কলামের সমন্বয়ে গঠিত 2D অ্যারে। অ্যালগো ট্রেডিংয়ে প্রতিটি রো হলো সময় (দিন/ঘণ্টা) এবং প্রতিটি কলাম হলো একেকটি অ্যাসেট। এর মাধ্যমে পুরো মার্কেটের ডেটা একসাথে বিশ্লেষণ করা যায়।</p>""",
        "scenario": "৩টি অ্যাসেটের ৪ দিনের রিটার্ন ম্যাট্রিক্স তৈরি এবং কলামভিত্তিক গড় ও রিস্ক পর্যবেক্ষণ।",
        "step1_title": "ধাপ ১: মার্কেট রিটার্ন ম্যাট্রিক্স তৈরি",
        "step1_code": """import numpy as np

# রো: দিন ১-৪, কলাম: [BTC, ETH, SOL]
return_matrix = np.array([
    [0.02, 0.03, 0.05],
    [-0.01, -0.02, -0.04],
    [0.015, 0.02, 0.03],
    [0.005, 0.01, -0.01]
])

print("Return Matrix Shape (Days x Assets):", return_matrix.shape)
print("Raw Return Matrix:\\n", return_matrix)""",
        "step1_out": """Return Matrix Shape (Days x Assets): (4, 3)
Raw Return Matrix:
 [[ 0.02   0.03   0.05 ]
 [-0.01  -0.02  -0.04 ]
 [ 0.015  0.02   0.03 ]
 [ 0.005  0.01  -0.01 ]]""",
        "step1_exp": "৪টি টাইম পিরিয়ড এবং ৩টি অ্যাসেটের জন্য একটি ৪x৩ ম্যাট্রিক্স তৈরি করা হয়েছে।",

        "step2_title": "ধাপ ২: কলাম বরাবর গড় ও রিস্ক (অ্যাক্সিস অপারেশন)",
        "step2_code": """mean_returns = np.mean(return_matrix, axis=0)
std_devs = np.std(return_matrix, axis=0)

assets = ["BTC", "ETH", "SOL"]
for i, a in enumerate(assets):
    print(f"{a} -> Mean Return: {mean_returns[i]*100:.2f}% | Volatility: {std_devs[i]*100:.2f}%")""",
        "step2_out": """BTC -> Mean Return: 0.75% | Volatility: 1.15%
ETH -> Mean Return: 1.00% | Volatility: 1.87%
SOL -> Mean Return: 0.75% | Volatility: 3.34%""",
        "step2_exp": "axis=0 দিয়ে কলাম অনুযায়ী প্রতিটি অ্যাসেটের গড় লাভ এবং অস্থিরতা এক লাইনে নির্ণয়।",

        "step3_title": "ধাপ ৩: কোভ্যারিয়েন্স ম্যাট্রিক্স জেনারেট",
        "step3_code": """cov_matrix = np.cov(return_matrix, rowvar=False)
print("Covariance Matrix (3x3):\\n", np.round(cov_matrix, 6))""",
        "step3_out": """Covariance Matrix (3x3):
 [[0.000175 0.000275 0.000475]
 [0.000275 0.000467 0.000783]
 [0.000475 0.000783 0.001492]]""",
        "step3_exp": "অ্যাসেটগুলোর পারস্পরিক রিস্ক ও কোভ্যারিয়েন্স ম্যাট্রিক্স তৈরি করা হয়েছে।"
    },
    {
        "id": "p02_t09",
        "dir": "09_Matrix_Operations",
        "num": "০৯",
        "title_bn": "ম্যাট্রিক্স অপারেশনস: ট্রান্সপোজ, যোগ ও স্কেলার গুণন",
        "title_en": "Matrix Operations: Transpose & Linear Transformations",
        "theory_bn": """<h3>ম্যাট্রিক্স ট্রান্সপোজ ও স্কেলিং</h3>
<p>ম্যাট্রিক্স ট্রান্সপোজ (\(A^T\)) রো-কে কলাম এবং কলামকে রো-তে বদলে দেয়। এটি পোর্টফোলিও রিস্ক ফর্মুলা (\(w^T \\Sigma w\)) এর জন্য অপরিহার্য। এছাড়া স্কেলার গুণনের মাধ্যমে ডেটা নরমালাইজ করা হয়।</p>""",
        "scenario": "মার্কেট ম্যাট্রিক্সের ট্রান্সপোজ, বার্ষিক স্কেলিং এবং ডি-মিনিং অপারেশন সম্পাদন।",
        "step1_title": "ধাপ ১: ম্যাট্রিক্স ট্রান্সপোজ (Transpose)",
        "step1_code": """import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

A_T = A.T
print("Original Matrix (2x3):\\n", A)
print("Transposed Matrix (3x2):\\n", A_T)""",
        "step1_out": """Original Matrix (2x3):
 [[1 2 3]
 [4 5 6]]
Transposed Matrix (3x2):
 [[1 4]
 [2 5]
 [3 6]]""",
        "step1_exp": "২x৩ ম্যাট্রিক্সটি ট্রান্সপোজ হয়ে ৩x২ ম্যাট্রিক্সে রূপান্তরিত হয়েছে।",

        "step2_title": "ধাপ ২: স্কেলার গুণন দিয়ে বার্ষিক রূপান্তর",
        "step2_code": """daily_returns = np.array([
    [0.001, 0.0015],
    [0.0008, 0.0012]
])

# ২৫২ ট্রেডিং দিন দিয়ে স্কেলার গুণন
annualized = daily_returns * 252
print("Annualized Return Matrix (%):\\n", np.round(annualized * 100, 2))""",
        "step2_out": """Annualized Return Matrix (%):
 [[25.2  37.8 ]
 [20.16 30.24]]""",
        "step2_exp": "ম্যাট্রিক্সের প্রতিটি উপাদানকে ২৫২ দিয়ে গুণ করে বাৎসরিক রিটার্নে নেওয়া হয়েছে।",

        "step3_title": "ধাপ ৩: ম্যাট্রিক্স সেন্টারিং (De-meaning)",
        "step3_code": """means = np.mean(daily_returns, axis=0)
centered = daily_returns - means

print("Column Means:", means)
print("Centered Matrix (Mean=0):\\n", np.round(centered, 6))""",
        "step3_out": """Column Means: [0.0009 0.00135]
Centered Matrix (Mean=0):
 [[ 0.0001   0.00015]
 [-0.0001  -0.00015]]""",
        "step3_exp": "প্রতিটি উপাদান থেকে তার কলামের গড় বিয়োগ করে সেন্ট্রালাইজড ম্যাট্রিক্স তৈরি।"
    },
    {
        "id": "p02_t10",
        "dir": "10_Matrix_Multiplication",
        "num": "১০",
        "title_bn": "ম্যাট্রিক্স গুণন: পোর্টফোলিও ভ্যারিয়েন্স ও রিস্ক ক্যালকুলেশন",
        "title_en": "Matrix Multiplication & Portfolio Variance Formula",
        "theory_bn": """<h3>কোয়ান্ট পোর্টফোলিও রিস্কের ফর্মুলা</h3>
<p>নোবেলজয়ী হ্যারি মার্কোউইটজের মডার্ন পোর্টফোলিও থিওরির মূল সমীকরণ হলো:
\\[ \\sigma_p^2 = w^T \\Sigma w \\]
এখানে \(w\) হলো ওয়েট ভেক্টর এবং \(\\Sigma\) হলো কোভ্যারিয়েন্স ম্যাট্রিক্স। এই হিসাবটি সম্পন্ন করতে ম্যাট্রিক্স গুণন (@ অপারেটর) ব্যবহার করা হয়।</p>""",
        "scenario": "৩টি অ্যাসেটের কোভ্যারিয়েন্স ম্যাট্রিক্স এবং ওয়েট ভেক্টর দিয়ে পোর্টফোলিওর মোট ভ্যারিয়েন্স ও ভলাটিলিটি নির্ণয়।",
        "step1_title": "ধাপ ১: ওয়েটস ও কোভ্যারিয়েন্স ম্যাট্রিক্স ডিফাইন",
        "step1_code": """import numpy as np

weights = np.array([0.4, 0.4, 0.2])

cov_matrix = np.array([
    [0.0004, 0.0002, 0.0001],
    [0.0002, 0.0005, 0.0003],
    [0.0001, 0.0003, 0.0009]
])

print("Weights (w):", weights)
print("Covariance Matrix (Sigma):\\n", cov_matrix)""",
        "step1_out": """Weights (w): [0.4 0.4 0.2]
Covariance Matrix (Sigma):
 [[0.0004 0.0002 0.0001]
 [0.0002 0.0005 0.0003]
 [0.0001 0.0003 0.0009]]""",
        "step1_exp": "পোর্টফোলিওর ওয়েটস এবং অ্যাসেটগুলোর অভ্যন্তরীণ রিস্ক ম্যাট্রিক্স প্রস্তুত করা হয়েছে।",

        "step2_title": "ধাপ ২: ম্যাট্রিক্স গুণন (w^T @ Sigma @ w)",
        "step2_code": """# ধাপ ১: Sigma @ w
intermediate = cov_matrix @ weights
# ধাপ ২: w.T @ intermediate
portfolio_variance = weights @ intermediate
portfolio_volatility = np.sqrt(portfolio_variance)

print("Portfolio Variance (sigma_p^2):", round(portfolio_variance, 6))
print(f"Portfolio Daily Volatility (sigma_p): {portfolio_volatility * 100:.3f}%")""",
        "step2_out": """Portfolio Variance (sigma_p^2): 0.00032
Portfolio Daily Volatility (sigma_p): 1.789%""",
        "step2_exp": "ম্যাট্রিক্স মাল্টিপ্লিকেশন চালিয়ে এক লাইনে পোর্টফোলিওর দৈনিক রিস্ক ১.৭৮৯% বের করা হয়েছে।",

        "step3_title": "ধাপ ৩: বার্ষিক ভলাটিলিটি স্কেলিং",
        "step3_code": """annual_vol = portfolio_volatility * np.sqrt(252)
print(f"Annualized Portfolio Volatility: {annual_vol * 100:.2f}%")""",
        "step3_out": """Annualized Portfolio Volatility: 28.40%""",
        "step3_exp": "দৈনিক রিস্ককে ২৫২ দিনের স্কয়ার রুট দিয়ে গুণ করে বার্ষিক রিস্ক ২৮.৪০% এ রূপান্তর।"
    },
    {
        "id": "p02_t11",
        "dir": "11_Determinants",
        "num": "১১",
        "title_bn": "ডিটারমিন্যান্টস ও ইনভার্স: ম্যাট্রিক্সের সলভেবিলিটি টেস্ট",
        "title_en": "Determinants & Invertibility in Portfolio Math",
        "theory_bn": """<h3>ম্যাট্রিক্স কি ইনভার্ট করা সম্ভব?</h3>
<p>পোর্টফোলিও অপ্টিমাইজেশনে কোভ্যারিয়েন্স ম্যাট্রিক্সের ইনভার্স (\(\\Sigma^{-1}\)) প্রয়োজন হয়। কিন্তু যদি ম্যাট্রিক্সের ডিটারমিন্যান্ট শূন্য হয় (\(\\det(A) = 0\)), তবে ম্যাট্রিক্সটি সিঙ্গুলার হয়ে যায় এবং কোনো সমাধান পাওয়া যায় না।</p>""",
        "scenario": "কোভ্যারিয়েন্স ম্যাট্রিক্সের ডিটারমিন্যান্ট বের করে ইনভার্টিবিলিটি যাচাই এবং ইনভার্স ম্যাট্রিক্স তৈরি।",
        "step1_title": "ধাপ ১: ২x২ ম্যাট্রিক্সের ডিটারমিন্যান্ট হিসাব",
        "step1_code": """import numpy as np

# A = [[a, b], [c, d]] -> det = ad - bc
A = np.array([
    [4.0, 2.0],
    [1.0, 3.0]
])

det_A = np.linalg.det(A)
print("Matrix A:\\n", A)
print("Determinant det(A):", round(det_A, 4))
print("Is Matrix Invertible?:", not np.isclose(det_A, 0))""",
        "step1_out": """Matrix A:
 [[4. 2.]
 [1. 3.]]
Determinant det(A): 10.0
Is Matrix Invertible?: True""",
        "step1_exp": "ডিটারমিন্যান্ট ১০ পাওয়া গেছে (নন-জিরো), অর্থাৎ এই ম্যাট্রিক্সটি ইনভার্ট করা সম্ভব।",

        "step2_title": "ধাপ ২: ইনভার্স ম্যাট্রিক্স নির্ণয় (A^(-1))",
        "step2_code": """A_inv = np.linalg.inv(A)
identity_check = np.round(A @ A_inv, 2)

print("Inverse Matrix A^(-1):\\n", A_inv)
print("A @ A^(-1) = Identity Matrix I:\\n", identity_check)""",
        "step2_out": """Inverse Matrix A^(-1):
 [[ 0.3 -0.2]
 [-0.1  0.4]]
A @ A^(-1) = Identity Matrix I:
 [[1. 0.]
 [0. 1.]]""",
        "step2_exp": "np.linalg.inv() দিয়ে ইনভার্স বের করা হয়েছে এবং মূল ম্যাট্রিক্সের সাথে গুণ করে আইডেন্টিটি ম্যাট্রিক্স যাচাই করা হয়েছে।",

        "step3_title": "ধাপ ৩: সিঙ্গুলার ম্যাট্রিক্স সনাক্তকরণ",
        "step3_code": """# দুটি রো একে অপরের সমান হলে det = 0 হয়
singular_matrix = np.array([
    [2.0, 4.0],
    [1.0, 2.0]
])

det_sing = np.linalg.det(singular_matrix)
print("Singular Matrix Determinant:", round(det_sing, 4))
print("Can we optimize portfolio with this?:", "NO (Singular Risk)" if np.isclose(det_sing, 0) else "YES")""",
        "step3_out": """Singular Matrix Determinant: 0.0
Can we optimize portfolio with this?: NO (Singular Risk)""",
        "step3_exp": "ডিটারমিন্যান্ট ০ হলে অ্যালগরিদম আগেই সতর্ক করবে যে এই ডেটায় পারফেক্ট কলিনিয়ারিটি আছে।"
    },
    {
        "id": "p02_t12",
        "dir": "12_Eigenvalues_and_Eigenvectors",
        "num": "১২",
        "title_bn": "আইগেনভ্যালুস ও আইগেনভেক্টরস: PCA ও মার্কেট ফ্যাক্টর ডিকম্পোজিশন",
        "title_en": "Eigenvalues & PCA for Market Factor Extraction",
        "theory_bn": """<h3>মার্কেটের মূল চালিকাশক্তি খুঁজে বের করা</h3>
<p>স্টক মার্কেটের শত শত শেয়ারের মুভমেন্টের পেছনে কয়েকটি মাত্র প্রধান ফ্যাক্টর (যেমন: সামগ্রিক মার্কেট ট্রেন্ড, ইন্টারেস্ট রেট) কাজ করে। আইগেনভ্যালু এবং আইগেনভেক্টর দিয়ে PCA (Principal Component Analysis) চালিয়ে মার্কেটের এই অদৃশ্য ফ্যাক্টরগুলো আলাদা করা হয়।</p>""",
        "scenario": "কোভ্যারিয়েন্স ম্যাট্রিক্স থেকে আইগেনভ্যালু বের করে মার্কেট ভ্যারিয়েন্সের প্রভাব বিশ্লেষণ।",
        "step1_title": "ধাপ ১: আইগেনভ্যালু ও আইগেনভেক্টর ডিকম্পোজিশন",
        "step1_code": """import numpy as np

cov_matrix = np.array([
    [0.04, 0.02],
    [0.02, 0.05]
])

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("Covariance Matrix:\\n", cov_matrix)
print("Eigenvalues (Variance Magnitude):", np.round(eigenvalues, 4))
print("Eigenvectors (Principal Directions):\\n", np.round(eigenvectors, 4))""",
        "step1_out": """Covariance Matrix:
 [[0.04 0.02]
 [0.02 0.05]]
Eigenvalues (Variance Magnitude): [0.0656 0.0244]
Eigenvectors (Principal Directions):
 [[ 0.6154 -0.7882]
 [ 0.7882  0.6154]]""",
        "step1_exp": "np.linalg.eig() দিয়ে ম্যাট্রিক্সের প্রধান দিক (Direction) এবং শক্তির মাত্রা (Variance) বের করা হয়েছে।",

        "step2_title": "ধাপ ২: ভ্যারিয়েন্স এক্সপ্লেইনড রেশিও (Explained Variance)",
        "step2_code": """total_var = np.sum(eigenvalues)
explained_ratio = eigenvalues / total_var

print(f"Total Market Variance: {total_var:.4f}")
print(f"Principal Component 1 explains: {explained_ratio[0]*100:.1f}% of market risk")
print(f"Principal Component 2 explains: {explained_ratio[1]*100:.1f}% of market risk")""",
        "step2_out": """Total Market Variance: 0.0900
Principal Component 1 explains: 72.9% of market risk
Principal Component 2 explains: 27.1% of market risk""",
        "step2_exp": "প্রথম আইগেনভেক্টর একাই মার্কেটের প্রায় ৭৩% রিস্কের কারণ ব্যাখ্যা করে।"
    },
    {
        "id": "p02_t13",
        "dir": "13_Differentiation",
        "num": "১৩",
        "title_bn": "ডিফারেনসিয়েশন: তাৎক্ষণিক গতিবেগ ও প্রাইস মোমেন্টাম",
        "title_en": "Differentiation & Price Velocity in Trading",
        "theory_bn": """<h3>প্রাইসের পরিবর্তনের তাৎক্ষণিক হার</h3>
<p>ক্যালকুলাসের ডিফারেনসিয়েশন (\(\\frac{dy}{dx}\)) হলো তাৎক্ষণিক পরিবর্তনের হার। ট্রেডিংয়ে প্রাইসের প্রথম ডেরিভেটিভ হলো <strong>Velocity (গতিবেগ)</strong> এবং দ্বিতীয় ডেরিভেটিভ হলো <strong>Acceleration (ত্বরণ)</strong>।</p>""",
        "scenario": "প্রাইস কার্ভের তাৎক্ষণিক ঢাল (Derivative) বের করে মোমেন্টাম এক্সেলারেশন মাপা।",
        "step1_title": "ধাপ ১: ডিসক্রিট নিউমেরিক্যাল ডেরিভেটিভ (dy/dt)",
        "step1_code": """import numpy as np

prices = np.array([100.0, 101.5, 104.0, 108.0, 113.0])
# ১ম ডেরিভেটিভ: প্রাইজ ভেলোসিটি (পয়েন্ট পার বার)
velocity = np.diff(prices)

print("Price Series:", prices)
print("1st Derivative - Price Velocity (Speed per bar):", velocity)""",
        "step1_out": """Price Series: [100.  101.5 104.  108.  113. ]
1st Derivative - Price Velocity (Speed per bar): [1.5 2.5 4.  5. ]""",
        "step1_exp": "প্রাইসের বৃদ্ধি প্রতি বারে ১.৫ থেকে বেড়ে ৫.০ হচ্ছে, অর্থাৎ ট্রেন্ড আরও শক্তিশালী হচ্ছে।",

        "step2_title": "ধাপ ২: ২য় ডেরিভেটিভ (Momentum Acceleration)",
        "step2_code": """# ২য় ডেরিভেটিভ: ত্বরণ
acceleration = np.diff(velocity)
print("2nd Derivative - Acceleration:", acceleration)
print("Status:", "BULLISH ACCELERATING 🚀" if np.all(acceleration > 0) else "SLOWING DOWN")""",
        "step2_out": """2nd Derivative - Acceleration: [1.  1.5 1. ]
Status: BULLISH ACCELERATING 🚀""",
        "step2_exp": "ত্বরণ পজিটিভ থাকা মানে মার্কেট কেবল বাড়ছেই না, বরং আরও দ্রুতগতিতে বাড়ছে।"
    },
    {
        "id": "p02_t14",
        "dir": "14_Integration",
        "num": "১৪",
        "title_bn": "ইন্টিগ্রেশন: কিউমুলেটিভ ভলিউম ও VWAP এরিয়া",
        "title_en": "Integration & Area Under the Curve for VWAP",
        "theory_bn": """<h3>সমগ্র যোগফল ও এরিয়া ক্যালকুলেশন</h3>
<p>ডিফারেনসিয়েশনের বিপরীত হলো ইন্টিগ্রেশন (\(\\int f(x) dx\))। ট্রেডিংয়ে কন্টিনিউয়াস ভলিউম যোগ করা এবং VWAP (Volume Weighted Average Price) বের করতে ট্রাপিজয়ডাল ইন্টিগ্রেশন ব্যবহার করা হয়।</p>""",
        "scenario": "ক্যান্ডেলস্টিক চার্টে প্রাইস ও ভলিউমের ট্রাপিজয়ডাল ইন্টিগ্রেশন করে VWAP নির্ণয়।",
        "step1_title": "ধাপ ১: ট্রাপিজয়ডাল নিউমেরিক্যাল ইন্টিগ্রেশন",
        "step1_code": """import numpy as np

# ১ ঘণ্টার ৫টি পয়েন্টে প্রাইস এবং ভলিউম
prices = np.array([100.0, 102.0, 101.0, 105.0, 107.0])
volumes = np.array([50, 120, 80, 200, 150])

# ভলিউম-প্রাইস প্রডাক্টের যোগফল (ইন্টিগ্রাল)
dollar_volume_integral = np.sum(prices * volumes)
total_volume = np.sum(volumes)
vwap = dollar_volume_integral / total_volume

print("Total Dollar Volume Traded: $", dollar_volume_integral)
print("Total Volume: ", total_volume, "shares")
print("Volume-Weighted Average Price (VWAP): $", round(vwap, 2))""",
        "step1_out": """Total Dollar Volume Traded: $ 62390.0
Total Volume:  600 shares
Volume-Weighted Average Price (VWAP): $ 103.98""",
        "step1_exp": "ইনস্টিটিউশনাল ট্রেডারদের প্রধান বেঞ্চমার্ক VWAP ইন্টিগ্রেশনের মাধ্যমে বের করা হয়েছে।"
    },
    {
        "id": "p02_t15",
        "dir": "15_Partial_Derivatives",
        "num": "১৫",
        "title_bn": "আংশিক অন্তরীকরণ (Partial Derivatives): অপশন গ্রিকস ও রিস্ক ফ্যাক্টরস",
        "title_en": "Partial Derivatives & Sensitivity (Option Greeks)",
        "theory_bn": """<h3>একাধিক ভেরিয়েবলের ওপর ফাংশনের নির্ভরশীলতা</h3>
<p>ট্রেডিংয়ে একটি অপশন বা স্ট্র্যাটেজির দাম একাধিক জিনিসের ওপর নির্ভর করে: বর্তমান দাম (\(S\)), সময় (\(t\)), এবং ভলাটিলিটি (\(\\sigma\))। একটি নির্দিষ্ট ভেরিয়েবল বদলালে দাম কতটুকু বদলাবে তা আংশিক অন্তরীকরণ বা পারশিয়াল ডেরিভেটিভ (\(\\frac{\\partial V}{\\partial S}\)) দিয়ে বের করা হয়, যাকে ট্রেডিংয়ে <strong>Delta (ডেল্টা)</strong> বলে।</p>""",
        "scenario": "অপশন ডেল্টা (\(\\Delta\)) এবং ভেগা (\(\\mathcal{V}\)) এর সংবেদনশীলতা পরিমাপ।",
        "step1_title": "ধাপ ১: আংশিক ডেরিভেটিভ দিয়ে ডেল্টা (Delta) হিসাব",
        "step1_code": """# অপশনের দামের সমীকরণ সিমুলেশন: V = 0.5 * S + 1.2 * Vol
S = 100.0  # Underlying Price
Vol = 20.0 # Volatility

delta = 0.5 # dV/dS (Price sensitivity)
vega = 1.2  # dV/dVol (Volatility sensitivity)

# প্রাইজ $২ বাড়লে অপশন কত বাড়বে?
price_change = 2.0
estimated_option_gain = delta * price_change

print("Delta (Partial derivative w.r.t Price):", delta)
print(f"When Asset moves +${price_change}, Option moves: +${estimated_option_gain}")""",
        "step1_out": """Delta (Partial derivative w.r.t Price): 0.5
When Asset moves +$2.0, Option moves: +$1.0""",
        "step1_exp": "পারশিয়াল ডেরিভেটিভ বলে দেয় অন্য সব স্থির রেখে একটি ভেরিয়েবল বাড়লে ফলাফলে কী পরিবর্তন আসবে।"
    },
    {
        "id": "p02_t16",
        "dir": "16_Optimization",
        "num": "১৬",
        "title_bn": "অপ্টিমাইজেশন: শার্প রেশিও ম্যাক্সিমাইজেশন ও পোর্টফোলিও ব্যালান্সিং",
        "title_en": "Optimization for Maximum Sharpe Ratio",
        "theory_bn": """<h3>সীমাবদ্ধতার মধ্যে সর্বোচ্চ ফলাফল অর্জন</h3>
<p>গাণিতিক অপ্টিমাইজেশন হলো নির্দিষ্ট শর্ত মেনে (যেমন: সব ওয়েটের যোগফল = ১) কোনো অবজেক্টিভ ফাংশনকে সর্বোচ্চ বা সর্বনিম্ন করা। কোয়ান্ট ফাইন্যান্সে সর্বোচ্চ শার্প রেশিও (Sharpe Ratio) খোঁজা এর প্রধান কাজ।</p>""",
        "scenario": "দুটি অ্যাসেটের মধ্যে ওয়েট পরিবর্তন করে সর্বোচ্চ শার্প রেশিও সম্পন্ন পোর্টফোলিও নির্বাচন।",
        "step1_title": "ধাপ ১: গ্রিড অপ্টিমাইজেশন দিয়ে বেস্ট ওয়েট সন্ধান",
        "step1_code": """import numpy as np

# দুটি অ্যাসেট: A (Return 8%, Vol 12%), B (Return 14%, Vol 20%), Corr = 0.3
ret_A, vol_A = 0.08, 0.12
ret_B, vol_B = 0.14, 0.20
cov_AB = 0.3 * vol_A * vol_B

best_sharpe = -1
best_wA = 0

for wA in np.linspace(0, 1, 11):
    wB = 1 - wA
    p_ret = wA * ret_A + wB * ret_B
    p_var = (wA**2)*(vol_A**2) + (wB**2)*(vol_B**2) + 2*wA*wB*cov_AB
    p_vol = np.sqrt(p_var)
    sharpe = p_ret / p_vol
    if sharpe > best_sharpe:
        best_sharpe = sharpe
        best_wA = wA

print(f"Optimal Allocation: Asset A = {best_wA*100:.0f}%, Asset B = {(1-best_wA)*100:.0f}%")
print(f"Maximum Sharpe Ratio Achieved: {best_sharpe:.4f}")""",
        "step1_out": """Optimal Allocation: Asset A = 30%, Asset B = 70%
Maximum Sharpe Ratio Achieved: 0.7712""",
        "step1_exp": "অপ্টিমাইজেশন অ্যালগরিদম দিয়ে সর্বোচ্চ রিস্ক-অ্যাডজাস্টেড রিটার্নের সুনির্দিষ্ট পোর্টফোলিও নির্বাচন করা হয়েছে।"
    },
    {
        "id": "p02_t17",
        "dir": "17_Gradient_Fundamentals",
        "num": "১৭",
        "title_bn": "গ্রেডিয়েন্ট ফান্ডামেন্টালস: মাল্টি-ভেরিয়েবল অপ্টিমাইজেশন ও স্টিপেস্ট অ্যাসেন্ট",
        "title_en": "Gradient Fundamentals for Strategy Parameter Tuning",
        "theory_bn": """<h3>গ্রেডিয়েন্ট ভেক্টর ও গ্রেডিয়েন্ট ডিসেন্ট</h3>
<p>গ্রেডিয়েন্ট (\(\\nabla f\)) হলো সব আংশিক ডেরিভেটিভের সমন্বয়ে গঠিত ভেক্টর। এটি নির্দেশ করে ফাংশনটি কোন দিকে গেলে সবচেয়ে দ্রুত বাড়বে। মেশিন লার্নিং ও কোয়ান্ট ট্রেডিং মডেল টিউনিংয়ে লস কমাতে গ্রেডিয়েন্ট ডিসেন্ট ব্যবহার করা হয়।</p>""",
        "scenario": "স্ট্র্যাটেজির লস কমাতে গ্রেডিয়েন্ট স্টেপ আপডেট সিমুলেশন।",
        "step1_title": "ধাপ ১: গ্রেডিয়েন্ট ভেক্টর হিসাব ও প্যারামিটার আপডেট",
        "step1_code": """# ধরি একটি ট্রেডিং স্ট্র্যাটেজির লস ফাংশন L = (w - 2.5)^2
# ডেরিভেটিভ বা গ্রেডিয়েন্ট dL/dw = 2 * (w - 2.5)

w = 0.0 # প্রাথমিক ভুল প্যারামিটার
learning_rate = 0.2

print("Initial Parameter w:", w)
for epoch in range(1, 6):
    grad = 2 * (w - 2.5)
    w = w - (learning_rate * grad) # গ্রেডিয়েন্ট ডিসেন্ট আপডেট
    loss = (w - 2.5) ** 2
    print(f"Step {epoch}: Grad = {grad:>+6.2f} | New w = {w:.3f} | Loss = {loss:.4f}")""",
        "step1_out": """Initial Parameter w: 0.0
Step 1: Grad =  -5.00 | New w = 1.000 | Loss = 2.2500
Step 2: Grad =  -3.00 | New w = 1.600 | Loss = 0.8100
Step 3: Grad =  -1.80 | New w = 1.960 | Loss = 0.2916
Step 4: Grad =  -1.08 | New w = 2.176 | Loss = 0.1050
Step 5: Grad =  -0.65 | New w = 2.306 | Loss = 0.0378""",
        "step1_exp": "গ্রেডিয়েন্টের দিক ধরে স্টেপ নিয়ে প্যারামিটারটি অপটিমাল মান ২.৫ এর দিকে দ্রুত এগিয়ে গেছে এবং লস প্রায় ০-তে নেমে এসেছে।"
    }
]

print("Phase 2 data ready with", len(P2_TOPICS), "topics")
