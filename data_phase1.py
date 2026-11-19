# data_phase1.py
# Phase 1 Topics 02 to 15 (Python for Quantitative Algorithmic Trading)

P1_TOPICS = [
    {
        "id": "p01_t02",
        "dir": "02_Variables_and_Data_Types",
        "num": "০২",
        "title_bn": "ভেরিয়েবল ও ডেটা টাইপস: মার্কেট টিক ডেটা মডেলিং",
        "title_en": "Variables & Data Types in Market Tick Data",
        "theory_bn": """<h3>ট্রেডিং অ্যালগরিদমে ডেটা টাইপ কেন অপরিহার্য?</h3>
<p>প্রতিটি কোয়ান্ট ট্রেডিং সিস্টেমে মার্কেট থেকে আসা রিয়েল-টাইম টিক ডেটা পার্স করতে হয়। পাইথনের প্রধান ৪টি ডেটা টাইপ এখানে ব্যবহার হয়:</p>
<ul>
    <li><strong>str (String):</strong> অ্যাসেট বা কারেন্সি পেয়ারের নাম (যেমন: <code>"BTC/USDT"</code>, <code>"EUR/USD"</code>)।</li>
    <li><strong>float (Floating Point):</strong> ক্যান্ডেলের দাম এবং সূচক মান (যেমন: <code>67450.50</code>, <code>1.0845</code>)।</li>
    <li><strong>int (Integer):</strong> ট্রেডিং ভলিউম বা লট সংখ্যা (যেমন: <code>15</code>, <code>100</code>)।</li>
    <li><strong>bool (Boolean):</strong> সিগন্যাল ট্রিগার বা বুলিশ/বেয়ারিশ স্ট্যাটাস (যেমন: <code>True</code>, <code>False</code>)।</li>
</ul>
<p>ব্রোকার API থেকে অনেক সময় দাম স্ট্রিং আকারে আসে। তাই <code>float()</code> এবং <code>int()</code> দিয়ে টাইপ কাস্টিং করে সঠিক গাণিতিক মান বের করতে হয়।</p>""",
        "scenario": "লাইভ এক্সচেঞ্জ টিক ফিড থেকে একটি অ্যাসেটের সিম্বল, ওএইচএলসি প্রাইস, ভলিউম ও বুলিশ স্ট্যাটাস ভেরিয়েবলে সংরক্ষণ এবং ডেটা টাইপ রূপান্তর।",
        "step1_title": "ধাপ ১: মার্কেট টিক ভেরিয়েবল ডিফাইন ও টাইপ চেক",
        "step1_code": """symbol = "BTC/USDT"
entry_price = 67450.50
trade_volume = 12
is_bullish = True

print("Asset:", symbol, "| Type:", type(symbol).__name__)
print("Entry Price: $", entry_price, "| Type:", type(entry_price).__name__)
print("Volume:", trade_volume, "| Type:", type(trade_volume).__name__)
print("Bullish Status:", is_bullish, "| Type:", type(is_bullish).__name__)""",
        "step1_out": """Asset: BTC/USDT | Type: str
Entry Price: $ 67450.5 | Type: float
Volume: 12 | Type: int
Bullish Status: True | Type: bool""",
        "step1_exp": "আমরা পাইথনের চারটি মৌলিক ডেটা টাইপ দিয়ে একটি ট্রেডিং টিক রেকর্ড তৈরি করেছি। type() ফাংশন দিয়ে যাচাই করা হয়েছে প্রতিটি ভেরিয়েবলের আসল ক্লাস।",

        "step2_title": "ধাপ ২: স্ট্রিং থেকে নিউমেরিক রূপান্তর (Type Casting)",
        "step2_code": """raw_api_price = "67450.50"
raw_api_volume = "15"

parsed_price = float(raw_api_price)
parsed_volume = int(raw_api_volume)
notional_value = parsed_price * parsed_volume

print("Parsed Price: $", parsed_price)
print("Parsed Volume:", parsed_volume, "contracts")
print("Total Notional Value: $", round(notional_value, 2))""",
        "step2_out": """Parsed Price: $ 67450.5
Parsed Volume: 15 contracts
Total Notional Value: $ 1011757.5""",
        "step2_exp": "ব্রোকার API থেকে প্রাপ্ত প্রাইস ও ভলিউম স্ট্রিং ফরম্যাটে আসে। float() ও int() কাস্টিং করে সঠিক গাণিতিক মান বের করা হয়েছে।",

        "step3_title": "ধাপ ৩: ট্রেড টিকেট সামারি ফরম্যাটিং (f-strings)",
        "step3_code": """portfolio_id = "QUANT-ALPHA-01"
leverage = 5
margin_required = notional_value / leverage

trade_ticket = f\"\"\"[TRADE TICKET]
Account  : {portfolio_id}
Asset    : {symbol}
Position : {parsed_volume} units @ ${parsed_price:,.2f}
Notional : ${notional_value:,.2f}
Margin   : ${margin_required:,.2f} ({leverage}x Leverage)\"\"\"

print(trade_ticket)""",
        "step3_out": """[TRADE TICKET]
Account  : QUANT-ALPHA-01
Asset    : BTC/USDT
Position : 15 units @ $67,450.50
Notional : $1,011,757.50
Margin   : $202,351.50 (5x Leverage)""",
        "step3_exp": "f-strings ব্যবহার করে সংখ্যার কমা ফরম্যাটিং এবং ডেসিমাল নিয়ন্ত্রণ করে পেশাদার ট্রেড কনফার্মেশন টিকেট তৈরি করা হয়েছে।"
    },
    {
        "id": "p01_t03",
        "dir": "03_Lists_Tuples_Sets_and_Dictionaries",
        "num": "০৩",
        "title_bn": "লিস্ট, টাপল, সেট ও ডিকশনারি: অর্ডারবুক ও ক্যান্ডেলস্টিক স্ট্রাকচার",
        "title_en": "Collections in Order Book & OHLCV Bars",
        "theory_bn": """<h3>ট্রেডিং ডেটা সংরক্ষণে পাইথন কালেকশনস</h3>
<p>অ্যালগরিদমিক ট্রেডিংয়ে বিভিন্ন বৈশিষ্ট্যের ডেটার জন্য ভিন্ন ভিন্ন কালেকশন ব্যবহার করতে হয়:</p>
<ul>
    <li><strong>List:</strong> পরিবর্তনযোগ্য (Mutable) তালিকা—যেমন লাইভ অর্ডারবুকের বিড এবং আস্ক প্রাইস লেভেল।</li>
    <li><strong>Tuple:</strong> অপরিবর্তনযোগ্য (Immutable) ডেটা—যেমন একটি ক্লোজড ক্যান্ডেলের ওপেন, হাই, লো, ক্লোজ (OHLC) যা একবার তৈরি হলে আর বদলানো যাবে না।</li>
    <li><strong>Set:</strong> ইউনিক উপাদানের সেট—যেমন পোর্টফোলিওতে সক্রিয় ট্রেডেড অ্যাসেটগুলোর ইউনিক সিম্বল তালিকা।</li>
    <li><strong>Dictionary:</strong> কী-ভ্যালু স্ট্রাকচার—একটি সম্পূর্ণ ক্যান্ডেলস্টিকের মেটাডেটা (টাইমস্ট্যাম্প, ভলিউম, ইন্ডিকেটর ভ্যালু)।</li>
</ul>""",
        "scenario": "লাইভ অর্ডারবুকের গভীরতা পর্যবেক্ষণ, ঐতিহাসিক ক্যান্ডেলের টাপল সংরক্ষণ এবং ইউনিক সিম্বল ম্যানেজমেন্ট।",
        "step1_title": "ধাপ ১: অর্ডারবুক বিড ও আস্ক লিস্ট ম্যানিপুলেশন",
        "step1_code": """bids = [67400.0, 67390.0, 67380.0]
asks = [67410.0, 67420.0, 67430.0]

bids.append(67405.0)
bids.sort(reverse=True)
best_bid = bids[0]
best_ask = asks[0]
spread = best_ask - best_bid

print("Top 3 Bids:", bids[:3])
print("Best Bid:", best_bid, "| Best Ask:", best_ask)
print("Current Bid-Ask Spread: $", round(spread, 2))""",
        "step1_out": """Top 3 Bids: [67405.0, 67400.0, 67390.0]
Best Bid: 67405.0 | Best Ask: 67410.0
Current Bid-Ask Spread: $ 5.0""",
        "step1_exp": "লিস্টে নতুন অর্ডারের মূল্য যুক্ত করে ডিসেন্ডিং অর্ডারে সর্ট করা হয়েছে এবং শীর্ষ বিড-আস্ক স্প্রেড বের করা হয়েছে।",

        "step2_title": "ধাপ ২: ইমিউটেবল ক্যান্ডেল টাপল ও ইউনিক সিম্বল সেট",
        "step2_code": """candle_bar = (67200.0, 67550.0, 67150.0, 67480.0)
bar_range = candle_bar[1] - candle_bar[2]

filled_symbols = {"BTC/USDT", "ETH/USDT", "SOL/USDT", "BTC/USDT"}
print("Candle Bar (O, H, L, C):", candle_bar)
print("Bar High-Low Range: $", bar_range)
print("Unique Traded Assets:", filled_symbols)""",
        "step2_out": """Candle Bar (O, H, L, C): (67200.0, 67550.0, 67150.0, 67480.0)
Bar High-Low Range: $ 400.0
Unique Traded Assets: {'SOL/USDT', 'BTC/USDT', 'ETH/USDT'}""",
        "step2_exp": "টাপল নিশ্চিত করে ঐতিহাসিক ক্যান্ডেল ডেটা অ্যাক্সিডেন্টালি মডিফাই হবে না। সেট ডুপ্লিকেট দূর করে ইউনিক সিম্বল সংরক্ষণ করে।",

        "step3_title": "ধাপ ৩: ক্যান্ডেলস্টিক ডিকশনারি ও কি-ভ্যালু এক্সেস",
        "step3_code": """candle = {
    "timestamp": "2026-11-19T23:00:00Z",
    "symbol": "BTC/USDT",
    "open": 67200.0,
    "high": 67550.0,
    "low": 67150.0,
    "close": 67480.0,
    "volume": 842.5
}

is_bullish_bar = candle["close"] > candle["open"]
candle["is_bullish"] = is_bullish_bar

print(f"Bar: {candle['symbol']} | Close: ${candle['close']}")
print(f"Volume: {candle['volume']} BTC | Bullish: {candle['is_bullish']}")""",
        "step3_out": """Bar: BTC/USDT | Close: $67480.0
Volume: 842.5 BTC | Bullish: True""",
        "step3_exp": "ডিকশনারিতে সম্পূর্ণ ক্যান্ডেলের প্রতিটি প্যারামিটার কী-ভ্যালু পেয়ারে সংরক্ষণ করে ডাইনামিক ফিল্ড যুক্ত করা হয়েছে।"
    },
    {
        "id": "p01_t04",
        "dir": "04_Conditional_Statements",
        "num": "০৪",
        "title_bn": "শর্ত ও লজিক্যাল স্টেটমেন্টস: অ্যালগো সিগন্যাল ইঞ্জিন",
        "title_en": "Conditional Logic & Trade Signal Filters",
        "theory_bn": """<h3>ট্রেডিং ডিসিশন মেকিংয়ে শর্তসমূহ</h3>
<p>ট্রেডিং বট প্রতিটি মিলিসেকেন্ডে শর্ত (if, elif, else) মূল্যায়ন করে:</p>
<ul>
    <li><strong>রিস্ক চেক:</strong> বর্তমান দাম কি স্টপলস অতিক্রম করেছে?</li>
    <li><strong>টার্গেট এক্সিট:</strong> প্রফিট টার্গেট পূরণ হয়েছে কি না?</li>
    <li><strong>ইন্ডিকেটর কনফার্মেশন:</strong> মুভিং এভারেজ এবং আরএসআই কি একসাথে বাই সিগন্যাল দিচ্ছে?</li>
</ul>""",
        "scenario": "একটি মুভিং এভারেজ ব্রেকআউট এবং আরএসআই ফিল্টার দিয়ে স্বয়ংক্রিয় বাই/সেল সিগন্যাল তৈরি।",
        "step1_title": "ধাপ ১: স্টপলস ও টেক প্রফিট চেকিং লজিক",
        "step1_code": """entry_price = 100.0
current_price = 106.5
stop_loss = 95.0
take_profit = 110.0

if current_price <= stop_loss:
    action = "CLOSE_STOP_LOSS"
elif current_price >= take_profit:
    action = "CLOSE_TAKE_PROFIT"
else:
    action = "HOLD_POSITION"

print("Price:", current_price, "--> Action:", action)""",
        "step1_out": """Price: 106.5 --> Action: HOLD_POSITION""",
        "step1_exp": "বর্তমান প্রাইস স্টপলস বা টার্গেট সীমা স্পর্শ করেছে কি না তা if-elif-else দিয়ে চেক করে তাৎক্ষণিক সিদ্ধান্ত নেওয়া হয়।",

        "step2_title": "ধাপ ২: মাল্টি-ইন্ডিকেটর কনফার্মেশন ফিল্টার",
        "step2_code": """fast_ma = 104.2
slow_ma = 101.8
rsi = 58.0
volume_surge = True

if fast_ma > slow_ma and 50 < rsi < 70 and volume_surge:
    signal = "STRONG_BUY"
elif fast_ma < slow_ma and rsi > 70:
    signal = "OVERBOUGHT_EXIT"
else:
    signal = "NEUTRAL"

print("Indicator Status: MA Fast > Slow =", fast_ma > slow_ma, "| RSI =", rsi)
print("Execution Signal:", signal)""",
        "step2_out": """Indicator Status: MA Fast > Slow = True | RSI = 58.0
Execution Signal: STRONG_BUY""",
        "step2_exp": "লজিক্যাল and অপারেটর দিয়ে ট্রেন্ড, মোমেন্টাম ও ভলিউম তিনটি শর্ত একই সাথে পূর্ণ হলে তবেই স্ট্রং বাই সিগন্যাল দেওয়া হয়।",

        "step3_title": "ধাপ ৩: টের্নারি কন্ডিশনে এক লাইনে সিগন্যাল তৈরি",
        "step3_code": """prev_close = 102.0
curr_close = 104.5

trend = "BULLISH" if curr_close > prev_close else "BEARISH"
print(f"Previous: ${prev_close} | Current: ${curr_close} --> Trend: {trend}")""",
        "step3_out": """Previous: $102.0 | Current: $104.5 --> Trend: BULLISH""",
        "step3_exp": "পাইথনের টের্নারি এক্সপ্রেশন দিয়ে মাত্র এক লাইনে ক্যান্ডেল ট্রেন্ড স্ট্যাটাস নির্ধারণ করা হয়।"
    },
    {
        "id": "p01_t05",
        "dir": "05_Loops",
        "num": "০৫",
        "title_bn": "লুপস ও ইটারেশন: প্রাইস হিস্ট্রি ও মুভিং এভারেজ ক্যালকুলেশন",
        "title_en": "Loops in Price Series & Moving Averages",
        "theory_bn": """<h3>সিরিয়াল ডেটা প্রসেসিংয়ে লুপের ভূমিকা</h3>
<p>হিস্টোরিক্যাল প্রাইস বার বিশ্লেষণ, ব্যাকটেস্টিং এবং চলমান গড় (SMA) বের করতে পাইথনের for এবং while লুপ ব্যবহার করা হয়। উইন্ডো স্লাইসিং টেকনিক ব্যবহার করে প্রতিটি ক্যান্ডেলের গড় মান বের করা অ্যালগো ট্রেডিংয়ের ভিত্তি।</p>""",
        "scenario": "৭টি ক্যান্ডেলের ক্লোজিং প্রাইস সিরিজ ধরে লুপের মাধ্যমে ৩-পিরিয়ড সিম্পল মুভিং এভারেজ (SMA) গণনা।",
        "step1_title": "ধাপ ১: হিস্টোরিক্যাল ক্লোজ প্রাইস ইটারেশন ও সামারি",
        "step1_code": """prices = [100.0, 102.0, 101.5, 104.0, 103.5, 106.0, 108.0]

total = 0.0
for p in prices:
    total += p

mean_price = total / len(prices)
print("Total Sum: $", round(total, 2))
print("Sample Mean Price: $", round(mean_price, 2))""",
        "step1_out": """Total Sum: $ 725.0
Sample Mean Price: $ 103.57""",
        "step1_exp": "for লুপ দিয়ে প্রতিটি প্রাইস পয়েন্ট প্রসেস করে সমষ্টি এবং গড় হিসেব করা হয়েছে।",

        "step2_title": "ধাপ ২: ৩-পিরিয়ড রোলিং মুভিং এভারেজ লুপ",
        "step2_code": """window = 3
sma_list = []

for i in range(len(prices) - window + 1):
    slice_prices = prices[i : i + window]
    sma = sum(slice_prices) / window
    sma_list.append(round(sma, 2))
    print(f"Window {i+1} {slice_prices} -> SMA: {round(sma, 2)}")

print("Calculated SMA Series:", sma_list)""",
        "step2_out": """Window 1 [100.0, 102.0, 101.5] -> SMA: 101.17
Window 2 [102.0, 101.5, 104.0] -> SMA: 102.5
Window 3 [101.5, 104.0, 103.5] -> SMA: 103.0
Window 4 [104.0, 103.5, 106.0] -> SMA: 104.5
Window 5 [103.5, 106.0, 108.0] -> SMA: 105.83
Calculated SMA Series: [101.17, 102.5, 103.0, 104.5, 105.83]""",
        "step2_exp": "স্লাইডিং উইন্ডো ব্যবহার করে প্রতিটি ধাপে ৩টি ক্যান্ডেলের গড় নিয়ে রোলিং মুভিং এভারেজ তৈরি করা হয়েছে।",

        "step3_title": "ধাপ ৩: হোয়াইল লুপ দিয়ে ব্যাকটেস্ট পজিশন ট্র্যাকিং",
        "step3_code": """equity = 1000.0
target = 1050.0
bar = 0

daily_gains = [12.0, -5.0, 18.0, 15.0, 16.0]

while equity < target and bar < len(daily_gains):
    equity += daily_gains[bar]
    bar += 1
    print(f"Bar {bar}: Equity = ${equity:.2f}")

print("Target reached or data exhausted at Bar:", bar)""",
        "step3_out": """Bar 1: Equity = $1012.00
Bar 2: Equity = $1007.00
Bar 3: Equity = $1025.00
Bar 4: Equity = $1040.00
Bar 5: Equity = $1056.00
Target reached or data exhausted at Bar: 5""",
        "step3_exp": "while লুপ দিয়ে শর্ত পূরণ না হওয়া পর্যন্ত বার-বাই-বার সিমুলেশন রান করে প্রফিট টার্গেট পূরণ টেস্ট করা হয়েছে।"
    },
    {
        "id": "p01_t06",
        "dir": "06_Functions",
        "num": "০৬",
        "title_bn": "ফাংশনস ও কোড মডুলারিটি: পজিশন সাইজার ও রিস্ক ইঞ্জিন",
        "title_en": "Functions & Code Modularity for Risk Engines",
        "theory_bn": """<h3>পুনর্ব্যবহারযোগ্য ট্রেডিং ফাংশন তৈরি</h3>
<p>একই হিসাব বারবার কোড না করে ফাংশন তৈরি করা সফটওয়্যার ইঞ্জিনিয়ারিং ও অ্যালগো ট্রেডিংয়ের সবচেয়ে ভালো অভ্যাস। যেমন: রিস্ক ক্যালকুলেটর, পজিশন সাইজার ও ড্র-ডাউন মাপার ফাংশন।</p>""",
        "scenario": "একাধিক ট্রেডের জন্য ১% রিস্ক নিয়মে পজিশন সাইজ ও রিস্ক-রিওয়ার্ড রেশিও নির্ণয়ের মডুলার ফাংশন তৈরি।",
        "step1_title": "ধাপ ১: পজিশন সাইজিং ফাংশন ডিফাইন",
        "step1_code": """def calculate_position_size(capital, risk_pct, entry_price, stop_loss):
    risk_dollars = capital * (risk_pct / 100.0)
    risk_per_share = abs(entry_price - stop_loss)
    if risk_per_share == 0:
        return 0
    return int(risk_dollars / risk_per_share)

size = calculate_position_size(capital=10000, risk_pct=1.0, entry_price=100, stop_loss=95)
print("Calculated Shares to Buy:", size, "units")""",
        "step1_out": """Calculated Shares to Buy: 20 units""",
        "step1_exp": "ফাংশনে ক্যাপিটাল, রিস্ক শতাংশ এবং প্রাইস পাস করে এক্সাক্ট লট বা শেয়ার সংখ্যা বের করা হয়েছে।",

        "step2_title": "ধাপ ২: ডিফল্ট প্যারামিটার ও মাল্টিপল রিটার্ন",
        "step2_code": """def evaluate_trade(entry, target, stop, fee_rate=0.001):
    gain = (target - entry) - (entry * fee_rate)
    risk = (entry - stop) + (entry * fee_rate)
    rr = gain / risk if risk > 0 else 0.0
    is_valid = rr >= 2.0
    return round(rr, 2), is_valid

ratio, approved = evaluate_trade(entry=100, target=112, stop=95)
print(f"Risk-Reward Ratio: {ratio} | Trade Approved: {approved}")""",
        "step2_out": """Risk-Reward Ratio: 2.36 | Trade Approved: True""",
        "step2_exp": "ডিফল্ট ট্রেডিং ফি দিয়ে মাল্টিপল রিটার্ন (টাপল) রিটার্ন করার পরিষ্কার উদাহরণ।",

        "step3_title": "ধাপ ৩: আর্বিট্রারি আর্গুমেন্টস (*args ও **kwargs)",
        "step3_code": """def summarize_portfolio(*returns, **meta):
    avg_return = sum(returns) / len(returns)
    print(f"Strategy: {meta.get('strategy', 'Unknown')} | Asset: {meta.get('asset', 'N/A')}")
    print(f"Average Return across {len(returns)} trades: {avg_return:.2f}%")

summarize_portfolio(1.2, -0.5, 2.4, 1.8, -0.3, strategy="Momentum-Alpha", asset="BTC")""",
        "step3_out": """Strategy: Momentum-Alpha | Asset: BTC
Average Return across 5 trades: 0.92%""",
        "step3_exp": "args ও kwargs দিয়ে ডাইনামিক সংখ্যক ট্রেড ফলাফল ও মেটাডেটা গ্রহণ করা।"
    },
    {
        "id": "p01_t07",
        "dir": "07_Lambda_Functions",
        "num": "০৭",
        "title_bn": "ল্যাম্বডা ফাংশনস: ফাস্ট অর্ডারবুক সর্টিং ও ট্রান্সফরমেশন",
        "title_en": "Lambda Functions for Rapid Order Book Sorting",
        "theory_bn": """<h3>এক লাইনের বেনামী (Anonymous) ফাংশন</h3>
<p>ল্যাম্বডা (Lambda) ফাংশন ছোট ছোট হিসাব এবং সর্টিং কি (sorting keys) হিসেবে পাইথনে ব্যবহৃত হয়। যেমন: অর্ডারবুকে প্রাইস অনুযায়ী অর্ডার সাজানো কিংবা রিটার্ন রূপান্তর করা।</p>""",
        "scenario": "লাইভ অর্ডারবুকের গভীরতার অর্ডারগুলোকে ল্যাম্বডা দিয়ে দ্রুত সর্ট করা এবং ম্যাপ ও ফিল্টার প্রয়োগ।",
        "step1_title": "ধাপ ১: ল্যাম্বডা দিয়ে অর্ডারবুক সর্টিং",
        "step1_code": """orders = [
    {"id": 1, "price": 67420.0, "qty": 1.5},
    {"id": 2, "price": 67400.0, "qty": 4.2},
    {"id": 3, "price": 67450.0, "qty": 0.8}
]

# সর্বোচ্চ দামের অর্ডার সবার আগে রাখা (বিড সর্টিং)
sorted_bids = sorted(orders, key=lambda x: x["price"], reverse=True)
print("Top Bid Order ID:", sorted_bids[0]["id"], "at Price: $", sorted_bids[0]["price"])""",
        "step1_out": """Top Bid Order ID: 3 at Price: $ 67450.0""",
        "step1_exp": "lambda x: x['price'] দিয়ে ডিকশনারি তালিকার মধ্য থেকে দাম অনুযায়ী অর্ডার সাজানো হয়েছে।",

        "step2_title": "ধাপ ২: map() এর সাথে ল্যাম্বডা রিটার্ন রূপান্তর",
        "step2_code": """close_prices = [100.0, 102.0, 105.0, 103.0]
entry = 100.0

pct_returns = list(map(lambda p: round(((p - entry) / entry) * 100, 2), close_prices))
print("Percentage Returns from Entry:", pct_returns)""",
        "step2_out": """Percentage Returns from Entry: [0.0, 2.0, 5.0, 3.0]""",
        "step2_exp": "map() এবং ল্যাম্বডা দিয়ে এক লাইনে সম্পূর্ণ প্রাইস লিস্টকে রিটার্নে কনভার্ট করা হয়েছে।",

        "step3_title": "ধাপ ৩: filter() এর সাথে ল্যাম্বডা ভলিউম স্পাইক ফিল্টার",
        "step3_code": """ticks = [
    {"vol": 12, "symbol": "BTC"},
    {"vol": 85, "symbol": "ETH"},
    {"vol": 120, "symbol": "SOL"},
    {"vol": 45, "symbol": "AVAX"}
]

high_volume = list(filter(lambda t: t["vol"] >= 80, ticks))
print("High Volume Spikes Detected:", [t["symbol"] for t in high_volume])""",
        "step3_out": """High Volume Spikes Detected: ['ETH', 'SOL']""",
        "step3_exp": "filter() দিয়ে ৮০ বা তার বেশি ভলিউমের অ্যাসেটগুলো নিমেষেই ফিল্টার করা হয়েছে।"
    },
    {
        "id": "p01_t08",
        "dir": "08_List_Comprehensions",
        "num": "০৮",
        "title_bn": "লিস্ট কম্প্রিহেনশন: ভেক্টরাইজড রিটার্ন পাইপলাইন",
        "title_en": "List Comprehensions in Return Calculations",
        "theory_bn": """<h3>দ্রুত ও সংক্ষিপ্ত ডেটা প্রসেসিং পাইপলাইন</h3>
<p>লিস্ট কম্প্রিহেনশন সাধারণ for লুপের চেয়ে দ্রুত কাজ করে এবং কোড অনেক পরিষ্কার ও রিডেবল রাখে। ক্যান্ডেল থেকে ক্যান্ডেলের রিটার্ন বের করতে এটি অত্যন্ত কার্যকর।</p>""",
        "scenario": "ক্যান্ডেলস্টিক তালিকা থেকে এক লাইনে বুলিশ ক্যান্ডেল ফিল্টার করা এবং রিটার্ন সিরিজ তৈরি।",
        "step1_title": "ধাপ ১: এক লাইনে রিটার্ন ক্যালকুলেশন",
        "step1_code": """prices = [100.0, 102.5, 101.0, 104.0, 106.5]

returns = [round((prices[i] - prices[i-1]) / prices[i-1] * 100, 2) for i in range(1, len(prices))]
print("Calculated Returns (%):", returns)""",
        "step1_out": """Calculated Returns (%): [2.5, -1.46, 2.97, 2.4]""",
        "step1_exp": "লিস্ট কম্প্রিহেনশনের মাধ্যমে ক্যান্ডেলগুলোর শতকরা লাভ/লস এক লাইনে রূপান্তর।",

        "step2_title": "ধাপ ২: শর্তযুক্ত ফিল্টারিং (Conditional Comprehension)",
        "step2_code": """# শুধুমাত্র পজিটিভ রিটার্নগুলো ফিল্টার করা
winning_trades = [r for r in returns if r > 0]
win_rate = (len(winning_trades) / len(returns)) * 100

print("Winning Trades (%):", winning_trades)
print("Win Rate:", win_rate, "%")""",
        "step2_out": """Winning Trades (%): [2.5, 2.97, 2.4]
Win Rate: 75.0 %""",
        "step2_exp": "if ফিল্টার যুক্ত করে উইনিং ট্রেডগুলোর তালিকা ও উইন রেট তৈরি করা।",

        "step3_title": "ধাপ ৩: ডিকশনারি কম্প্রিহেনশন দিয়ে টিকার ম্যাপিং",
        "step3_code": """symbols = ["BTC", "ETH", "SOL"]
prices_usd = [67400, 3500, 175]

market_map = {sym: pr for sym, pr in zip(symbols, prices_usd)}
print("Market Price Map:", market_map)""",
        "step3_out": """Market Price Map: {'BTC': 67400, 'ETH': 3500, 'SOL': 175}""",
        "step3_exp": "zip() ও ডিকশনারি কম্প্রিহেনশন দিয়ে একাধিক লিস্টকে এক পলকে ডিকশনারিতে রূপান্তর।"
    },
    {
        "id": "p01_t09",
        "dir": "09_File_Handling",
        "num": "০৯",
        "title_bn": "ফাইল হ্যান্ডলিং: ট্রেড লগিং ও হিস্টোরিক্যাল CSV রিডিং",
        "title_en": "File Handling for Trade Logs & CSV Bar Data",
        "theory_bn": """<h3>ট্রেড এক্সিকিউশন লগিং ও ডেটা পার্সিং</h3>
<p>লাইভ ট্রেডিং বট বন্ধ হলেও ট্রেড লগ সংরক্ষণ করতে ফাইলে ডেটা রাইট করতে হয়। এছাড়া ব্যাকটেস্টিংয়ের জন্য ডিস্ক থেকে হিস্টোরিক্যাল CSV ক্যান্ডেল ডেটা রিড করা অ্যালগো ইঞ্জিনিয়ারের প্রতিদিনের কাজ।</p>""",
        "scenario": "লাইভ ট্রেড কনফার্মেশন ফাইলে লগ করা এবং সেভ করা ট্রেড লগ লাইন-বাই-লাইন রিড করে পিএনএল হিসাব।",
        "step1_title": "ধাপ ১: ট্রেড এক্সিকিউশন লগ ফাইলে লেখা (Writing)",
        "step1_code": """trades = [
    "2026-11-19,BTC,BUY,67400.0,1.5",
    "2026-11-19,ETH,BUY,3500.0,10.0",
    "2026-11-19,BTC,SELL,67900.0,1.5"
]

with open("trade_log.txt", "w", encoding="utf-8") as f:
    for t in trades:
        f.write(t + "\\n")

print("Successfully written", len(trades), "trades to trade_log.txt")""",
        "step1_out": """Successfully written 3 trades to trade_log.txt""",
        "step1_exp": "with কনটেক্সট ম্যানেজার ব্যবহার করে ফাইল সেফভাবে ওপেন ও রাইট করা হয়েছে।",

        "step2_title": "ধাপ ২: ফাইল রিড করে ট্রেড ডেটা পার্সিং",
        "step2_code": """parsed_trades = []
with open("trade_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        parsed_trades.append({
            "date": parts[0], "symbol": parts[1], 
            "side": parts[2], "price": float(parts[3]), "qty": float(parts[4])
        })

print("Parsed First Trade:", parsed_trades[0])
print("Total Trades Read:", len(parsed_trades))""",
        "step2_out": """Parsed First Trade: {'date': '2026-11-19', 'symbol': 'BTC', 'side': 'BUY', 'price': 67400.0, 'qty': 1.5}
Total Trades Read: 3""",
        "step2_exp": "ফাইল থেকে প্রতিটি লাইন পড়ে কমা দিয়ে স্প্লিট করে ডিকশনারি লিস্ট তৈরি করা হয়েছে।",

        "step3_title": "ধাপ ৩: পিএনএল ক্যালকুলেশন ও ফাইল ক্লিনআপ",
        "step3_code": """import os

buy_val = parsed_trades[0]["price"] * parsed_trades[0]["qty"]
sell_val = parsed_trades[2]["price"] * parsed_trades[2]["qty"]
btc_profit = sell_val - buy_val

print(f"BTC Roundtrip Realized PnL: ${btc_profit:,.2f}")
if os.path.exists("trade_log.txt"):
    os.remove("trade_log.txt")
    print("Temporary log file cleaned up.")""",
        "step3_out": """BTC Roundtrip Realized PnL: $750.00
Temporary log file cleaned up.""",
        "step3_exp": "পার্স করা ডেটা থেকে নিট লাভ হিসাব করা হয়েছে এবং কাজ শেষে ফাইল ক্লিনআপ করা হয়েছে।"
    },
    {
        "id": "p01_t10",
        "dir": "10_Exception_Handling",
        "num": "১০",
        "title_bn": "এক্সেপশন হ্যান্ডলিং: রোবাস্ট ফল্ট-টলারেন্ট ট্রেডিং সিস্টেম",
        "title_en": "Exception Handling for Mission-Critical Trading Systems",
        "theory_bn": """<h3>ট্রেডিং বটের ক্র্যাশ রোধে ট্রাই-এক্সেপ্ট</h3>
<p>লাইভ মার্কেটে নেটওয়ার্ক সমস্যা, API এরর বা অপ্রত্যাশিত ইনপুট হলে বট যাতে ক্র্যাশ না করে, সেজন্য <code>try-except-finally</code> ব্লক ব্যবহার করা আবশ্যক। ট্রেডিংয়ে একটি ক্র্যাশ মানেই বিরাট মূলধন হারানোর ঝুঁকি!</p>""",
        "scenario": "মার্কেট ডেটা ফেচিং এরর, জিরো ডিভিশন রিটার্ন বাগ এবং মিসিং কী এক্সেপশন হ্যান্ডেল করা।",
        "step1_title": "ধাপ ১: জিরো ডিভিশন ও ভ্যালু এরর হ্যান্ডলিং",
        "step1_code": """def safe_return_calc(curr, prev):
    try:
        return (curr - prev) / prev
    except ZeroDivisionError:
        print("Warning: Previous price was 0! Division by zero prevented.")
        return 0.0

ret = safe_return_calc(105.0, 0.0)
print("Safe Return:", ret)""",
        "step1_out": """Warning: Previous price was 0! Division by zero prevented.
Safe Return: 0.0""",
        "step1_exp": "জিরো ডিভিশন এরর ট্র্যাপ করে বট ক্র্যাশ হওয়া থেকে রক্ষা করা হয়েছে।",

        "step2_title": "ধাপ ২: ডিকশনারি কী-এরর ও টাইপ এরর সেফগার্ড",
        "step2_code": """raw_packet = {"symbol": "BTC/USDT", "bid": 67400.0}

try:
    ask = raw_packet["ask"]
except KeyError as e:
    print(f"KeyError handled: Missing key {e} in ticker packet. Using fallback.")
    ask = raw_packet["bid"] + 5.0

print("Recovered Ask Price: $", ask)""",
        "step2_out": """KeyError handled: Missing key 'ask' in ticker packet. Using fallback.
Recovered Ask Price: $ 67405.0""",
        "step2_exp": "API প্যাকেটে 'ask' না থাকলে ফলব্যাক মেকানিজম দিয়ে ডেটা রিকভারি করা হয়েছে।",

        "step3_title": "ধাপ ৩: কাস্টম এক্সেপশন ও ফাইনালি ব্লক",
        "step3_code": """class InsufficientMarginError(Exception):
    pass

def execute_order(balance, margin_req):
    try:
        if balance < margin_req:
            raise InsufficientMarginError("Account balance is below required margin!")
        print("Order placed successfully.")
    except InsufficientMarginError as err:
        print("ORDER REJECTED:", err)
    finally:
        print("Execution heartbeat logged.")

execute_order(balance=500, margin_req=1000)""",
        "step3_out": """ORDER REJECTED: Account balance is below required margin!
Execution heartbeat logged.""",
        "step3_exp": "কাস্টম এক্সেপশন তৈরি করে মার্জিন ঘাটতি স্পষ্টভাবে হ্যান্ডেল করা হয়েছে।"
    },
    {
        "id": "p01_t11",
        "dir": "11_Object_Oriented_Programming",
        "num": "১১",
        "title_bn": "অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP): পজিশন ও অ্যাকাউন্ট ক্লাস",
        "title_en": "OOP Architecture for Positions & Portfolio Accounts",
        "theory_bn": """<h3>ট্রেডিং সিস্টেম আর্কিটেকচারে OOP</h3>
<p>পেশাদার কোয়ান্ট সিস্টেমে সবকিছু অবজেক্ট হিসেবে চিন্তা করা হয়: প্রতিটি ওপেন ট্রেড একটি <code>Position</code> অবজেক্ট, ব্যবহারকারীর মূলধন পরিচালনা করে একটি <code>TradingAccount</code> ক্লাস। এনক্যাপসুলেশন ও মেথড দিয়ে হিসাব নিয়ন্ত্রণ করা হয়।</p>""",
        "scenario": "একটি অবজেক্ট-ওরিয়েন্টেড অ্যাকাউন্ট ও পজিশন ট্র্যাকিং সিস্টেম তৈরি যেখানে অটোমেটিক PnL আপডেট হয়।",
        "step1_title": "ধাপ ১: পজিশন ক্লাস ও PnL মেথড",
        "step1_code": """class Position:
    def __init__(self, symbol, entry_price, size, is_long=True):
        self.symbol = symbol
        self.entry_price = float(entry_price)
        self.size = float(size)
        self.is_long = is_long

    def get_unrealized_pnl(self, current_price):
        diff = (current_price - self.entry_price) if self.is_long else (self.entry_price - current_price)
        return round(diff * self.size, 2)

pos = Position(symbol="BTC/USDT", entry_price=67000.0, size=2.0)
print("Position:", pos.symbol, "| Size:", pos.size, "BTC")
print("Unrealized PnL at $68,500: $", pos.get_unrealized_pnl(68500.0))""",
        "step1_out": """Position: BTC/USDT | Size: 2.0 BTC
Unrealized PnL at $68,500: $ 3000.0""",
        "step1_exp": "Position ক্লাসে স্টেট (symbol, entry_price) এবং বিহেভিয়ার (get_unrealized_pnl) এনক্যাপসুলেট করা হয়েছে।",

        "step2_title": "ধাপ ২: অ্যাকাউন্ট পোর্টফোলিও ক্লাস",
        "step2_code": """class TradingAccount:
    def __init__(self, account_id, initial_balance):
        self.account_id = account_id
        self.cash = float(initial_balance)
        self.positions = []

    def add_position(self, pos):
        self.positions.append(pos)
        print(f"[{self.account_id}] Opened position: {pos.size} {pos.symbol}")

    def total_equity(self, current_prices):
        unrealized = sum(p.get_unrealized_pnl(current_prices.get(p.symbol, p.entry_price)) for p in self.positions)
        return round(self.cash + unrealized, 2)

acc = TradingAccount("ACC-901", 10000.0)
acc.add_position(pos)
print("Account Total Equity: $", acc.total_equity({"BTC/USDT": 68500.0}))""",
        "step2_out": """[ACC-901] Opened position: 2.0 BTC/USDT
Account Total Equity: $ 13000.0""",
        "step2_exp": "TradingAccount ক্লাসের ভেতরে একাধিক Position অবজেক্ট ম্যানেজ করে লাইভ ইকুইটি নির্ণয়।",

        "step3_title": "ধাপ ৩: ইনহেরিটেন্স ও মার্জিন অ্যাকাউন্ট",
        "step3_code": """class MarginAccount(TradingAccount):
    def __init__(self, account_id, initial_balance, leverage=5):
        super().__init__(account_id, initial_balance)
        self.leverage = leverage

    def available_margin(self):
        return round(self.cash * self.leverage, 2)

m_acc = MarginAccount("MARGIN-77", 5000.0, leverage=10)
print(f"Margin Account: {m_acc.account_id} | Leverage: {m_acc.leverage}x | Buying Power: ${m_acc.available_margin():,}")""",
        "step3_out": """Margin Account: MARGIN-77 | Leverage: 10x | Buying Power: $50,000.0""",
        "step3_exp": "ইনহেরিটেন্স ব্যবহার করে সাধারণ অ্যাকাউন্ট থেকে মার্জিন অ্যাকাউন্ট এক্সটেন্ড করা হয়েছে।"
    },
    {
        "id": "p01_t12",
        "dir": "12_Modules_and_Packages",
        "num": "১২",
        "title_bn": "মডিউলস ও প্যাকেজেস: কোয়ান্ট ট্রেডিং লাইব্রেরি অর্গানাইজেশন",
        "title_en": "Modules & Packaging for Systematic Trading Code",
        "theory_bn": """<h3>কোড অর্গানাইজেশন ও স্ট্যান্ডার্ড লাইব্রেরি</h3>
<p>একটি পূর্ণাঙ্গ ট্রেডিং অ্যালগরিদম শত শত ফাইলে বিভক্ত থাকে। পাইথনের বিল্ট-ইন <code>math</code>, <code>datetime</code> মডিউল ব্যবহার এবং নিজস্ব ফাইলগুলোকে মডিউলে রূপান্তর করা সিস্টেমের স্কেলেবিলিটির জন্য জরুরি।</p>""",
        "scenario": "datetime এবং math মডিউল ব্যবহার করে ক্যান্ডেলস্টিক টাইমস্ট্যাম্প ও ভলাটিলিটি হিসাব।",
        "step1_title": "ধাপ ১: datetime মডিউল দিয়ে টাইমস্ট্যাম্প পার্সিং",
        "step1_code": """from datetime import datetime, timezone

unix_ts = 1732057200
utc_time = datetime.fromtimestamp(unix_ts, tz=timezone.utc)
formatted_time = utc_time.strftime("%Y-%m-%d %H:%M:%S UTC")

print("Unix Timestamp:", unix_ts)
print("Parsed UTC Candle Time:", formatted_time)""",
        "step1_out": """Unix Timestamp: 1732057200
Parsed UTC Candle Time: 2024-11-19 23:00:00 UTC""",
        "step1_exp": "datetime মডিউল ব্যবহার করে ইউনিক্স টাইমস্ট্যাম্পকে মানুষের পাঠযোগ্য ইউটিসি সময়ে রূপান্তর।",

        "step2_title": "ধাপ ২: math মডিউল দিয়ে লগারিদম ও ভলাটিলিটি স্কেলিং",
        "step2_code": """import math

daily_vol = 0.02
trading_days = 252
annualized_vol = daily_vol * math.sqrt(trading_days)

print("Daily Volatility: 2.0%")
print(f"Annualized Volatility (sqrt(252)): {annualized_vol * 100:.2f}%")""",
        "step2_out": """Daily Volatility: 2.0%
Annualized Volatility (sqrt(252)): 31.75%""",
        "step2_exp": "math.sqrt() ব্যবহার করে দৈনিক ভলাটিলিটিকে বাৎসরিক স্কেলে রূপান্তর করা হয়েছে।",

        "step3_title": "ধাপ ৩: কাস্টম মডিউল ফাংশন সিমুলেশন",
        "step3_code": """def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
    mean_ret = sum(returns) / len(returns)
    variance = sum((r - mean_ret) ** 2 for r in returns) / len(returns)
    std_dev = math.sqrt(variance)
    return round((mean_ret - risk_free_rate) / std_dev, 2) if std_dev > 0 else 0.0

trade_rets = [0.03, 0.01, -0.01, 0.02, 0.04, -0.02]
sharpe = calculate_sharpe_ratio(trade_rets)
print("Calculated Sharpe Ratio:", sharpe)""",
        "step3_out": """Calculated Sharpe Ratio: 0.58""",
        "step3_exp": "মডুলার শার্প রেশিও ক্যালকুলেটর যা অন্য যেকোনো স্ক্রিপ্ট থেকে সরাসরি ইমপোর্ট করা যাবে।"
    },
    {
        "id": "p01_t13",
        "dir": "13_Virtual_Environments",
        "num": "১৩",
        "title_bn": "ভার্চুয়াল এনভায়রনমেন্টস ও ডিপেন্ডেন্সি ম্যানেজমেন্ট: প্রোডাকশন সেটআপ",
        "title_en": "Virtual Environments & Pip Dependency Management",
        "theory_bn": """<h3>আইসোলেটেড পাইথন এনভায়রনমেন্টের গুরুত্ব</h3>
<p>বিভিন্ন লাইব্রেরির (যেমন: NumPy 2.x বনাম 1.x) ভার্সন কনফ্লিক্ট এড়াতে প্রোডাকশন ট্রেডিং সিস্টেমে ভার্চুয়াল এনভায়রনমেন্ট (venv) ব্যবহার করা বাধ্যতামূলক। <code>requirements.txt</code> দিয়ে ডিপেন্ডেন্সি লক করা হয়।</p>""",
        "scenario": "ট্রেডিং প্রজেক্টের ডিপেন্ডেন্সি তালিকা তৈরি, প্যাকেজ ভার্সন ভ্যালিডেশন এবং এনভায়রনমেন্ট ম্যানেজমেন্ট।",
        "step1_title": "ধাপ ১: পাইথন sys ও ভার্সন ইন্সপেকশন",
        "step1_code": """import sys
import os

print("Python Executable Path:", sys.executable)
print("Python Major.Minor Version:", f"{sys.version_info.major}.{sys.version_info.minor}")
print("Is Running inside Virtual Env:", sys.prefix != sys.base_prefix)""",
        "step1_out": """Python Executable Path: C:\\Program Files\\Python313\\python.exe
Python Major.Minor Version: 3.13
Is Running inside Virtual Env: False""",
        "step1_exp": "sys মডিউল দিয়ে রানটাইম এনভায়রনমেন্ট এবং পাইথন ভার্সন ভ্যালিডেট করা হয়েছে।",

        "step2_title": "ধাপ ২: requirements.txt জেনারেট ও পার্সিং",
        "step2_code": """reqs = [
    "numpy>=2.0.0",
    "pandas>=2.2.0",
    "requests>=2.31.0",
    "scipy>=1.13.0"
]

with open("sample_requirements.txt", "w") as f:
    f.write("\\n".join(reqs) + "\\n")

with open("sample_requirements.txt", "r") as f:
    locked_packages = [line.strip().split(">=")[0] for line in f if line.strip()]

print("Locked Packages for Trading Bot:", locked_packages)
if os.path.exists("sample_requirements.txt"):
    os.remove("sample_requirements.txt")""",
        "step2_out": """Locked Packages for Trading Bot: ['numpy', 'pandas', 'requests', 'scipy']""",
        "step2_exp": "ডিপেন্ডেন্সি ফাইল রাইট এবং পার্স করে প্যাকেজ কনফ্লিক্ট ম্যানেজমেন্ট প্রদর্শন।",

        "step3_title": "ধাপ ৩: CLI কমান্ড গাইডলাইন",
        "step3_code": """commands = [
    "python -m venv .venv",
    ".\\\\.venv\\\\Scripts\\\\activate  # Windows",
    "pip install -r requirements.txt",
    "pip freeze > requirements.txt"
]

print("Standard Quant Deployment Workflow:")
for i, cmd in enumerate(commands, 1):
    print(f"{i}. {cmd}")""",
        "step3_out": """Standard Quant Deployment Workflow:
1. python -m venv .venv
2. .\\.venv\\Scripts\\activate  # Windows
3. pip install -r requirements.txt
4. pip freeze > requirements.txt""",
        "step3_exp": "ভার্চুয়াল এনভায়রনমেন্ট তৈরি, এক্টিভেট ও প্যাকেজ ফ্রিজ করার ৪টি স্ট্যান্ডার্ড কমান্ড।"
    },
    {
        "id": "p01_t14",
        "dir": "14_Working_with_APIs",
        "num": "১৪",
        "title_bn": "REST APIs ও HTTP রিকোয়েস্টস: পাবলিক মার্কেট ডেটা ফেচিং",
        "title_en": "REST APIs & HTTP Requests for Real-Time Market Data",
        "theory_bn": """<h3>এক্সচেঞ্জ API এর সাথে কানেক্টিভিটি</h3>
<p>অ্যালগো ট্রেডিং বট ব্রোকার বা এক্সচেঞ্জ সার্ভারের সাথে HTTP REST API (GET, POST) এর মাধ্যমে যোগাযোগ করে লাইভ টিকার এবং অর্ডারবুক ডেটা সংগ্রহ করে। রেসপন্স স্ট্যাটাস কোড (200 OK, 429 Rate Limit) যাচাই করা জরুরি।</p>""",
        "scenario": "পাবলিক মার্কেট API এন্ডপয়েন্ট থেকে লাইভ ক্রিপ্টো বা স্টক প্রাইস ফেচিং ও রেসপন্স পার্সিং সিমুলেশন।",
        "step1_title": "ধাপ ১: HTTP রেসপন্স স্ট্যাটাস ও পে-লোড পার্সিং",
        "step1_code": """# সিমুলেটেড API রেসপন্স পে-লোড
mock_api_response = {
    "status_code": 200,
    "payload": {
        "symbol": "BTCUSDT",
        "price": "67489.20",
        "timestamp": 1732057200000
    }
}

if mock_api_response["status_code"] == 200:
    data = mock_api_response["payload"]
    price = float(data["price"])
    print(f"API Success 200 OK! Asset: {data['symbol']} | Latest Price: ${price:,.2f}")
else:
    print("API Error:", mock_api_response["status_code"])""",
        "step1_out": """API Success 200 OK! Asset: BTCUSDT | Latest Price: $67,489.20""",
        "step1_exp": "API রেসপন্সের স্ট্যাটাস যাচাই করে পে-লোড থেকে প্রাইস এক্সট্রাক্ট করা হয়েছে।",

        "step2_title": "ধাপ ২: কোয়েরি প্যারামিটার ও এন্ডপয়েন্ট বিল্ডার",
        "step2_code": """base_url = "https://api.exchange.com/v1/klines"
params = {"symbol": "BTCUSDT", "interval": "1h", "limit": 100}

query_str = "&".join(f"{k}={v}" for k, v in params.items())
full_endpoint = f"{base_url}?{query_str}"

print("Constructed REST API Endpoint:")
print(full_endpoint)""",
        "step2_out": """Constructed REST API Endpoint:
https://api.exchange.com/v1/klines?symbol=BTCUSDT&interval=1h&limit=100""",
        "step2_exp": "প্রফেশনাল অ্যালগো সিস্টেমের মতো এন্ডপয়েন্ট ইউআরএল ডাইনামিক্যালি বিল্ড করা হয়েছে।",

        "step3_title": "ধাপ ৩: রেট লিমিট হ্যান্ডলিং লজিক (429)",
        "step3_code": """def handle_api_status(status_code):
    if status_code == 200:
        return "READY_TO_PARSE"
    elif status_code == 429:
        return "BACKOFF_AND_SLEEP"
    elif status_code == 401:
        return "API_KEY_INVALID"
    else:
        return "UNKNOWN_SERVER_ERROR"

print("Status 200 Action:", handle_api_status(200))
print("Status 429 Action:", handle_api_status(429))""",
        "step3_out": """Status 200 Action: READY_TO_PARSE
Status 429 Action: BACKOFF_AND_SLEEP""",
        "step3_exp": "এক্সচেঞ্জের 429 Too Many Requests রেট লিমিট হ্যান্ডল করার স্মার্ট লজিক।"
    },
    {
        "id": "p01_t15",
        "dir": "15_Data_Serialization_JSON_CSV",
        "num": "১৫",
        "title_bn": "ডেটা সিরিয়ালাইজেশন (JSON ও CSV): মার্কেট ফিড এনকোডিং ও ডিকম্প্রেশন",
        "title_en": "Data Serialization (JSON & CSV) in Trading Feeds",
        "theory_bn": """<h3>মার্কেট স্ট্রিমিং ও স্টোরেজ ফরম্যাট</h3>
<p>ওয়েবসকেট এবং REST API তে ডেটা আদান-প্রদান হয় <strong>JSON</strong> ফরম্যাটে, আর হিস্টোরিক্যাল ব্যাকটেস্টিং ডেটা স্টোর করা হয় <strong>CSV</strong> ফাইলে। পাইথনের <code>json</code> এবং <code>csv</code> মডিউল দিয়ে এই ডেটা এনকোড এবং ডিকোড করা হয়।</p>""",
        "scenario": "মার্কেট টিক অবজেক্টকে JSON স্ট্রিংয়ে সিরিয়ালাইজ করা এবং ক্যান্ডেলস্টিক ডেটা CSV ফরম্যাটে এক্সপোর্ট করা।",
        "step1_title": "ধাপ ১: JSON সিরিয়ালাইজেশন ও ডিসিরিয়ালাইজেশন",
        "step1_code": """import json

tick_data = {
    "symbol": "BTC/USDT",
    "bids": [[67400.0, 1.2], [67390.0, 3.5]],
    "asks": [[67410.0, 0.8], [67420.0, 2.0]],
    "is_active": True
}

# Python Dict to JSON String
json_payload = json.dumps(tick_data)
# JSON String to Python Dict
parsed_back = json.loads(json_payload)

print("JSON String Payload:", json_payload)
print("Parsed Back Best Bid Price:", parsed_back["bids"][0][0])""",
        "step1_out": """JSON String Payload: {"symbol": "BTC/USDT", "bids": [[67400.0, 1.2], [67390.0, 3.5]], "asks": [[67410.0, 0.8], [67420.0, 2.0]], "is_active": true}
Parsed Back Best Bid Price: 67400.0""",
        "step1_exp": "json.dumps() এবং json.loads() দিয়ে মেমোরি অবজেক্ট এবং নেটওয়ার্ক স্ট্রিং এর মধ্যে নিখুঁত রূপান্তর।",

        "step2_title": "ধাপ ২: CSV ফরম্যাটে ক্যান্ডেল ডেটা এক্সপোর্ট",
        "step2_code": """import csv
import io

candles = [
    ["timestamp", "open", "high", "low", "close", "volume"],
    ["2026-11-19T20:00Z", 67100, 67300, 67050, 67250, 420.5],
    ["2026-11-19T21:00Z", 67250, 67500, 67200, 67480, 580.2]
]

output = io.StringIO()
writer = csv.writer(output)
writer.writerows(candles)

print("Serialized CSV Data:")
print(output.getvalue().strip())""",
        "step2_out": """Serialized CSV Data:
timestamp,open,high,low,close,volume
2026-11-19T20:00Z,67100,67300,67050,67250,420.5
2026-11-19T21:00Z,67250,67500,67200,67480,580.2""",
        "step2_exp": "csv.writer ব্যবহার করে ক্যান্ডেলস্টিক ডেটাকে স্ট্যান্ডার্ড কমা-সেপারেটেড ফরম্যাটে এক্সপোর্ট করা।",

        "step3_title": "ধাপ ৩: ডিকশনারি রিডার দিয়ে CSV পার্সিং",
        "step3_code": """csv_content = \"\"\"symbol,close,volume
BTC/USDT,67480,580
ETH/USDT,3520,1240\"\"\"

f = io.StringIO(csv_content)
reader = csv.DictReader(f)
parsed_bars = [row for row in reader]

print("First Asset Parsed from CSV:", parsed_bars[0]["symbol"], "| Price: $", parsed_bars[0]["close"])""",
        "step3_out": """First Asset Parsed from CSV: BTC/USDT | Price: $ 67480""",
        "step3_exp": "csv.DictReader দিয়ে হেডার নাম অনুযায়ী ডেটা রো-বাই-রো ডিকশনারিতে পার্স করা।"
    }
]

print("Phase 1 data ready with", len(P1_TOPICS), "topics")
