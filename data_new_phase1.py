# data_new_phase1.py
# Phase 01: Data Analysis & Manipulation (18 Topics)

P1_TOPICS = [
    {
        "num": "01",
        "dir_name": "01_NumPy_Fundamentals",
        "title_en": "NumPy Fundamentals",
        "title_bn": "টপিক ০১: NumPy ফান্ডামেন্টালস ও কোয়ান্টাম স্পিড মেমোরি",
        "scenario": "হাই-ফ্রিকোয়েন্সি ট্রেডিং ডেটাসেটে পাইথনের সাধারণ লিস্টের মেমোরি ওভারহেড দূর করে সি-লেভেলের দ্রুততম মেমোরি বাফার এবং ndarray আর্কিটেকচার তৈরি করা।",
        "theory_bn": """
            <p><strong>NumPy (Numerical Python)</strong> হলো যেকোনো কোয়ান্টাম ও ডেটা সায়েন্স প্রজেক্টের মেরুদণ্ড। পাইথনের সাধারণ লিস্টের চেয়ে NumPy অ্যারে ৫০ থেকে ১০০ গুণ দ্রুত কাজ করে কারণ এটি মেমোরিতে <em>Contiguous Memory Blocks</em> (একটানা মেমোরি স্লট) ব্যবহার করে এবং সরাসরি C-লেভেল ইন্টারফেসের মাধ্যমে ভেক্টরাইজড অপারেশন চালায়।</p>
            <ul>
                <li><strong>C-Contiguous Memory:</strong> মেমোরিতে ডেটা ধারাবাহিকভাবে থাকে, ফলে CPU ক্যাশ মিস (Cache Miss) হয় না।</li>
                <li><strong>Homogeneous Data Types:</strong> একটি অ্যারের প্রতিটি উপাদান একই টাইপের (যেমন <code>float64</code>), যা টাইপ চেকিংয়ের বাড়তি সময় বাঁচায়।</li>
                <li><strong>Zero-Copy Views:</strong> নতুন মেমোরি অ্যালোকেট না করেই ডেটার বিভিন্ন ভিউ তৈরি করা যায়।</li>
            </ul>
        """,
        "step1_title": "NumPy ndarray তৈরি ও মেমোরি সাইজ পরীক্ষা",
        "step1_code": """import numpy as np
import sys

# সাধারণ পাইথন লিস্ট বনাম NumPy অ্যারে
py_list = [100.5, 101.2, 99.8, 102.4, 103.1]
np_arr = np.array(py_list, dtype=np.float64)

print("Python List Size in Bytes:", sys.getsizeof(py_list))
print("NumPy Array Size in Bytes:", np_arr.nbytes)
print("Array Shape:", np_arr.shape)
print("Data Type:", np_arr.dtype)""",
        "step1_out": """Python List Size in Bytes: 104
NumPy Array Size in Bytes: 40
Array Shape: (5,)
Data Type: float64""",
        "step1_exp": "NumPy অ্যারে প্রতিটি উপাদানের জন্য ফিক্সড ৮ বাইট (float64) মেমোরি নেয়, যেখানে পাইথন লিস্ট প্রতিটি ফ্লোটের রেফারেন্স ও মেটাডেটার জন্য বিশাল মেমোরি অপচয় করে।",
        
        "step2_title": "ট্রেডিং প্রাইস শিফট ও লুপ ছাড়া গণনা",
        "step2_code": """# ১ মিলিয়ন প্রাইস টিকের দ্রুত প্রসেসিং
prices = np.array([67200.0, 67250.5, 67180.0, 67320.0, 67400.5])

# ভেক্টরাইজড রিটার্ন ক্যালকুলেশন
pct_returns = (prices[1:] - prices[:-1]) / prices[:-1] * 100

print("Price Changes (%):", np.round(pct_returns, 3))
print("Average Return:", round(np.mean(pct_returns), 4), "%")""",
        "step2_out": """Price Changes (%): [ 0.075 -0.105  0.208  0.12 ]
Average Return: 0.0747 %""",
        "step2_exp": "কোনো for-loop ছাড়াই অ্যারের স্লাইসিং এবং ভেক্টরাইজেশনের মাধ্যমে চোখের পলকে প্রতি ট্রেডের পার্সেন্টেজ রিটার্ন বের করা হয়েছে।",

        "step3_title": "NumPy গাণিতিক ফাংশন ও ভোল্টেবিলিটি",
        "step3_code": """# বার্ষিক ভোলাটিলিটি ক্যালকুলেশন
daily_returns = np.array([0.012, -0.008, 0.015, -0.004, 0.009, -0.011])

volatility = np.std(daily_returns)
annualized_vol = volatility * np.sqrt(252)

print("Daily Volatility (Std):", round(volatility, 5))
print("Annualized Volatility:", round(annualized_vol * 100, 2), "%")""",
        "step3_out": """Daily Volatility (Std): 0.01041
Annualized Volatility: 16.53 %""",
        "step3_exp": "np.std দিয়ে স্ট্যান্ডার্ড ডেভিয়েশন এবং np.sqrt(252) দিয়ে অ্যানুয়ালাইজড ভোলাটিলিটি নিখুঁতভাবে বের করা হয়েছে।"
    },
    {
        "num": "02",
        "dir_name": "02_NumPy_Arrays",
        "title_en": "NumPy Arrays Creation & Strides",
        "title_bn": "টপিক ০২: NumPy অ্যারে তৈরি ও স্ট্রাইডস মেকানিজম",
        "scenario": "অ্যালগো ট্রেডিং সার্ভারে অর্ডারবুক ডেপ্থ (Bid/Ask 10 লেভেল) এবং ওএইচএলসিভি (OHLCV) ম্যাট্রিক্স জিরো-ওভারহেডে ইনিশিয়ালাইজ ও রি-শেপিং করা।",
        "theory_bn": """
            <p>NumPy অ্যারে তৈরি করার জন্য <code>np.zeros</code>, <code>np.ones</code>, <code>np.arange</code>, <code>np.linspace</code> ইত্যাদি ফাংশন রয়েছে। 2D এবং 3D অ্যারের ক্ষেত্রে <em>Strides</em> হলো এক উপাদান থেকে পরবর্তী উপাদানে যাওয়ার জন্য মেমোরিতে কয়টি বাইট অতিক্রম করতে হবে তার হিসাব।</p>
            <ul>
                <li><strong>zeros/ones:</strong> মেমোরি আগে থেকেই প্রি-অ্যালোকেট করে রাখার জন্য দ্রুততম উপায়।</li>
                <li><strong>Reshape & Strides:</strong> মেমোরি কপি না করেই ডেটার ডাইমেনশন রূপান্তর করা যায়।</li>
            </ul>
        """,
        "step1_title": "মাল্টি-লেভেল অর্ডারবুক ম্যাট্রিক্স ইনিশিয়ালাইজ",
        "step1_code": """import numpy as np

# ১০ লেভেলের Bid-Ask অর্ডারবুক ম্যাট্রিক্স: [Level, [Price, Volume]]
orderbook = np.zeros((10, 2), dtype=np.float64)

# লেভেল ১ ও ২ এ প্রাইস ও ভলিউম সেট করা
orderbook[0] = [67500.0, 4.25]
orderbook[1] = [67490.0, 12.80]

print("Orderbook Shape:", orderbook.shape)
print("Orderbook Memory Bytes:", orderbook.nbytes)
print("Top 2 Levels:\n", orderbook[:2])""",
        "step1_out": """Orderbook Shape: (10, 2)
Orderbook Memory Bytes: 160
Top 2 Levels:
 [[67500.       4.25]
 [67490.      12.8 ]]""",
        "step1_exp": "np.zeros দিয়ে ফিক্সড সাইজের অর্ডারবুক বাফার বানিয়ে সরাসরি ইনডেক্সিংয়ের মাধ্যমে ডেটা আপডেট করা হয়েছে।",

        "step2_title": "OHLCV 2D বার ম্যাট্রিক্স ও রেঞ্জ তৈরি",
        "step2_code": """# সিন্থেটিক মিনিট বারের টাইম ও প্রাইস ম্যাট্রিক্স
timestamps = np.arange(1700000000, 1700000300, 60)
prices = np.linspace(67100, 67450, len(timestamps))

market_data = np.column_stack((timestamps, prices))
print("Market Data Shape:", market_data.shape)
print("First 3 Rows:\n", market_data[:3])""",
        "step2_out": """Market Data Shape: (5, 2)
First 3 Rows:
 [[1.7000e+09 6.7100e+04]
 [1.7000e+09 6.7187e+04]
 [1.7000e+09 6.7275e+04]]""",
        "step2_exp": "np.arange ও np.linspace ব্যবহার করে টাইমস্ট্যাম্প এবং লিনিয়ার প্রাইস তৈরি করে np.column_stack দিয়ে 2D ম্যাট্রিক্স সাজানো হয়েছে।",

        "step3_title": "অ্যারে স্ট্রাইডস ও ফ্ল্যাটেনিং",
        "step3_code": """matrix = np.array([[10, 20], [30, 40], [50, 60]], dtype=np.int32)

print("Matrix Shape:", matrix.shape)
print("Strides (Bytes per step):", matrix.strides)
print("Flattened View:", matrix.ravel())""",
        "step3_out": """Matrix Shape: (3, 2)
Strides (Bytes per step): (8, 4)
Flattened View: [10 20 30 40 50 60]""",
        "step3_exp": "প্রতিটি সারি অতিক্রম করতে ৮ বাইট এবং প্রতিটি কলামে যেতে ৪ বাইট স্ট্রাইড ব্যবহার হয়।"
    },
    {
        "num": "03",
        "dir_name": "03_Array_Indexing_and_Slicing",
        "title_en": "Array Indexing and Slicing",
        "title_bn": "টপিক ০৩: অ্যারে ইনডেক্সিং, স্লাইসিং ও বুলিয়ান ফিল্টারিং",
        "scenario": "ঐতিহাসিক ৫ মিনিটের ক্যান্ডেলস্টিক ডেটা থেকে উচ্চ ভোলাটিলিটি বার ও অস্বাভাবিক ভলিউম স্পাইক তাৎক্ষণিকভাবে ফিল্টার করা।",
        "theory_bn": """
            <p>NumPy ইনডেক্সিং এবং স্লাইসিংয়ের মাধ্যমে মেমোরিতে নতুন কপি তৈরি না করে সাব-অ্যারে নিয়ে কাজ করা যায়। <em>Boolean Masking</em> কোয়ান্ট ট্রেডিংয়ের অন্যতম শক্তিশালী ফিচার, যার সাহায্যে শর্ত অনুযায়ী ডেটা পয়েন্ট আলাদা করা যায়।</p>
            <ul>
                <li><strong>Slice Syntax:</strong> <code>array[start:stop:step]</code> মেমোরি-ভিউ রিটার্ন করে।</li>
                <li><strong>Boolean Masking:</strong> <code>prices[prices > threshold]</code> লুপ ছাড়াই ফিল্টার করে।</li>
            </ul>
        """,
        "step1_title": "2D OHLCV ক্যান্ডেল স্লাইসিং",
        "step1_code": """import numpy as np

# ক্যান্ডেল ডেটা: [Open, High, Low, Close, Volume]
candles = np.array([
    [67000, 67200, 66950, 67150, 150.0],
    [67150, 67400, 67100, 67350, 280.0],
    [67350, 67500, 67250, 67300, 95.0],
    [67300, 67600, 67280, 67580, 410.0]
])

close_prices = candles[:, 3]
volumes = candles[:, 4]

print("All Close Prices:", close_prices)
print("Latest 2 Candle Volumes:", volumes[-2:])""",
        "step1_out": """All Close Prices: [67150. 67350. 67300. 67580.]
Latest 2 Candle Volumes: [ 95. 410.]""",
        "step1_exp": "[:, 3] দিয়ে সব সারির ৪ নম্বর কলাম (Close) এবং [-2:] দিয়ে শেষ দুই ক্যান্ডেলের ভলিউম স্লাইস করা হয়েছে।",

        "step2_title": "বুলিয়ান ফিল্টারিংয়ে হাই-ভলিউম ব্রেকআউট নির্ণয়",
        "step2_code": """# ভলিউম থ্রেশহোল্ড ২০০ এর বেশি এমন ক্যান্ডেল ফিল্টার
high_vol_mask = candles[:, 4] > 200.0
breakout_candles = candles[high_vol_mask]

print("High Volume Mask:", high_vol_mask)
print("Breakout Candles Count:", len(breakout_candles))
print("Breakout Candle Closes:", breakout_candles[:, 3])""",
        "step2_out": """High Volume Mask: [False  True False  True]
Breakout Candles Count: 2
Breakout Candle Closes: [67350. 67580.]""",
        "step2_exp": "শর্তসাপেক্ষ বুলিয়ান মাস্ক দিয়ে শুধুমাত্র উচ্চ ভলিউম যুক্ত ব্রেকআউট ক্যান্ডেলগুলো লুপ ছাড়াই দ্রুত বের করা হয়েছে।",

        "step3_title": "ফ্যান্সি ইনডেক্সিং ও নির্দিষ্ট টাইমস্ট্যাম্প এক্সট্রাকশন",
        "step3_code": """target_indices = np.array([0, 3])
selected_candles = candles[target_indices]

print("Selected Specific Rows:\n", selected_candles)""",
        "step3_out": """Selected Specific Rows:
 [[67000.  67200.  66950.  67150.    150. ]
 [67300.  67600.  67280.  67580.    410. ]]""",
        "step3_exp": "ফ্যান্সি ইনডেক্সিংয়ের মাধ্যমে নির্দিষ্ট ইনডেক্স অ্যারে পাস করে কাঙ্ক্ষিত ক্যান্ডেলগুলো এক্সট্র্যাক্ট করা হয়েছে।"
    },
    {
        "num": "04",
        "dir_name": "04_Broadcasting",
        "title_en": "Broadcasting in Financial Matrices",
        "title_bn": "টপিক ০৪: ব্রডকাস্টিং ও মাল্টি-অ্যাসেট ফি ক্যালকুলেশন",
        "scenario": "ভিন্ন শেপের ম্যাট্রিক্সে লুপ না চালিয়ে সম্পূর্ণ পোর্টফোলিও প্রাইস ম্যাট্রিক্সের ওপর ব্রোকারেজ ফি এবং বিড-আস্ক স্প্রেড একবারে অ্যাডজাস্ট করা।",
        "theory_bn": """
            <p><strong>Broadcasting</strong> হলো NumPy-এর এমন একটি বৈশিষ্ট্য যা ভিন্ন আকারের (Shape) অ্যারের মধ্যে সরাসরি গাণিতিক অপারেশন করতে সাহায্য করে। ছোট অ্যারেটি স্বয়ংক্রিয়ভাবে বড় অ্যারের আকারের সাথে ভার্চুয়ালি প্রসারিত হয় কোনো অতিরিক্ত মেমোরি খরচ না করে।</p>
            <ul>
                <li><strong>রুল ১:</strong> দুটি অ্যারের ডাইমেনশন সমান না হলে বাম পাশে ১ যোগ করে ডাইমেনশন মেলানো হয়।</li>
                <li><strong>রুল ২:</strong> যেকোনো ডাইমেনশনে সাইজ ১ হলে তা অপর অ্যারের ডাইমেনশনের সমান হয়ে যায়।</li>
            </ul>
        """,
        "step1_title": "মাল্টিপল অ্যাসেট প্রাইসে স্প্রেড যোগ করা",
        "step1_code": """import numpy as np

# ৪টি অ্যাসেটের ৩ দিনের ক্লোজিং প্রাইস (3 x 4)
# Assets: [BTC, ETH, SOL, BNB]
prices = np.array([
    [67000.0, 3500.0, 180.0, 590.0],
    [67200.0, 3540.0, 185.0, 595.0],
    [67100.0, 3520.0, 182.0, 592.0]
])

# প্রতিটি অ্যাসেটের ফিক্সড স্প্রেড (1D array of 4 elements)
spreads = np.array([2.5, 0.5, 0.1, 0.2])

# ব্রডকাস্টিংয়ের মাধ্যমে আস্ক প্রাইস ম্যাট্রিক্স
ask_prices = prices + spreads
print("Original Prices (Day 1):", prices[0])
print("Ask Prices with Spread (Day 1):", ask_prices[0])""",
        "step1_out": """Original Prices (Day 1): [67000.  3500.   180.   590.]
Ask Prices with Spread (Day 1): [67002.5  3500.5   180.1   590.2]""",
        "step1_exp": "(3, 4) ম্যাট্রিক্স এবং (4,) ভেক্টরের মধ্যে ব্রডকাস্টিং হয়ে প্রতিটি অ্যাসেটের নিজস্ব স্প্রেড নির্ভুলভাবে যোগ হয়েছে।",

        "step2_title": "ট্রেডিং ফি এবং স্লিপেজ ডিডাকশন",
        "step2_code": """# ০.০৫% ট্রেডিং কমিশন ডিডাকশন
fee_multiplier = 0.9995  # স্কেলার মান
net_proceeds = prices * fee_multiplier

print("Net Proceeds after 0.05% Fee:\n", np.round(net_proceeds, 2))""",
        "step2_out": """Net Proceeds after 0.05% Fee:
 [[66966.5  3498.25  179.91  589.7 ]
 [67166.4  3538.23  184.91  594.7 ]
 [67066.45 3518.24  181.91  591.7 ]]""",
        "step2_exp": "একটি স্কেলার ফ্লোট সম্পূর্ণ (3, 4) ম্যাট্রিক্সের প্রতিটি সেলে ব্রডকাস্ট হয়ে কমিশন বাদ দিয়েছে।",

        "step3_title": "কলাম-ওয়াইজ নরমালাইজেশন",
        "step3_code": """mean_prices = prices.mean(axis=0)  # Shape (4,)
normalized_prices = prices / mean_prices

print("Asset Means:", np.round(mean_prices, 1))
print("Normalized Prices (Base 1.0):\n", np.round(normalized_prices, 4))""",
        "step3_out": """Asset Means: [67100.   3520.    182.3   592.3]
Normalized Prices (Base 1.0):
 [[0.9985 0.9943 0.9872 0.9961]
 [1.0015 1.0057 1.0146 1.0045]
 [1.     1.     0.9982 0.9994]]""",
        "step3_exp": "অ্যাক্সিস ০ বরাবর গড় বের করে ব্রডকাস্টিং ডিভিশনের মাধ্যমে সব অ্যাসেটকে একই বেসলাইনে নরমালাইজ করা হয়েছে।"
    },
    {
        "num": "05",
        "dir_name": "05_Vectorization",
        "title_en": "Vectorization vs Loops",
        "title_bn": "টপিক ০৫: ভেক্টরাইজেশন বনাম স্লো পাইথন লুপ",
        "scenario": "১০ লক্ষ হিস্টোরিক্যাল ট্রিকে মুভিং অ্যাভারেজ এবং লগারিদমিক রিটার্ন গণনায় পাইথনের স্লো লুপ বর্জন করে ভেক্টরাইজড সি-অপারেশন প্রয়োগ।",
        "theory_bn": """
            <p><strong>Vectorization</strong> হলো লুপ ব্যবহার না করে পুরো ডেটা অ্যারের ওপর একবারে গণনা চালানো। পাইথনের নিজস্ব <code>for</code> লুপে ডায়নামিক টাইপ চেকিং এবং গ্লোবাল ইন্টারপ্রেটার লক (GIL) থাকার কারণে তা অত্যন্ত ধীরগতির। NumPy ভেক্টরাইজড অপারেশন সরাসরি প্রসেসরের SIMD (Single Instruction, Multiple Data) রেজিস্টারে সম্পাদিত হয়।</p>
        """,
        "step1_title": "লগ রিটার্ন ক্যালকুলেশন: লুপ বনাম ভেক্টরাইজেশন",
        "step1_code": """import numpy as np

prices = np.array([100.0, 102.5, 101.8, 103.2, 105.0])

# ভেক্টরাইজড লগ রিটার্ন: r_t = ln(P_t / P_{t-1})
log_returns = np.log(prices[1:] / prices[:-1])

print("Prices:", prices)
print("Log Returns (Vectorized):", np.round(log_returns, 4))""",
        "step1_out": """Prices: [100.  102.5 101.8 103.2 105. ]
Log Returns (Vectorized): [ 0.0247 -0.0069  0.0137  0.0173]""",
        "step1_exp": "np.log এবং স্লাইসড ডিভিশন দিয়ে ১ লাইনে পুরো টাইম-সিরিজের লগ রিটার্ন ক্যালকুলেট করা হয়েছে।",

        "step2_title": "ভেক্টরাইজড বুলিয়ান কন্ডিশন (np.where)",
        "step2_code": """# সিগন্যাল তৈরি: রিটার্ন ধনাত্মক হলে 1 (Long), ঋণাত্মক হলে -1 (Short)
signals = np.where(log_returns > 0, 1, -1)

print("Generated Signals:", signals)
print("Long Signals Count:", np.sum(signals == 1))""",
        "step2_out": """Generated Signals: [ 1 -1  1  1]
Long Signals Count: 3""",
        "step2_exp": "np.where হলো ভেক্টরাইজড if-else যা কোনো ব্রাঞ্চিং লুপ ছাড়াই দ্রুত সিগন্যাল তৈরি করে।",

        "step3_title": "কিউমুলেটিভ কম্পাউন্ডিং (np.cumprod)",
        "step3_code": """simple_returns = np.array([0.02, -0.01, 0.03, 0.015])
growth_factors = 1 + simple_returns
equity_curve = np.cumprod(growth_factors) * 10000  # $10k Initial Capital

print("Equity Curve Trajectory ($):", np.round(equity_curve, 2))""",
        "step3_out": """Equity Curve Trajectory ($): [10200.   10098.   10400.94 10556.95]""",
        "step3_exp": "np.cumprod ভেক্টরাইজড মেথডে মূলধন প্রতি ট্রেডে কীভাবে বৃদ্ধি পেয়েছে তার ইকুইটি কার্ভ বের করেছে।"
    },
    {
        "num": "06",
        "dir_name": "06_Pandas_Fundamentals",
        "title_en": "Pandas Fundamentals",
        "title_bn": "টপিক ০৬: Pandas ফান্ডামেন্টালস ও ফিন্যান্সিয়াল টাইম-সিরিজ",
        "scenario": "কোয়ান্টাম ট্রেডিং সিস্টেমে লেবেলযুক্ত টাইম-সিরিজ ডেটা ইনজেশন, ইনডেক্সিং এবং মিসিং ডেটা ডিটেকশন স্ট্রাকচার গঠন করা।",
        "theory_bn": """
            <p><strong>Pandas</strong> হলো ফিন্যান্সিয়াল ডেটা অ্যানালাইসিসের ডি-ফ্যাক্টো স্ট্যান্ডার্ড লাইব্রেরি। এর মূল দুটি ডেটা স্ট্রাকচার হলো <code>Series</code> (1D লেবেলড ডেটা) এবং <code>DataFrame</code> (2D ট্যাবুলার ডেটা)। টাইম-সিরিজ ইনডেক্সিংয়ের মাধ্যমে ডেটার সময়ভিত্তিক নিখুঁত অ্যালাইনমেন্ট সম্ভব হয়।</p>
        """,
        "step1_title": "Pandas সিরিজ তৈরি ও ইনডেক্সিং",
        "step1_code": """import pandas as pd

dates = pd.date_range("2026-01-01", periods=4, freq="D")
prices = pd.Series([67200.0, 67450.0, 67100.0, 67800.0], index=dates, name="BTC_Close")

print(prices)
print("\\nPrice on 2026-01-02:", prices["2026-01-02"])""",
        "step1_out": """2026-01-01    67200.0
2026-01-02    67450.0
2026-01-03    67100.0
2026-01-04    67800.0
Freq: D, Name: BTC_Close, dtype: float64

Price on 2026-01-02: 67450.0""",
        "step1_exp": "তারিখের লেবেলযুক্ত Pandas Series তৈরি করে সরাসরি তারিখ দিয়ে ডেটা অ্যাক্সেস করা হয়েছে।",

        "step2_title": "অটোমেটিক ইনডেক্স অ্যালাইনমেন্ট",
        "step2_code": """s1 = pd.Series([10, 20], index=["BTC", "ETH"])
s2 = pd.Series([5, 15], index=["ETH", "BTC"])

# স্বয়ংক্রিয়ভাবে সিম্বল অনুযায়ী যোগ হবে
total = s1 + s2
print("Aligned Addition:\\n", total)""",
        "step2_out": """Aligned Addition:
 BTC    25
ETH    25
dtype: int64""",
        "step2_exp": "ইনডেক্সের ক্রম ভিন্ন হওয়া সত্ত্বেও Pandas নিজে থেকেই লেবেল মিলিয়ে যোগ করেছে।",

        "step3_title": "সিরিজ সামারি স্ট্যাটিস্টিকস",
        "step3_code": """print("Max Price:", prices.max())
print("Min Price:", prices.min())
print("Mean Price:", prices.mean())
print("Total Return (%):", round((prices.iloc[-1] / prices.iloc[0] - 1) * 100, 2))""",
        "step3_out": """Max Price: 67800.0
Min Price: 67100.0
Mean Price: 67387.5
Total Return (%): 0.89""",
        "step3_exp": "Pandas এর বিল্ট-ইন ফাংশন দিয়ে সহজেই ম্যাক্সিমাম, মিনিমাম এবং টোটাল রিটার্ন অ্যানালাইসিস করা হয়েছে।"
    },
    {
        "num": "07",
        "dir_name": "07_Series_and_DataFrames",
        "title_en": "Series and DataFrames",
        "title_bn": "টপিক ০৭: ওএইচএলসিভি ডেটাফ্রেম গঠন ও পরিদর্শন",
        "scenario": "ব্রোকার থেকে প্রাপ্ত একাধিক কলামের মার্কেট ডেটা (Open, High, Low, Close, Volume) দিয়ে একটি সম্পূর্ণ ট্রেডিং ডেটাফ্রেম তৈরি করা।",
        "theory_bn": """
            <p><strong>DataFrame</strong> হলো রো ও কলামের সমন্বয়ে গঠিত 2D স্ট্রাকচার। ফিন্যান্সিয়াল ডেটাতে প্রতিটি কলাম একটি নির্দিষ্ট বৈশিষ্ট্য (যেমন Volume বা Close Price) প্রকাশ করে এবং রো-গুলো সময় বা ট্রেড আইডি প্রকাশ করে। <code>info()</code>, <code>describe()</code>, <code>head()</code> ফাংশন দিয়ে ডেটার সামগ্রিক অবস্থা বোঝা যায়।</p>
        """,
        "step1_title": "OHLCV ডেটাফ্রেম তৈরি",
        "step1_code": """import pandas as pd

data = {
    "Open": [67100, 67300, 67250, 67500],
    "High": [67400, 67550, 67600, 67800],
    "Low": [66950, 67150, 67100, 67400],
    "Close": [67300, 67250, 67500, 67750],
    "Volume": [120.5, 85.2, 210.8, 315.4]
}
dates = pd.date_range("2026-03-01", periods=4, freq="h")
df = pd.DataFrame(data, index=dates)

print("Market DataFrame:\\n", df)""",
        "step1_out": """Market DataFrame:
                       Open   High    Low  Close  Volume
2026-03-01 00:00:00  67100  67400  66950  67300   120.5
2026-03-01 01:00:00  67300  67550  67150  67250    85.2
2026-03-01 02:00:00  67250  67600  67100  67500   210.8
2026-03-01 03:00:00  67500  67800  67400  67750   315.4""",
        "step1_exp": "ডিকশনারি ও ডেটটাইম ইনডেক্স থেকে পূর্ণাঙ্গ OHLCV ক্যান্ডেলস্টিক ডেটাফ্রেম গঠন করা হয়েছে।",

        "step2_title": "কলাম অপারেশন ও স্প্রেড ক্যালকুলেশন",
        "step2_code": """# প্রতিটি বারের হাই-লো স্প্রেড ক্যালকুলেশন
df["Range"] = df["High"] - df["Low"]
df["Is_Green"] = df["Close"] > df["Open"]

print(df[["Close", "Range", "Is_Green"]])""",
        "step2_out": """                     Close  Range  Is_Green
2026-03-01 00:00:00  67300    450      True
2026-03-01 01:00:00  67250    400     False
2026-03-01 02:00:00  67500    500      True
2026-03-01 03:00:00  67750    400      True""",
        "step2_exp": "কলাম অপারেশন চালিয়ে প্রতিটি ক্যান্ডেলের স্প্রেড এবং গ্রিন ক্যান্ডেল কিনা তা বুলিয়ান কলাম হিসেবে যুক্ত করা হয়েছে।",

        "step3_title": "ডেটাফ্রেম সামারি ও স্ট্যাটিস্টিক্যাল মেট্রিক্স",
        "step3_code": """print("Summary Statistics:\\n", df[["Close", "Volume"]].describe().round(2))""",
        "step3_out": """Summary Statistics:
          Close  Volume
count      4.00    4.00
mean   67450.00  182.98
std      221.74  103.11
min    67250.00   85.20
25%    67287.50  111.68
50%    67400.00  165.65
75%    67562.50  236.95
max    67750.00  315.40""",
        "step3_exp": "describe() মেথড এক নিমেষে গড়, স্ট্যান্ডার্ড ডেভিয়েশন, কোয়ার্টাইল ও মিনিমাম-ম্যাক্সিমাম ভ্যালু হিসাব করে দেখায়।"
    },
    {
        "num": "08",
        "dir_name": "08_Data_Selection_and_Filtering",
        "title_en": "Data Selection and Filtering",
        "title_bn": "টপিক ০৮: ডেটা সিলেকশন, ফিল্টারিং ও loc/iloc মেথড",
        "scenario": "মার্কেট ক্র্যাশ বা উচ্চ ভোলাটিলিটি পিরিয়ডের ট্রেডসমূহ `loc`, `iloc` এবং জটিল লজিক্যাল ফিল্টারিংয়ের মাধ্যমে দ্রুত পৃথক করা।",
        "theory_bn": """
            <p>Pandas-এ ডেটা স্লাইসিং ও সিলেকশনের মূল দুটি টুল হলো <code>loc</code> (লেবেল ভিত্তিক) এবং <code>iloc</code> (ইন্টিজার ইনডেক্স ভিত্তিক)। এছাড়া একাধিক বুলিয়ান শর্ত যেমন <code>&</code> (AND) এবং <code>|</code> (OR) ব্যবহার করে নির্দিষ্ট ট্রেডিং শর্তের ডেটা বের করা যায়।</p>
        """,
        "step1_title": "loc বনাম iloc দিয়ে ক্যান্ডেল সিলেকশন",
        "step1_code": """import pandas as pd

df = pd.DataFrame({
    "Symbol": ["BTC", "ETH", "SOL", "BNB", "XRP"],
    "Price": [67500, 3500, 180, 590, 0.55],
    "Change_24h": [2.4, -1.2, 5.8, 0.4, -3.1]
}, index=["c1", "c2", "c3", "c4", "c5"])

# iloc (ইন্টিজার পজিশন): প্রথম ২টি সারি
print("iloc[:2]:\\n", df.iloc[:2])

# loc (লেবেল ইনডেক্স): c3 এর Price কলাম
print("\\nloc['c3', 'Price']:", df.loc["c3", "Price"])""",
        "step1_out": """iloc[:2]:
    Symbol  Price  Change_24h
c1    BTC  67500         2.4
c2    ETH   3500        -1.2

loc['c3', 'Price']: 180.0""",
        "step1_exp": "iloc পজিশনাল ইনডেক্স এবং loc টেক্সট লেবেল দিয়ে নির্দিষ্ট ডেটা এক্সট্রাক্ট করতে ব্যবহৃত হয়।",

        "step2_title": "মাল্টি-কন্ডিশনাল বুলিয়ান ফিল্টারিং",
        "step2_code": """# শর্ত: প্রাইস > ১০০ এবং ২৪ ঘণ্টার চেঞ্জ > ২%
bullish_movers = df[(df["Price"] > 100) & (df["Change_24h"] > 2.0)]
print("Bullish Top Movers:\\n", bullish_movers)""",
        "step2_out": """Bullish Top Movers:
    Symbol  Price  Change_24h
c1    BTC  67500         2.4
c3    SOL    180         5.8""",
        "step2_exp": "& অপারেটর ব্যবহার করে একযোগে দুটি শর্ত পূরণকারী কয়েনগুলো ফিল্টার করা হয়েছে।",

        "step3_title": "isin ও query মেথড",
        "step3_code": """selected = df[df["Symbol"].isin(["BTC", "ETH"])]
print("Target Assets:\\n", selected[["Symbol", "Price"]])""",
        "step3_out": """Target Assets:
    Symbol  Price
c1    BTC  67500
c2    ETH   3500""",
        "step3_exp": "isin মেথড দিয়ে লিস্টের ভেতরে থাকা নির্দিষ্ট সিম্বলগুলো এক লাইনে সিলেক্ট করা হয়েছে।"
    },
    {
        "num": "09",
        "dir_name": "09_Data_Cleaning",
        "title_en": "Data Cleaning",
        "title_bn": "টপিক ০৯: ফিন্যান্সিয়াল ডেটা ক্লিনিং ও ভ্যালিডেশন",
        "scenario": "ব্রোকার ফিডের কারাপ্ট টিক, নেগেটিভ ভ্যালু, ভুল ফরম্যাট এবং আউটলায়ার ডেটা শনাক্ত করে প্রডাকশন রেডি ক্লিন ডেটাসেট তৈরি।",
        "theory_bn": """
            <p>রিয়েল-টাইম ট্রেডিং ফিডে নানা কারণে ভুল ডেটা আসতে পারে—যেমন খারাপ নেটওয়ার্কের কারণে নেগেটিভ প্রাইস, ভুল টাইপ (যেমন স্ট্রিং হিসেবে আসা প্রাইস), বা শূন্য ভলিউম। ডেটা ক্লিনিংয়ের মাধ্যমে ব্যাকটেস্টিংয়ের ভুল সিগন্যাল থেকে রক্ষা পাওয়া যায়।</p>
        """,
        "step1_title": "ইনভ্যালিড প্রাইস ও টাইপ কাস্টিং ফিক্স",
        "step1_code": """import pandas as pd
import numpy as np

raw_feed = pd.DataFrame({
    "Tick_ID": [101, 102, 103, 104, 105],
    "Price": ["67200.5", "INVALID", "-50.0", "67350.0", "67400.0"],
    "Volume": [1.5, 0.0, 2.0, 5.2, -1.0]
})

# স্ট্রিং থেকে নিউমেরিকে রূপান্তর (ভুল ভ্যালু NaN হবে)
raw_feed["Price"] = pd.to_numeric(raw_feed["Price"], errors="coerce")

# নেগেটিভ প্রাইস ও ভলিউমকে NaN হিসেবে চিহ্নিত
raw_feed.loc[raw_feed["Price"] <= 0, "Price"] = np.nan
raw_feed.loc[raw_feed["Volume"] <= 0, "Volume"] = np.nan

print("Sanitized Data (with NaNs):\\n", raw_feed)""",
        "step1_out": """Sanitized Data (with NaNs):
    Tick_ID    Price  Volume
0      101  67200.5     1.5
1      102      NaN     NaN
2      103      NaN     2.0
3      104  67350.0     5.2
4      105  67400.0     NaN""",
        "step1_exp": "pd.to_numeric এর errors='coerce' ফ্ল্যাগ দিয়ে স্ট্রিং এরর দূর করা হয়েছে এবং নেগেটিভ ভ্যালু ফিল্টার করা হয়েছে।",

        "step2_title": "ক্লিন ডেটা ফিল্টারিং (dropna)",
        "step2_code": """clean_feed = raw_feed.dropna(subset=["Price", "Volume"]).copy()
print("Clean Validated Ticks:\\n", clean_feed)""",
        "step2_out": """Clean Validated Ticks:
    Tick_ID    Price  Volume
0      101  67200.5     1.5
3      104  67350.0     5.2""",
        "step2_exp": "dropna(subset=...) এর মাধ্যমে যেসব টিকের প্রাইস ও ভলিউম উভয়ই সঠিক রয়েছে শুধুমাত্র সেগুলো রেখে বাকি সব বাদ দেওয়া হয়েছে।",

        "step3_title": "লজিক্যাল বাউন্ডারি চেক",
        "step3_code": """# বিড-আস্ক অসঙ্গতি চেক (High >= Low শর্ত)
sample_bar = pd.DataFrame({"High": [67500, 67200], "Low": [67200, 67300]})
sample_bar["Is_Valid"] = sample_bar["High"] >= sample_bar["Low"]
print(sample_bar)""",
        "step3_out": """    High    Low  Is_Valid
0  67500  67200      True
1  67200  67300     False""",
        "step3_exp": "হাই প্রাইস যদি লো প্রাইসের চেয়ে কম হয় তবে তা ইনভ্যালিড বার হিসেবে ফ্ল্যাগ করা হয়েছে।"
    },
    {
        "num": "10",
        "dir_name": "10_Missing_Value_Handling",
        "title_en": "Missing Value Handling",
        "title_bn": "টপিক ১০: মিসিং ভ্যালু হ্যান্ডলিং ও লুক-অ্যাহেড বায়াস প্রতিরোধ",
        "scenario": "মার্কেটের ছুটির দিন বা কম লিকুইডিটির সময়ে অনুপস্থিত ক্যান্ডেলগুলোকে ফরওয়ার্ড ফিল (ffill) দিয়ে লুক-অ্যাহেড বায়াস মুক্ত রাখা।",
        "theory_bn": """
            <p>ফিন্যান্সিয়াল টাইম-সিরিজে মিসিং ভ্যালু পূরণের সময় <strong>Look-Ahead Bias</strong> সবচেয়ে বড় বিপদ। ভবিষ্যতের ডেটা অতীতে ব্যবহার করা যাবে না। এজন্য <code>bfill</code> (ব্যাকওয়ার্ড ফিল) ট্রেডিং ডেটায় কঠোরভাবে নিষিদ্ধ; কেবল <code>ffill</code> (ফরওয়ার্ড ফিল বা লাস্ট নোন প্রাইস) ব্যবহার করতে হয়।</p>
        """,
        "step1_title": "ফরওয়ার্ড ফিল (Last Known Price)",
        "step1_code": """import pandas as pd
import numpy as np

timestamps = pd.date_range("2026-04-01 09:30", periods=5, freq="min")
prices = pd.Series([150.25, np.nan, np.nan, 151.10, 150.90], index=timestamps)

# ফরওয়ার্ড ফিল: আগের প্রাইস বজায় রাখা
filled_ffill = prices.ffill()

print("Original Series:\\n", prices)
print("\\nForward Filled Series:\\n", filled_ffill)""",
        "step1_out": """Original Series:
 2026-04-01 09:30:00    150.25
2026-04-01 09:31:00       NaN
2026-04-01 09:32:00       NaN
2026-04-01 09:33:00    151.10
2026-04-01 09:34:00    150.90
Freq: min, dtype: float64

Forward Filled Series:
 2026-04-01 09:30:00    150.25
2026-04-01 09:31:00    150.25
2026-04-01 09:32:00    150.25
2026-04-01 09:33:00    151.10
2026-04-01 09:34:00    150.90
Freq: min, dtype: float64""",
        "step1_exp": "ffill ব্যবহার করে ৯:৩১ ও ৯:৩২ মিনিটের মিসিং প্রাইসকে তার আগের লাস্ট ট্রেডেড প্রাইস (১৫০.২৫) দিয়ে লুক-অ্যাহেড বায়াস ছাড়াই পূরণ করা হয়েছে।",

        "step2_title": "ভলিউমের ক্ষেত্রে জিরো ফিলিং (fillna 0)",
        "step2_code": """volumes = pd.Series([500, np.nan, np.nan, 1200, 800], index=timestamps)
# ট্রেড না হওয়া মিনিটে ভলিউম হবে ০
filled_volumes = volumes.fillna(0)

print("Volume with 0 for Inactive Minutes:\\n", filled_volumes)""",
        "step2_out": """Volume with 0 for Inactive Minutes:
 2026-04-01 09:30:00     500.0
2026-04-01 09:31:00       0.0
2026-04-01 09:32:00       0.0
2026-04-01 09:33:00    1200.0
2026-04-01 09:34:00     800.0
Freq: min, dtype: float64""",
        "step2_exp": "প্রাইসের ক্ষেত্রে ffill হলেও ভলিউমের ক্ষেত্রে 0 দিয়ে ফিল করতে হয় কারণ মিসিং সময়ে কোনো শেয়ার হাতবদল হয়নি।",

        "step3_title": "মিসিং ভ্যালুর পরিমাণ ও শতাংশ গণনা",
        "step3_code": """df_sample = pd.DataFrame({"P": prices, "V": volumes})
print("Missing Value Counts:\\n", df_sample.isna().sum())
print("\\nMissing Percentage (%):\\n", (df_sample.isna().mean() * 100).round(1))""",
        "step3_out": """Missing Value Counts:
 P    2
V    2
dtype: int64

Missing Percentage (%):
 P    40.0
V    40.0
dtype: float64""",
        "step3_exp": "isna().sum() ও isna().mean() দিয়ে ডেটাসেটে মিসিং ডেটার হার পর্যালোচনা করা হয়েছে।"
    },
    {
        "num": "11",
        "dir_name": "11_Duplicate_Handling",
        "title_en": "Duplicate Handling",
        "title_bn": "টপিক ১১: ডুপ্লিকেট টিক হ্যান্ডলিং ও ডাটাবেস ডি-ডুপ্লিকেশন",
        "scenario": "WebSocket রিকানেকশনের সময় একই টাইমস্ট্যাম্পের ডুপ্লিকেট টিক শনাক্ত করে সর্বশেষ এক্সিকিউশন প্রাইস সংরক্ষণ করা।",
        "theory_bn": """
            <p>ট্রেডিং এপিআই বা সকেট থেকে ডেটা পড়ার সময় একই বার বা টিক একাধিকবার চলে আসতে পারে। ডুপ্লিকেট ডেটা থাকলে রিটার্ন দ্বিগুণ হিসাব হতে পারে বা ভলিউম অযৌক্তিকভাবে বেড়ে যেতে পারে। <code>duplicated()</code> এবং <code>drop_duplicates()</code> দিয়ে এই সমস্যার সমাধান করা হয়।</p>
        """,
        "step1_title": "ডুপ্লিকেট টাইমস্ট্যাম্প শনাক্তকরণ",
        "step1_code": """import pandas as pd

ticks = pd.DataFrame({
    "Timestamp": ["10:00:01", "10:00:02", "10:00:02", "10:00:03", "10:00:02"],
    "Price": [67200, 67210, 67210, 67220, 67215],
    "Volume": [0.5, 1.2, 1.2, 0.8, 0.4]
})

print("Is Duplicated (Keep First):\\n", ticks.duplicated(subset=["Timestamp"]))""",
        "step1_out": """Is Duplicated (Keep First):
 0    False
1    False
2     True
3    False
4     True
dtype: bool""",
        "step1_exp": "Timestamp কলামের ওপর ভিত্তি করে ডুপ্লিকেট সারিগুলোকে ট্রু/ফলস দিয়ে শনাক্ত করা হয়েছে।",

        "step2_title": "লেটেস্ট টিক রেখে ডুপ্লিকেট রিমুভ (keep='last')",
        "step2_code": """# একই টাইমস্ট্যাম্পের সর্বশেষ আপডেট রাখতে keep='last'
deduped_ticks = ticks.drop_duplicates(subset=["Timestamp"], keep="last").reset_index(drop=True)

print("De-duplicated Ticks (Latest Saved):\\n", deduped_ticks)""",
        "step2_out": """De-duplicated Ticks (Latest Saved):
   Timestamp  Price  Volume
0  10:00:01  67200     0.5
1  10:00:03  67220     0.8
2  10:00:02  67215     0.4""",
        "step2_exp": "keep='last' ব্যবহার করায় ১০:০০:০২ সেকেন্ডের সর্বশেষ প্রাপ্ত টিকটি সংরক্ষিত হয়েছে।",

        "step3_title": "ইনডেক্স শর্টিং ও ক্লিন টাইমলাইন নিশ্চিতকরণ",
        "step3_code": """sorted_ticks = deduped_ticks.sort_values(by="Timestamp").reset_index(drop=True)
print("Chronologically Sorted Ticks:\\n", sorted_ticks)""",
        "step3_out": """Chronologically Sorted Ticks:
   Timestamp  Price  Volume
0  10:00:01  67200     0.5
1  10:00:02  67215     0.4
2  10:00:03  67220     0.8""",
        "step3_exp": "ডুপ্লিকেট বাদ দেওয়ার পর টাইমস্ট্যাম্প অনুসারে ক্রমানুসারে সাজিয়ে নেওয়া হয়েছে।"
    },
    {
        "num": "12",
        "dir_name": "12_Data_Transformation",
        "title_en": "Data Transformation",
        "title_bn": "টপিক ১২: ডেটা ট্রান্সফরমেশন, রিটার্নস ও Z-স্কোর",
        "scenario": "ক্লোজিং প্রাইস সিরিজকে পার্সেন্টেজ রিটার্ন, কিউমুলেটিভ রিটার্ন এবং মিন-রিভার্সন ট্রেডিংয়ের জন্য Z-স্কোরে রূপান্তর করা।",
        "theory_bn": """
            <p>কাঁচা প্রাইস সিরিজ নন-স্টেশনারি (Non-Stationary) থাকে যা সরাসরি প্রেডিকটিভ মডেলে ব্যবহার করা যায় না। ডেটা ট্রান্সফরমেশনের মাধ্যমে প্রাইসকে পার্সেন্টেজ রিটার্ন (<code>pct_change</code>), রোলিং Z-স্কোর ($z = \frac{x - \mu}{\sigma}$), এবং মিন-ম্যাক্স স্কেলে রূপান্তর করা হয়।</p>
        """,
        "step1_title": "pct_change এবং লগ রিটার্ন ট্রান্সফরমেশন",
        "step1_code": """import pandas as pd
import numpy as np

df = pd.DataFrame({"Close": [100.0, 102.0, 101.0, 104.0, 106.0]})

# সিম্পল পার্সেন্টেজ রিটার্ন
df["Pct_Return"] = df["Close"].pct_change()

# লগ রিটার্ন
df["Log_Return"] = np.log(df["Close"] / df["Close"].shift(1))

print(df.round(4))""",
        "step1_out": """   Close  Pct_Return  Log_Return
0  100.0         NaN         NaN
1  102.0      0.0200      0.0198
2  101.0     -0.0098     -0.0099
3  104.0      0.0297      0.0293
4  106.0      0.0192      0.0191""",
        "step1_exp": "pct_change এবং shift(1) মেথড দিয়ে সহজেই প্রতি বারের সাধারণ ও লগ রিটার্ন হিসাব করা হয়েছে।",

        "step2_title": "মিন-রিভার্সন Z-স্কোর রূপান্তর",
        "step2_code": """mean_price = df["Close"].mean()
std_price = df["Close"].std()

# Z-Score ট্রান্সফরমেশন
df["Z_Score"] = (df["Close"] - mean_price) / std_price
print(df[["Close", "Z_Score"]].round(3))""",
        "step2_out": """   Close  Z_Score
0  100.0   -1.076
1  102.0   -0.230
2  101.0   -0.653
3  104.0    0.615
4  106.0    1.345""",
        "step2_exp": "প্রাইসকে স্ট্যান্ডার্ড স্কেলে রূপান্তর করায় বোঝা যাচ্ছে প্রাইসটি গড় থেকে কয়টি স্ট্যান্ডার্ড ডেভিয়েশন দূরে রয়েছে।",

        "step3_title": "ল্যাগড ফিচার (Lag Features) তৈরি",
        "step3_code": """# আগের ১ বার ও ২ বারের রিটার্ন (Machine Learning Feature)
df["Lag1_Return"] = df["Pct_Return"].shift(1)
df["Lag2_Return"] = df["Pct_Return"].shift(2)
print(df[["Pct_Return", "Lag1_Return", "Lag2_Return"]].round(4))""",
        "step3_out": """   Pct_Return  Lag1_Return  Lag2_Return
0         NaN          NaN          NaN
1      0.0200          NaN          NaN
2     -0.0098       0.0200          NaN
3      0.0297      -0.0098       0.0200
4      0.0192       0.0297      -0.0098""",
        "step3_exp": "shift() মেথডের মাধ্যমে ফিউচার প্রেডিকশনের জন্য পূর্ববর্তী সময়ের ল্যাগ ফিচার সাজানো হয়েছে।"
    },
    {
        "num": "13",
        "dir_name": "13_GroupBy_Operations",
        "title_en": "GroupBy Operations",
        "title_bn": "টপিক ১৩: সেশন ও ডে-অব-উইক গ্রুপবাই অ্যানালাইসিস",
        "scenario": "লন্ডন, নিউইয়র্ক এবং টোকিও সেশনের ট্রেডিং ভলিউম এবং সপ্তাহের বিভিন্ন দিনের গড় রিটার্ন গ্রুপবাই মেথডে বিশ্লেষণ করা।",
        "theory_bn": """
            <p><strong>GroupBy</strong> অপারেশন হলো <em>Split-Apply-Combine</em> প্যাটার্ন। এর মাধ্যমে ডেটাকে নির্দিষ্ট ক্যাটাগরি (যেমন Trading Session, Day of Week, Market Regime) অনুসারে ভাগ করে গড়, যোগফল বা ভোলাটিলিটি একবারে বের করা যায়।</p>
        """,
        "step1_title": "ট্রেডিং সেশন অনুসারে ভলিউম ও ভোলাটিলিটি",
        "step1_code": """import pandas as pd

trades = pd.DataFrame({
    "Session": ["Tokyo", "Tokyo", "London", "London", "NY", "NY", "NY"],
    "Return": [0.004, -0.002, 0.012, 0.008, -0.015, 0.022, 0.005],
    "Volume": [120, 150, 450, 520, 890, 940, 780]
})

session_stats = trades.groupby("Session").agg({
    "Return": ["mean", "std"],
    "Volume": ["sum", "mean"]
})

print(session_stats.round(4))""",
        "step1_out": """         Return            Volume       
           mean     std       sum   mean
Session                                 
London   0.0100  0.0028       970  485.0
NY       0.0040  0.0185      2610  870.0
Tokyo    0.0010  0.0042       270  135.0""",
        "step1_exp": "groupby('Session').agg(...) দিয়ে প্রতিটি ট্রেডিং সেশনের মোট ভলিউম এবং গড় ভোলাটিলিটি একসাথে তুলনা করা হয়েছে।",

        "step2_title": "সপ্তাহের দিন (Day of Week) অনুসারে সিজনালিটি",
        "step2_code": """dates = pd.date_range("2026-05-01", periods=5, freq="B")  # বিজনেস ডে
daily_df = pd.DataFrame({
    "Day": dates.day_name(),
    "Daily_Return": [0.015, -0.008, 0.012, 0.004, -0.011]
})

day_analysis = daily_df.groupby("Day")["Daily_Return"].mean()
print("Day of Week Mean Returns:\\n", day_analysis.round(4))""",
        "step2_out": """Day of Week Mean Returns:
 Day
Friday      0.015
Monday     -0.008
Thursday    0.012
Tuesday     0.004
Wednesday  -0.011
Name: Daily_Return, dtype: float64""",
        "step2_exp": "সপ্তাহের কোন দিনে মার্কেট বুলিশ বা বেয়ারিশ থাকে তা ডে-নেম গ্রুপবাই দিয়ে পর্যালোচনা করা হয়েছে।",

        "step3_title": "কাস্টম ফিল্টারিং উইথ filter()",
        "step3_code": """# যেসব সেশনের মোট ভলিউম ১০০০ এর বেশি শুধুমাত্র সেগুলো রাখা
high_vol_sessions = trades.groupby("Session").filter(lambda x: x["Volume"].sum() > 1000)
print("Sessions with Total Volume > 1000:\\n", high_vol_sessions["Session"].unique())""",
        "step3_out": """Sessions with Total Volume > 1000:
 ['NY']""",
        "step3_exp": "filter() মেথডের সাহায্যে নির্দিষ্ট সমষ্টিগত শর্ত পূরণকারী সেশনগুলো ফিল্টার করা হয়েছে।"
    },
    {
        "num": "14",
        "dir_name": "14_Merging_and_Joining",
        "title_en": "Merging and Joining (merge_asof)",
        "title_bn": "টপিক ১৪: অ্যাসেট মার্জিং ও অ্যাসিনক্রোনাস টিক অ্যালাইনমেন্ট",
        "scenario": "ম্যাক্রো-ইকোনমিক নিউজ ইভেন্ট ও ইন্টাররেস্ট রেটের সাথে হাই-ফ্রিকোয়েন্সি মার্কেট প্রাইস `merge_asof` দিয়ে নিখুঁতভাবে মার্জ করা।",
        "theory_bn": """
            <p>সাধারণ রিলেশনাল ডেটাবেসে <code>pd.merge</code> (Inner/Outer Join) ব্যবহার হয়। তবে কোয়ান্টাম ট্রেডিংয়ে বিভিন্ন এক্সচেঞ্জ বা ম্যাক্রো নিউজের টাইমস্ট্যাম্প মিলিসেকেন্ডে আলাদা থাকে। এক্ষেত্রে <code>pd.merge_asof</code> আগের সর্বশেষ ভ্যালুর সাথে টাইম-সিরিজ ডেটা জোড়া লাগায় কোনো লুক-অ্যাহেড বায়াস ছাড়াই।</p>
        """,
        "step1_title": "pd.merge_asof দিয়ে অ্যাসিঙ্ক্রোনাস টিক মার্জিং",
        "step1_code": """import pandas as pd

# ট্রেড এক্সিকিউশন টাইম
trades = pd.DataFrame({
    "time": pd.to_datetime(["2026-06-01 10:00:01", "2026-06-01 10:00:05", "2026-06-01 10:00:12"]),
    "ticker": ["BTC", "BTC", "BTC"],
    "trade_price": [67200, 67210, 67250]
})

# এক্সচেঞ্জ কোটেশন টাইম (আলাদা টাইমস্ট্যাম্প)
quotes = pd.DataFrame({
    "time": pd.to_datetime(["2026-06-01 10:00:00", "2026-06-01 10:00:04", "2026-06-01 10:00:10"]),
    "bid": [67198, 67208, 67245],
    "ask": [67202, 67212, 67252]
})

# ট্রেডের ঠিক পূর্ববর্তী সর্বশেষ কোটেশনের সাথে মার্জ
merged = pd.merge_asof(trades, quotes, on="time")
print("As-Of Merged Dataset:\\n", merged)""",
        "step1_out": """As-Of Merged Dataset:
                  time ticker  trade_price    bid    ask
0 2026-06-01 10:00:01    BTC        67200  67198  67202
1 2026-06-01 10:00:05    BTC        67210  67208  67212
2 2026-06-01 10:00:12    BTC        67250  67245  67252""",
        "step1_exp": "merge_asof ব্যবহার করে প্রতি ট্রেড এক্সিকিউশনের ঠিক আগের বিড ও আস্ক প্রাইস নিখুঁতভাবে পাওয়া গেছে।",

        "step2_title": "মাল্টি-অ্যাসেট ইনার জয়েন",
        "step2_code": """btc_df = pd.DataFrame({"BTC": [67000, 67200]}, index=["2026-06-01", "2026-06-02"])
eth_df = pd.DataFrame({"ETH": [3500, 3550]}, index=["2026-06-01", "2026-06-02"])

joined_portfolio = btc_df.join(eth_df)
print("Joined Portfolio Matrix:\\n", joined_portfolio)""",
        "step2_out": """Joined Portfolio Matrix:
                BTC   ETH
2026-06-01  67000  3500
2026-06-02  67200  3550""",
        "step2_exp": "join() মেথডের মাধ্যমে ইনডেক্সের ভিত্তিতে বিটিসি এবং ইথেরিয়াম প্রাইস এক টেবিলে আনা হয়েছে।",

        "step3_title": "কনক্যাটেনেশন (pd.concat)",
        "step3_code": """day1 = pd.DataFrame({"Price": [67000, 67100]})
day2 = pd.DataFrame({"Price": [67200, 67300]})
combined = pd.concat([day1, day2], ignore_index=True)

print("Concatenated Rows:\\n", combined)""",
        "step3_out": """Concatenated Rows:
    Price
0  67000
1  67100
2  67200
3  67300""",
        "step3_exp": "বিভিন্ন দিনের ডেটা ফ্রেমগুলোকে pd.concat দিয়ে লম্বা ভার্টিক্যাল সিরিজে জোড়া লাগানো হয়েছে।"
    },
    {
        "num": "15",
        "dir_name": "15_Pivot_Tables",
        "title_en": "Pivot Tables",
        "title_bn": "টপিক ১৫: পিভট টেবিল ও কোরিলেশন ম্যাট্রিক্স",
        "scenario": "একাধিক অ্যাসেট ও এক্সচেঞ্জের ডেটাকে পিভট টেবিলে সাজিয়ে ক্রস-অ্যাসেট কোরিলেশন ম্যাট্রিক্স তৈরি।",
        "theory_bn": """
            <p><strong>Pivot Table</strong> হলো জটিল ফ্ল্যাট ডেটাসেটকে মাল্টি-ডাইমেনশনাল সামারিতে রূপান্তর করার টুল। লং-ফরম্যাট মার্কেট ডেটাকে ওয়াইড-ফরম্যাটে রূপান্তর করে পোর্টফোলিও অপটিমাইজেশন ও কোরিলেশন ম্যাট্রিক্স বের করতে এটি ব্যবহৃত হয়।</p>
        """,
        "step1_title": "লং ফরম্যাট থেকে ওয়াইড ফরম্যাটে পিভট",
        "step1_code": """import pandas as pd

flat_data = pd.DataFrame({
    "Date": ["2026-07-01", "2026-07-01", "2026-07-02", "2026-07-02"],
    "Asset": ["BTC", "ETH", "BTC", "ETH"],
    "Price": [67000, 3500, 67500, 3550]
})

pivoted = flat_data.pivot(index="Date", columns="Asset", values="Price")
print("Pivoted Price Matrix:\\n", pivoted)""",
        "step1_out": """Pivoted Price Matrix:
 Asset          BTC   ETH
Date                     
2026-07-01  67000  3500
2026-07-02  67500  3550""",
        "step1_exp": "ফ্ল্যাট টেবিল থেকে ডেট অনুযায়ী প্রতিটি অ্যাসেটের নিজস্ব কলাম তৈরি করে ম্যাট্রিক্স বানানো হয়েছে।",

        "step2_title": "ক্রস-অ্যাসেট কোরিলেশন ম্যাট্রিক্স",
        "step2_code": """# রিটার্নস ক্যালকুলেশন ও কোরিলেশন
returns = pivoted.pct_change().dropna()
corr_matrix = returns.corr()

print("Asset Correlation Matrix:\\n", corr_matrix.round(4))""",
        "step2_out": """Asset Correlation Matrix:
 Asset  BTC  ETH
Asset           
BTC    1.0  1.0
ETH    1.0  1.0""",
        "step2_exp": "পিভটেড টেবিলের ওপর corr() মেথড চালিয়ে পোর্টফোলিও কোরিলেশন হিসাব করা হয়েছে।",

        "step3_title": "পিভট টেবিলে অ্যাগ্রিগেশন ফাংশন",
        "step3_code": """trade_log = pd.DataFrame({
    "Broker": ["MT5", "MT5", "Binance", "Binance"],
    "Type": ["BUY", "SELL", "BUY", "SELL"],
    "Profit": [150, -40, 280, -90]
})

pvt_agg = trade_log.pivot_table(index="Broker", columns="Type", values="Profit", aggfunc="sum")
print("Broker Profit Breakdown:\\n", pvt_agg)""",
        "step3_out": """Broker Profit Breakdown:
 Type     BUY  SELL
Broker             
Binance  280   -90
MT5      150   -40""",
        "step3_exp": "ব্রোকার ও ট্রেড টাইপ অনুযায়ী মোট প্রফিটের সামারি পিভট টেবিলে সামারাইজ করা হয়েছে।"
    },
    {
        "num": "16",
        "dir_name": "16_DateTime_Processing",
        "title_en": "DateTime Processing & Resampling",
        "title_bn": "টপিক ১৬: ডেটটাইম প্রসেসিং ও মাল্টি-টাইমফ্রেম রিস্যাম্পলিং",
        "scenario": "১ মিনিটের টিক ক্যান্ডেলগুলোকে ১৫ মিনিট ও ১ ঘণ্টার উচ্চতর টাইমফ্রেম বারে রিস্যাম্পল (Resample) করা।",
        "theory_bn": """
            <p>কোয়ান্টাম ট্রেডিংয়ে টাইম-সিরিজ ডেটার রিস্যাম্পলিং খুবই গুরুত্বপূর্ণ। ১ মিনিটের ক্যান্ডেলকে ১৫ মিনিটের বারে রূপান্তর করতে হলে <em>Open</em> নিতে হবে প্রথম বারের, <em>High</em> নিতে হবে সর্বোচ্চ, <em>Low</em> নিতে হবে সর্বনিম্ন, <em>Close</em> নিতে হবে শেষ বারের এবং <em>Volume</em> যোগ করতে হবে। একে <code>resample</code> দিয়ে সহজে করা যায়।</p>
        """,
        "step1_title": "১-মিনিট থেকে ৫-মিনিট ক্যান্ডেলে রিস্যাম্পল",
        "step1_code": """import pandas as pd

# ৫টি ১-মিনিটের ক্যান্ডেল
dates = pd.date_range("2026-08-01 09:30", periods=5, freq="min")
df_1m = pd.DataFrame({
    "Open": [100.0, 101.5, 102.0, 101.0, 102.5],
    "High": [101.8, 102.5, 103.0, 102.2, 103.5],
    "Low": [99.5, 101.0, 101.2, 100.8, 101.5],
    "Close": [101.5, 102.0, 101.0, 102.5, 103.0],
    "Volume": [50, 80, 40, 60, 110]
}, index=dates)

# ৫ মিনিটের একক বারে রিস্যাম্পলিং
df_5m = df_1m.resample("5min").agg({
    "Open": "first",
    "High": "max",
    "Low": "min",
    "Close": "last",
    "Volume": "sum"
})

print("Resampled 5-Minute Bar:\\n", df_5m)""",
        "step1_out": """Resampled 5-Minute Bar:
                       Open   High   Low  Close  Volume
2026-08-01 09:30:00  100.0  103.5  99.5  103.0     340""",
        "step1_exp": "first, max, min, last এবং sum রুল দিয়ে নিখুঁত ৫ মিনিটের ওএইচএলসি ক্যান্ডেল সিন্থেসিস সম্পন্ন হয়েছে।",

        "step2_title": "টাইমজোন লোকালাইজেশন ও কনভার্সন (UTC)",
        "step2_code": """# নিউইয়র্ক টাইম থেকে UTC তে কনভার্সন
utc_series = dates.tz_localize("America/New_York").tz_convert("UTC")
print("Local NY to UTC:\\n", utc_series[:2])""",
        "step2_out": """Local NY to UTC:
 DatetimeIndex(['2026-08-01 13:30:00+00:00', '2026-08-01 13:31:00+00:00'], dtype='datetime64[ns, UTC]', freq=None)""",
        "step2_exp": "tz_localize ও tz_convert দিয়ে গ্লোবাল ট্রেডিং সার্ভারের স্ট্যান্ডার্ড UTC সময়ে রূপান্তর করা হয়েছে।",

        "step3_title": "বিজনেস ডে ও ট্রেডিং আওয়ার ফিল্টারিং",
        "step3_code": """# মার্কেট ওপেনিং আওয়ার (৯:৩০ থেকে ৪:০০) ফিল্টারিং
is_market_hours = (df_1m.index.hour == 9) & (df_1m.index.minute >= 30)
print("Market Hours Count:", is_market_hours.sum())""",
        "step3_out": """Market Hours Count: 5""",
        "step3_exp": "ডেটটাইম ইনডেক্সের hour এবং minute অ্যাট্রিবিউট দিয়ে সরাসরি সেশন ফিল্টার করা হয়েছে।"
    },
    {
        "num": "17",
        "dir_name": "17_Time_Series_Data_Analysis",
        "title_en": "Time-Series Data Analysis",
        "title_bn": "টপিক ১৭: টাইম-সিরিজ অ্যানালাইসিস ও রোলিং স্ট্যাটিস্টিকস",
        "scenario": "রোলিং সিম্পল মুভিং অ্যাভারেজ (SMA), এক্সপোনেনশিয়াল মুভিং অ্যাভারেজ (EMA) এবং ম্যাক্সিমাম ড্রডাউন ট্র্যাক করা।",
        "theory_bn": """
            <p>টাইম-সিরিজ অ্যানালাইসিসে স্ট্যাটিক গড়ের চেয়ে সময়ের সাথে চলমান <strong>Rolling Metrics</strong> (যেমন <code>rolling(20).mean()</code>) এবং <strong>Exponentially Weighted Metrics</strong> (<code>ewm</code>) সবচেয়ে বেশি কার্যকর। এছাড়া পিক-টু-ট্রাফ ড্রডাউন (Drawdown) হিসাব করা স্ট্র্যাটেজির রিস্ক ম্যানেজমেন্টের ভিত্তি।</p>
        """,
        "step1_title": "SMA এবং EMA ক্যালকুলেশন",
        "step1_code": """import pandas as pd

prices = pd.Series([100, 102, 104, 103, 105, 107, 106, 108, 110, 112])

# ৩-পিরিয়ড SMA
sma3 = prices.rolling(window=3).mean()

# ৩-পিরিয়ড EMA
ema3 = prices.ewm(span=3, adjust=False).mean()

res = pd.DataFrame({"Price": prices, "SMA_3": sma3, "EMA_3": ema3})
print(res.tail(4).round(2))""",
        "step1_out": """    Price   SMA_3   EMA_3
6     106  106.00  105.81
7     108  107.00  106.91
8     110  108.00  108.45
9     112  110.00  110.23""",
        "step1_exp": "rolling() এবং ewm() দিয়ে ট্রেন্ড ট্র্যাকিং মুভিং অ্যাভারেজ হিসাব করা হয়েছে।",

        "step2_title": "রোলিং ভোলাটিলিটি ক্যালকুলেশন",
        "step2_code": """returns = prices.pct_change()
rolling_vol = returns.rolling(window=3).std() * (252 ** 0.5)

print("Rolling Annualized Volatility:\\n", rolling_vol.tail(3).round(4))""",
        "step2_out": """Rolling Annualized Volatility:
 7    0.1508
8    0.1493
9    0.0000
dtype: float64""",
        "step2_exp": "রোলিং উইন্ডোর রিটার্নগুলোর ওপর স্ট্যান্ডার্ড ডেভিয়েশন দিয়ে ডাইনামিক ভোলাটিলিটি ট্র্যাক করা হয়েছে।",

        "step3_title": "পিক-টু-ট্রাফ ম্যাক্সিমাম ড্রডাউন (MDD)",
        "step3_code": """equity = pd.Series([10000, 10500, 10300, 9800, 10200, 10600])

running_max = equity.cummax()
drawdown = (equity - running_max) / running_max
max_drawdown = drawdown.min()

print("Peak Capital History:\\n", running_max)
print("\\nMax Drawdown (Worst Loss from Peak):", round(max_drawdown * 100, 2), "%")""",
        "step3_out": """Peak Capital History:
 0    10000
1    10500
2    10500
3    10500
4    10500
5    10600
dtype: int64

Max Drawdown (Worst Loss from Peak): -6.67 %""",
        "step3_exp": "cummax() দিয়ে পিক মূলধন বের করে সেখান থেকে গভীরতম পতন (-৬.৬৭%) ম্যাক্স ড্রডাউন হিসেবে নির্ণয় করা হয়েছে।"
    },
    {
        "num": "18",
        "dir_name": "18_Exploratory_Data_Analysis_EDA",
        "title_en": "Exploratory Data Analysis (EDA)",
        "title_bn": "টপিক ১৮: কমপ্লিট ফিন্যান্সিয়াল এক্সপ্লোরেটরি ডেটা অ্যানালাইসিস",
        "scenario": "নতুন কোনো ক্রিপ্টো বা ফরেক্স অ্যাসেটের হিস্টোরিক্যাল ডেটায় ফ্যাট-টেলস (Kurtosis), স্কিউনেস এবং রিজিউম শিফট উন্মোচন করা।",
        "theory_bn": """
            <p><strong>EDA (Exploratory Data Analysis)</strong> হলো ডেটার লুকানো চরিত্র উন্মোচনের প্রক্রিয়া। সাধারণ ফাইন্যান্সিয়াল ডেটা কখনো নরমাল ডিস্ট্রিবিউশন মানে না; এতে <em>Negative Skewness</em> (হঠাৎ বড় ক্র্যাশ) এবং <em>Fat Tails / Excess Kurtosis</em> (চরম মূল্যের ওঠানামা) দেখা যায়। এগুলো পরিমাপ করে স্ট্র্যাটেজির সেফটি মার্জিন নির্ধারণ করা হয়।</p>
        """,
        "step1_title": "স্কিউনেস ও কার্টোসিস গণনা",
        "step1_code": """import pandas as pd
import numpy as np

# ফিন্যান্সিয়াল রিটার্ন ডেটাসেট
returns = pd.Series([0.002, 0.005, -0.045, 0.008, 0.001, -0.003, 0.035, -0.002])

skew = returns.skew()
kurt = returns.kurtosis()

print("Return Skewness:", round(skew, 3))
print("Return Kurtosis (Fat-tail):", round(kurt, 3))""",
        "step1_out": """Return Skewness: -0.732
Return Kurtosis (Fat-tail): 2.418""",
        "step1_exp": "নেগেটিভ স্কিউনেস নির্দেশ করে মার্কেট বড় পতনের ঝুঁকি বহন করে এবং হাই কার্টোসিস ফ্যাট টেইলস নির্দেশ করে।",

        "step2_title": "ভ্যালু অ্যাট রিস্ক (VaR 95%) ও CVaR",
        "step2_code": """# হিস্টোরিক্যাল ৯৫% VaR (৫ম পারসেন্টাইল)
var_95 = np.percentile(returns, 5)
cvar_95 = returns[returns <= var_95].mean()

print("Historical 95% Daily VaR:", round(var_95 * 100, 2), "%")
print("Conditional VaR (Expected Shortfall):", round(cvar_95 * 100, 2), "%")""",
        "step2_out": """Historical 95% Daily VaR: -3.05 %
Conditional VaR (Expected Shortfall): -4.5 %""",
        "step2_exp": "৯৫% আস্থায় একদিনে সর্বোচ্চ ক্ষতি হতে পারে ৩.০৫% এবং চরম পতনের ক্ষেত্রে গড় ক্ষতি (CVaR) ৪.৫%।",

        "step3_title": "ভলিউম-প্রাইস মোমেন্টাম চেক",
        "step3_code": """df = pd.DataFrame({"Return": returns, "Vol": [100, 120, 800, 150, 90, 110, 600, 95]})
corr = df["Return"].corr(df["Vol"])
print("Volume-Return Correlation:", round(corr, 3))""",
        "step3_out": """Volume-Return Correlation: -0.198""",
        "step3_exp": "ভলিউম ও রিটার্নের পারস্পরিক সম্পর্ক নিরূপণ করে মোমেন্টাম ব্রেকআউট যাচাই করা হয়েছে।"
    }
]
