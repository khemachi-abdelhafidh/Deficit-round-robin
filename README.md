# 🏆 محاكاة خوارزمية Deficit Round Robin باستخدام Python 🐍
- 🔹 واجهة رسومية تفاعلية لمحاكاة جدولة الحزم باستخدام خوارزمية DRR.
- 🔹 أدخل أوقات وصول الحزم لكل طابور (A, B, C) وشاهد كيف يتم توزيعها عبر الجدولة العادلة!
- 🔹 حدد قيمة DC 💡 ثم تابع تنفيذ الخوارزمية خطوة بخطوة.
- 🔹 عرض مرئي ديناميكي 🖥️ للبيانات مع إمكانية إضافة أعمدة وتحليل النتائج بسهولة.
# ✨ Deficit Round Robin Algorithm Simulation in Python 🐍

## 📌 Overview
- 🔹 Interactive GUI to simulate packet scheduling using the Deficit Round Robin (DRR) Algorithm.
- 🔹 Enter packet arrival times for each queue (A, B, C) and watch how they are fairly scheduled!
- 🔹 Set the Deficit Counter (DC) value 💡 and observe step-by-step execution.
- 🔹 Dynamic visualization 🖥️ with the ability to add columns and analyze results easily.

## 🚀 How to Use
- 1️⃣ Run the script.
- 2️⃣ Enter arrival times for packets in queues (A, B, C).
- 3️⃣ Set the Deficit Counter (DC) value.
- 4️⃣ Click Apply to run the simulation.


<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
        }

        .gallery {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            width: 80%;
            max-width: 1200px;
        }

        .figure {
            text-align: center;
            width: 32%;
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .figure:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }

        .figure img {
            width: 100%;
            height: auto;
            border-bottom: 2px solid #eee;
            transition: opacity 0.3s ease;
        }

        .figure:hover img {
            opacity: 0.85;
        }

        .caption {
            font-size: 16px;
            color: #333;
            padding: 10px;
            font-weight: bold;
            background-color: #fff;
        }
    </style>
    <title>Image Gallery</title>
</head>
<body>
    <div class="gallery">
        <figure class="figure">
            <img src="https://github.com/user-attachments/assets/12b54508-fc21-4cbb-ba93-dd3ece4075a5" alt="Capture" />
            <figcaption class="caption">Caption 1</figcaption>
        </figure>

        <figure class="figure">
            <img src="https://github.com/user-attachments/assets/73a37bd3-92f9-4106-b2d9-80e0fa978123" alt="Capture1" />
            <figcaption class="caption">Caption 2</figcaption>
        </figure>

        <figure class="figure">
            <img src="https://github.com/user-attachments/assets/760a2828-bd0b-4d7b-a280-70e8bac5fbf7" alt="Capture3" />
            <figcaption class="caption">Caption 3</figcaption>
        </figure>
    </div>
</body>
</html>



