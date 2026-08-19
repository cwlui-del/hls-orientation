import streamlit as st
import pandas as pd

# 1. 網頁基本設定
st.set_page_config(
    page_title="HLS Orientation Day 2026",
    page_icon="🔬",
    layout="centered"
)

# 2. 視覺風格（含手機卡片、地圖、以及全新表單按鈕美化）
st.markdown("""
    <style>
    .main-title { font-size: 24px; font-weight: bold; color: #007A87; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size: 15px; color: #666666; text-align: center; margin-bottom: 25px; font-weight: 500; }
    .card { background-color: #F0F9F8; padding: 16px; border-radius: 12px; border-left: 6px solid #00A896; margin-bottom: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }
    .time-tag { font-weight: bold; color: #007A87; font-size: 15px; }
    .venue-tag { background-color: #E2F0D9; padding: 3px 10px; border-radius: 6px; font-size: 13px; color: #385723; font-weight: bold; float: right; }
    .remarks-tag { background-color: #FFF2CC; padding: 2px 6px; border-radius: 4px; font-size: 12px; color: #D6B656; font-weight: bold; }
    .map-box { width: 100%; border-radius: 8px; margin-top: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    
    /* 📝 表單專屬手機優化樣式 */
    .form-section { background-color: #F9F9F9; border: 1px dashed #007A87; padding: 15px; border-radius: 10px; margin-bottom: 20px; }
    .form-btn { display: block; text-align: center; background-color: #007A87; color: white !important; font-weight: bold; padding: 12px; border-radius: 8px; text-decoration: none; margin-top: 10px; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .form-btn:hover { background-color: #005A66; text-decoration: none; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🔬 Dept of Health & Life Sciences</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Orientation Day 2026-27 新生導航 App</div>', unsafe_allow_html=True)

# 3. 日程資料庫
orientation_data = {
    "課程": [
        "全體 (HD & DFS)", "全體 (HD & DFS)", 
        "AS110114 (可持續發展及環境管理高級文憑（科目組）)", "AS114103 (化驗科學高級文憑)", 
        "AS114109 (保育及樹木管理高級文憑)", "AS114109J (保育及樹木管理高級文憑（授課語言：中文（廣東話））)", 
        "AS114205 (生物醫學高級文憑)", "FS113002A (基礎課程文憑)"
    ],
    "活動名稱 (Title)": [
        "集合 (Assembly)", "學系迎新會 (Departmental Orientation)", 
        "AS110114課程迎新會 (Programme Orientation)", "AS114103課程迎新會 (Programme Orientation)", 
        "AS114109課程迎新會 (Programme Orientation)", "AS114109J課程迎新會 (Programme Orientation)", 
        "AS114205課程迎新會 (Programme Orientation)", "FS113002A課程迎新會第一階段 (DFS Orientation P1)"
    ],
    "時間 (Time)": [
        "09:15 - 09:30", "09:30 - 10:20", 
        "10:30 - 12:30", "10:30 - 12:30", 
        "10:30 - 12:30", "10:30 - 12:30", 
        "10:30 - 12:30", "10:30 - 11:15"
    ],
    "地點 (Venue)": [
        "禮堂 (Hall)", "禮堂 (Hall)", 
        "118B 室", "新翼禮堂", 
        "208B 室", "207B 室", 
        "030 室", "禮堂 (Hall)"
    ],
    "活動重點摘要 (Details)": [
        "歡迎各位新生！迎新日活動正式開始，請各位移步至禮堂集合。解讀校園第一步，請先安坐。",
        "1. 院長及系主任致歡迎辭<br>2. 校園支援資訊與基礎設施講座<br>3. HLS IVElite 計劃介紹及學生會招募。所有高級文憑及基礎文憑新生均需參與。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。</b>（本場為英文班專場）。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。</b>（本場為廣東話班專場）。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。",
        "基礎課程文憑（健康與生命科學）全體說明會。介紹基礎課程大綱、校園適應。本階段結束後，將根據個別班別進行分流。"
    ],
    "重要備註 (Remarks)": [
        "核心活動，請勿遲到", "所有新生必須出席", 
        "可持續發展及環境管理高級文憑（科目組）專屬", "化驗科學高級文憑專屬", 
        "保育及樹木管理高級文憑專屬", "保育及樹木管理高級文憑（授課語言：中文（廣東話））專屬", 
        "生物醫學高級文憑專屬", "稍後需進行分流"
    ],
    # 💡 請把下方的圖片網址，替換成你們自己在 GitHub 或是圖床上的真實路線圖連結
    "地圖網址 (MapUrl)": [
        "https://github.com/cwlui-del/hls-orientation/blob/main/Hall.png?raw=true", 
        "https://github.com/cwlui-del/hls-orientation/blob/main/Hall.png?raw=true",
        "https://github.com/cwlui-del/hls-orientation/blob/main/1F.png?raw=true", 
        "https://github.com/cwlui-del/hls-orientation/blob/main/Annex%20Hall.png?raw=true",
        "https://github.com/cwlui-del/hls-orientation/blob/main/2F.png?raw=true", 
        "https://github.com/cwlui-del/hls-orientation/blob/main/2F.png?raw=true",
        "https://github.com/cwlui-del/hls-orientation/blob/main/GF.png?raw=true", 
        "https://github.com/cwlui-del/hls-orientation/blob/main/Hall.png?raw=true"
    ]
}

df = pd.DataFrame(orientation_data)

# 4. 新生互動互動篩選器
st.markdown("### 🔍 查詢你的專屬日程")
programme_list = ["顯示全日所有活動 (Show All)"] + list(df["課程"].unique())
selected_prog = st.selectbox("請選擇你入讀的課程：", programme_list)

# 📝 5. 採用 100% 安全的 Streamlit 官方原生元件進行表單分流
st.markdown("### 📋 新生必填網上表格 (Online Forms)")

if "AS" in selected_prog:
    # 只要選單文字包含 AS 字頭
    st.info("💡 **高級文憑課程新生請注意：**\n\n請點擊下方按鈕，於今日內在網上填妥並提交以下兩份高級文憑專屬表格：")
    
    # 官方安全連結按鈕一
    st.link_button(
        "📝 1. 線上填寫：學生出席率要求和操行及紀律同意書", 
        "https://forms.cloud.microsoft/Pages/ShareFormPage.aspx?id=qwXbfulCSEO4kyumJaNQxowMOY0lU-xGgk44FFyRACRUNjhQMlVUU0haWVJVQUc4OTY5TFZWUEI2OS4u&sharetoken=Vr72GmTA7i5TsElwJmZT",
        use_container_width=True
    )
    
    # 官方安全連結按鈕二
    st.link_button(
        "🔬 2. 線上填寫：實驗室安全回條", 
        "https://forms.cloud.microsoft/Pages/ShareFormPage.aspx?id=qwXbfulCSEO4kyumJaNQxowMOY0lU-xGgk44FFyRACRUOFpVUzgyT05ROTZWNEZDMkNMMzZPNTFaTi4u&sharetoken=Fjhj6vHhmnciXJ3QpjOo",
        use_container_width=True
    )

elif "FS" in selected_prog:
    # 只要選單文字包含 FS 字頭
    st.info("💡 **基礎課程文憑新生請注意：**\n\n請點擊下方按鈕，於今日內在網上填妥並提交以下兩份基礎課程文憑專屬表格：")
    
    # 官方安全連結按鈕一
    st.link_button(
        "📝 1. 線上填寫：學生出席率要求和操行及紀律同意書 (DFS)", 
        "https://forms.cloud.microsoft/Pages/ShareFormPage.aspx?id=qwXbfulCSEO4kyumJaNQxowMOY0lU-xGgk44FFyRACRUMUEySDROSzUyRVA4RFdGSkJLUjhQQTgwTy4u&sharetoken=fXfweBOhGmYfznYAeXvB",
        use_container_width=True
    )
    
    # 官方安全連結按鈕二
    st.link_button(
        "🔬 2. 線上填寫：實驗室安全回條 (FS113002A)", 
        "https://forms.cloud.microsoft/Pages/ShareFormPage.aspx?id=qwXbfulCSEO4kyumJaNQxowMOY0lU-xGgk44FFyRACRURVRPUVk1Vko3N08yVDdUVTNZRExVNVNQWi4u&sharetoken=Fjhj6vHhmnciXJ3QpjOo",
        use_container_width=True
    )

else:
    # 預設狀態或「顯示全日所有活動」時的提示
    st.warning("💡 請先在上方下拉選單選擇你的【入讀課程 / 班別】，系統會自動為你生成需要填寫的網上表格連結。")

# 6. 篩選日程邏輯
if selected_prog != "顯示全日所有活動 (Show All)":
    filtered_df = df[df["課程"] == selected_prog]
    general_df = df[df["課程"] == "全體 (HD & DFS)"]
    filtered_df = pd.concat([general_df, filtered_df]).drop_duplicates()
else:
    filtered_df = df

# 5. 渲染日程與摺疊地圖
st.markdown("### 📅 當日活動時間線 (Timeline)")

for index, row in filtered_df.iterrows():
    st.markdown(f"""
    <div class="card">
        <span class="venue-tag">📍 {row['地點 (Venue)']}</span>
        <span class="time-tag">⏱️ {row['時間 (Time)']}</span>
        <h4 style="margin-top: 10px; margin-bottom: 8px; color:#005A66; font-size:17px;">{row['活動名稱 (Title)']}</h4>
        <p style="font-size: 14px; color:#333333; line-height:1.5; margin-bottom: 8px;">{row['活動重點摘要 (Details)']}</p>
        <span class="remarks-tag">💡 {row['重要備註 (Remarks)']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 💡 改用安全的 HTML Markdown 注入地圖，徹底免除 st.image 的參數相容報錯
    with st.expander(f"🗺️ 查看【{row['地點 (Venue)']}】的位置"):
        st.markdown(f"""
            <p style='font-size:13px; color:#666;'>指引：請留意地點前往。</p>
            <img src='{row['地圖網址 (MapUrl)']}' class='map-box' alt='地圖'>
        """, unsafe_allow_html=True)

# 6. DFS 基礎文憑分流提示
if selected_prog == "顯示全日所有活動 (Show All)" or "基礎課程文憑" in selected_prog:
    st.info("💡 **DFS 基礎課程文憑新生注意：**\n\n在 11:15 完結第一階段後，請根據你的班別前往以下分流教室：\n* **1A, 1E, 1G 班** ➡️ 前往 **118A 室**\n* **1B, 1F 班** ➡️ 前往 **104 室**\n* **1C, 1D, 1H 班** ➡️ 留在 **禮堂 (Hall)**")

# 7. 底部重要公告與總地圖
st.markdown("---")
st.markdown("### 🗺️ 校園樓層分佈圖 (General Map)")
with st.expander("🏢 點擊展開查看校園樓層指南"):
    st.markdown("""
        <img src='https://github.com/cwlui-del/hls-orientation/blob/main/GF.png?raw=true' class='map-box' alt='校園指南G/F'>
        <img src='https://github.com/cwlui-del/hls-orientation/blob/main/1F.png?raw=true' class='map-box' alt='校園指南1/F'>
        <img src='https://github.com/cwlui-del/hls-orientation/blob/main/2F.png?raw=true' class='map-box' alt='校園指南2/F'>
        <img src='https://github.com/cwlui-del/hls-orientation/blob/main/3F.png?raw=true' class='map-box' alt='校園指南3/F'>
        <img src='https://github.com/cwlui-del/hls-orientation/blob/main/4F.png?raw=true' class='map-box' alt='校園指南4/F'>
        <img src='https://github.com/cwlui-del/hls-orientation/blob/main/5F.png?raw=true' class='map-box' alt='校園指南5/F'>
    """, unsafe_allow_html=True)

st.markdown("### ⚠️ 緊急通知與聯絡資訊")
with st.expander("☔ 查看颱風 / 暴雨取消及延期指引"):
    st.warning("若當天早上 6:15 或之前發出紅雨/黑雨警告或八號或以上烈風信號，當日活動將全部取消，並順延至 8月28日 (09:00-11:00) 在原定教室舉行。")

with st.expander("📞 缺席處理與學系聯絡"):
    st.write("當天因病或其他緊急原因無法出席者，請務必瀏覽**新生資訊網站(https://www.vtc.edu.hk/st/orientation)** 或登入 **學生 Webmail(https://webmail.vtc.edu.hk )** 查看後續補領學生證與教學大綱的安排。")
    st.write("如有任何疑問，可於辦公時間致電學系查詢：")
    st.markdown("- **電話：** 2256 7100 / 2256 7156 / 2256 7158")
