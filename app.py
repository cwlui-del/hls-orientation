import streamlit as st
import pandas as pd

# 1. 網頁基本設定（針對手機版進行極致優化）
st.set_page_config(
    page_title="HLS Orientation Day 2026",
    page_icon="🔬",
    layout="centered"
)

# 2. 健康與生命科學系（HLS）專屬薄荷綠與醫學藍視覺 Style
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

# 3. 頂部橫幅與學系標題
st.markdown('<div class="main-title">🔬 Dept of Health & Life Sciences</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Orientation Day 2026-27 新生導航 App</div>', unsafe_allow_html=True)

# 4. 直接將 PDF 的完整日程資料寫入 Python 字典中（免除讀取 CSV 失敗的風險）
orientation_data = {
    "課程/學系 (Target)": [
        "全體 (HD & DFS)", "全體 (HD & DFS)", 
        "AS114205 (生物醫學高級文憑)", "AS114103 (化驗科學高級文憑)", 
        "AS110114 (可持續發展及環境管理高級文憑（科目組）)", "AS114109 (保育及樹木管理高級文憑)", 
        "AS114109J (保育及樹木管理高級文憑（授課語言：中文（廣東話））)", "FS113002A (基礎課程文憑)"
    ],
    "活動名稱 (Title)": [
        "集合 (Assembly)", "學系迎新會 (Departmental Orientation)", 
        "AS110114課程導向 (Programme Orientation)", "AS114103課程導向 (Programme Orientation)", 
        "AS114109課程導向 (Programme Orientation)", "AS114109J課程導向 (Programme Orientation)", 
        "AS114205課程導向 (Programme Orientation)", "FS113002A課程導向第一階段 (DFS Orientation P1)"
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
        "1. 院長及系主任致歡迎辭<br>2. 校園支援資訊與基礎設施講座<br>3. HLS IVElite 計劃介紹及學生會（Student Association）招募。所有高級文憑及基礎文憑新生均需參與。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構詳細介紹、班級時間表、學分豁免申請說明<br>3. <b>現場派發學生證 (Student ID Card)</b><br>4. 校園生活適應與學生支援服務諮詢。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構與時間表介紹、學分豁免申請<br>3. <b>現場派發學生證 (Student ID Card)</b>（本場為英文班專場）。",
        "1. 班主任見面與簡報 (Class tutor briefing)<br>2. 課程結構與時間表介紹、學分豁免申請<br>3. <b>現場派發學生證 (Student ID Card)</b>（本場為廣東話班專場）。",
        "基礎文憑（健康與生命科學學群）全體說明會。介紹基礎課程大綱、校園適應。本階段結束後，將根據個別班別進行分流教室導航。"
    ],
    "重要備註 (Remarks)": [
        "核心活動，請勿遲到", "所有新生必須出席", 
        "生物醫學高級文憑專屬", "化驗科學高級文憑專屬", 
        "可持續發展及環境管理高級文憑（科目組）專屬", "保育及樹木管理高級文憑專屬", 
        "保育及樹木管理高級文憑（授課語言：中文（廣東話））專屬", "稍後需進行分流"
    ]
}

# 轉化為 Pandas DataFrame 方便進行一鍵篩選
df = pd.DataFrame(orientation_data)

# 5. 新生互動互動篩選器（下拉選單）
st.markdown("### 🔍 查詢你的專屬日程")
programme_list = ["顯示全日所有活動 (Show All)"] + list(df["課程/學系 (Target)"].unique())
selected_prog = st.selectbox("請選擇你入讀的課程 / 班別：", programme_list)

# 根據新生的選擇，動態過濾不相關的資訊
if selected_prog != "顯示全日所有活動 (Show All)":
    filtered_df = df[df["課程/學系 (Target)"] == selected_prog]
    # 自動幫選了個別學系的學生，在最頂部疊加全體都要參加的早上大會
    general_df = df[df["課程/學系 (Target)"] == "全體 (HD & DFS)"]
    filtered_df = pd.concat([general_df, filtered_df]).drop_duplicates()
else:
    filtered_df = df

# 6. 渲染日程卡片（極致適合手機單手滑動閱讀）
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

# 7. 針對基礎文憑（DFS）新生的專屬點對點分流提示
if selected_prog == "顯示全日所有活動 (Show All)" or "基礎課程文憑" in selected_prog:
    st.info("💡 **DFS 基礎課程文憑新生注意：**\n\n在 11:15 完結第一階段後，請根據你的班別前往以下分流教室：\n* **1A, 1E, 1G 班** ➡️ 前往 **118A 室**\n* **1B, 1F 班** ➡️ 前往 **104 室**\n* **1C, 1D, 1H 班** ➡️ 留在 **禮堂 (Hall)**")

# 8. 底部重要公告與惡劣天氣安排（防呆摺疊面板）
st.markdown("---")
st.markdown("### ⚠️ 緊急通知與聯絡資訊")

with st.expander("☔ 查看颱風 / 暴雨取消及延期指引"):
    st.warning("若當天早上 6:15 或之前發出**紅色/黑色暴雨警告**或**八號或以上烈風信號**，當日活動將全部取消，並順延至 **8月28日 (09:00-11:00)** 在原定教室舉行。")

with st.expander("📞 缺席處理與學系秘書處聯絡"):
    st.write("當天因病或其他緊急原因無法出席者，請務必瀏覽**新生資訊網站https://www.vtc.edu.hk/st/orientation**或登入 **學生 Webmail https://webmail.vtc.edu.hk** 收取學系最新資訊。")
    st.write("如有任何疑問，可於辦公時間致電健康及生命科學學系查詢：")
    st.markdown("- **電話：** 2256 7100 / 2256 7156 / 2256 7158")
