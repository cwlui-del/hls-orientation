import streamlit as st
import pandas as pd

# 1. 網頁基本設定（手機版優化）
st.set_page_config(
    page_title="HLS Orientation Day 2026",
    page_icon="🔬",
    layout="centered"
)

# 2. 健康與生命科學系專屬視覺風格 (Mint Green & Medical Blue)
st.markdown("""
    <style>
    .main-title { font-size: 26px; font-weight: bold; color: #007A87; text-align: center; margin-bottom: 20px; }
    .sub-title { font-size: 16px; color: #555555; text-align: center; margin-bottom: 25px; }
    .card { background-color: #F0F9F8; padding: 15px; border-radius: 10px; border-left: 5px solid #00A896; margin-bottom: 15px; }
    .time-tag { font-weight: bold; color: #007A87; }
    .venue-tag { background-color: #E2F0D9; padding: 2px 8px; border-radius: 5px; font-size: 14px; color: #385723; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. 頂部標題與系徽設計
st.markdown('<div class="main-title">🔬 Department of Health & Life Sciences</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Welcome Orientation Day 2026-27 指南 App</div>', unsafe_allow_html=True)

# 4. 讀取剛才上傳的 CSV 資料
try:
    df = pd.read_csv("schedule.csv")
    
    # 5. 新生互動篩選器（下拉選單）
    st.markdown("### 🔍 查詢你的專屬日程")
    programme_list = ["全部日程 (Show All)"] + list(df["課程/學系 (Target)"].unique())
    selected_prog = st.selectbox("請選擇你的課程/班別：", programme_list)
    
    # 根據選擇篩選資料
    if selected_prog != "全部日程 (Show All)":
        filtered_df = df[df["課程/學系 (Target)"] == selected_prog]
    else:
        filtered_df = df

    # 6. 渲染日程卡片（極致適合手機閱讀）
    st.markdown("### 📅 當日時間線 (Timeline)")
    for index, row in filtered_df.iterrows():
        st.markdown(f"""
        <div class="card">
            <span class="time-tag">⏱️ {row['時間 (Time)']}</span> &nbsp;&nbsp; 
            <span class="venue-tag">📍 {row['地點 (Venue)']}</span>
            <h4 style="margin-top: 8px; margin-bottom: 5px; color:#111;">{row['活動名稱 (Title)']}</h4>
            <p style="font-size: 14px; color:#444; margin-bottom: 5px;">{str(row['活動重點摘要 (Details)']).replace('<br>', '<br>')}</p>
            <small style="color:#888;">💡 備註: {row['重要備註 (Remarks)'] if pd.notna(row['重要備註 (Remarks)']) else '無'}</small>
        </div>
        """, unsafe_allow_html=True)

except Exception as e:
    st.error("資料加載失敗，請檢查 schedule.csv 檔案是否存在。")

# 7. 底部重要公告與惡劣天氣安排
st.markdown("---")
st.markdown("### ⚠️ 緊急通知與惡劣天氣安排")
with st.expander("☔ 查看打風 / 暴雨取消指引"):
    st.write("若當天早上 6:15 或之前發出紅雨/黑雨警告或八號風球，活動將取消並順延至 8月28日 (09:00-11:00) 在原定教室舉行。")

with st.expander("📞 缺席處理與健康及生命科學學系聯絡"):
    st.write("無法出席者請務必瀏覽新生資訊網頁 (https://www.vtc.edu.hk/st/orientation)，及檢查學生電郵 (https://webmail.vtc.edu.hk )收取學系最新資訊。有疑問可致電健康及生命科學學系：2256 7100。")
