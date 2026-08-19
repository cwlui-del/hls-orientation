import streamlit as st
import pandas as pd

# 1. 網頁基本設定
st.set_page_config(
    page_title="HLS Orientation Day 2026",
    page_icon="🔬",
    layout="centered"
)

# 2. 視覺風格增加按鈕與地圖美化
st.markdown("""
    <style>
    .main-title { font-size: 24px; font-weight: bold; color: #007A87; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size: 15px; color: #666666; text-align: center; margin-bottom: 25px; font-weight: 500; }
    .card { background-color: #F0F9F8; padding: 16px; border-radius: 12px; border-left: 6px solid #00A896; margin-bottom: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }
    .time-tag { font-weight: bold; color: #007A87; font-size: 15px; }
    .venue-tag { background-color: #E2F0D9; padding: 3px 10px; border-radius: 6px; font-size: 13px; color: #385723; font-weight: bold; float: right; }
    .remarks-tag { background-color: #FFF2CC; padding: 2px 6px; border-radius: 4px; font-size: 12px; color: #D6B656; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🔬 Dept of Health & Life Sciences</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Orientation Day 2026-27 新生導航 App</div>', unsafe_allow_html=True)

# 3. 完整日程資料（新增了「地圖網址」欄位，請把下方的網址替換成你們自己畫的圖）
orientation_data = {
    "課程/學系 (Target)": [
        "全體 (HD & DFS)", "全體 (HD & DFS)", 
        "AS114205 (生物醫學)", "AS114103 (分析科學)", 
        "AS110114 (環境管理)", "AS114109 (樹木管理-Eng)", 
        "AS114109J (樹木管理-粵)", "FS113002A (基礎文憑)"
    ],
    "活動名稱 (Title)": [
        "集合與報到 (Assembly)", "院系迎新大會 (Departmental Orientation)", 
        "課程導向 (Programme Orientation)", "課程導向 (Programme Orientation)", 
        "課程導向 (Programme Orientation)", "課程導向 (Programme Orientation)", 
        "課程導向 (Programme Orientation)", "課程導向第一階段 (DFS Orientation P1)"
    ],
    "時間 (Time)": [
        "09:15 - 09:30", "09:30 - 10:20", 
        "10:30 - 12:30", "10:30 - 12:30", 
        "10:30 - 12:30", "10:30 - 12:30", 
        "10:30 - 12:30", "10:30 - 11:15"
    ],
    "地點 (Venue)": [
        "禮堂 (Hall)", "禮堂 (Hall)", 
        "030 室", "Annex Hall", 
        "118B 室", "208B 室", 
        "207B 室", "禮堂 (Hall)"
    ],
    "活動重點摘要 (Details)": [
        "歡迎各位新生！迎新日活動正式開始，請各位移步至禮堂集合。解讀校園第一步，請先安坐。",
        "1. 院長及系主任致歡迎辭<br>2. 校園支援資訊與基礎設施講座<br>3. HLS IVElite 計劃介紹及學生會招募。所有高級文憑及基礎文憑新生均需參與。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構與時間表介紹、學分豁免申請<br>3. <b>現場派發學生證 (Student ID Card)</b>（本場為英文班專場）。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構與時間表介紹、學分豁免申請<br>3. <b>現場派發學生證 (Student ID Card)</b>（本場為廣東話班專場）。",
        "基礎文憑（健康與生命科學學群）全體說明會。介紹基礎課程大綱、校園適應。本階段結束後，將根據個別班別進行分流教室導航。"
    ],
    "重要備註 (Remarks)": [
        "核心活動，請勿遲到", "所有新生必須出席", 
        "生物醫學系專屬", "分析科學系專屬", 
        "環境管理系專屬", "樹木管理英文班", 
        "樹木管理廣東話班", "稍後需進行分流"
    ],
    # 💡 這裡貼上你們製作的路線圖圖片網址。以下先用免費的 placeholder 示意圖代替，上線前改掉即可
    "地圖網址 (MapUrl)": [
        "https://github.com/cwlui-del/hls-orientation/blob/main/GF.png?raw=true", 
        "https://github.com/cwlui-del/hls-orientation/blob/main/1F.png?raw=true", 
        "https://github.com/cwlui-del/hls-orientation/blob/main/2F.png?raw=true"
    ]
}
df = pd.DataFrame(orientation_data)

# 4. 新生互動互動篩選器
st.markdown("### 🔍 查詢你的專屬日程")
programme_list = ["顯示全日所有活動 (Show All)"] + list(df["課程/學系 (Target)"].unique())
selected_prog = st.selectbox("請選擇你入讀的課程 / 班別：", programme_list)

if selected_prog != "顯示全日所有活動 (Show All)":
    filtered_df = df[df["課程/學系 (Target)"] == selected_prog]
    general_df = df[df["課程/學系 (Target)"] == "全體 (HD & DFS)"]
    filtered_df = pd.concat([general_df, filtered_df]).drop_duplicates()
else:
    filtered_df = df

# 5. 渲染日程卡片與動態路線圖按鈕
st.markdown("### 📅 當日活動時間線 (Timeline)")

for index, row in filtered_df.iterrows():
    # 建立外殼卡片
    st.markdown(f"""
    <div class="card">
        <span class="venue-tag">📍 {row['地點 (Venue)']}</span>
        <span class="time-tag">⏱️ {row['時間 (Time)']}</span>
        <h4 style="margin-top: 10px; margin-bottom: 8px; color:#005A66; font-size:17px;">{row['活動名稱 (Title)']}</h4>
        <p style="font-size: 14px; color:#333333; line-height:1.5; margin-bottom: 8px;">{row['活動重點摘要 (Details)']}</p>
        <span class="remarks-tag">💡 {row['重要備註 (Remarks)']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 💡 在卡片下方新增一個專屬的 Streamlit 免費按鈕，點擊就展開該地點的路線圖
    with st.expander(f"🗺️ 點擊查看前往【{row['地點 (Venue)']}】的路線圖指引"):
        st.image(row['地圖網址 (MapUrl)'], use_container_width=True, caption=f"從學校正門前往 {row['地點 (Venue)']} 路線圖")

# 6. DFS 基礎文憑分流教室地圖
if selected_prog == "顯示全日所有活動 (Show All)" or "基礎文憑" in selected_prog:
    st.info("💡 **DFS 基礎文憑新生注意：**\n\n在 11:15 完結第一階段後，請根據你的班別前往以下分流教室：\n* **1A, 1E, 1G 班** ➡️ 前往 **118A 室**\n* **1B, 1F 班** ➡️ 前往 **104 室**\n* **1C, 1D, 1H 班** ➡️ 留在 **禮堂 (Hall)**")

# 7. 底部重要公告與總地圖
st.markdown("---")
st.markdown("### ⚠️ 緊急通知與聯絡資訊")
with st.expander("☔ 查看颱風 / 暴雨取消及延期指引"):
    st.warning("若當天早上 6:15 或之前發出紅雨/黑雨警告或八號或以上烈風信號，當日活動將全部取消，並順延至 8月28日 (09:00-11:00) 在原定教室舉行。")
