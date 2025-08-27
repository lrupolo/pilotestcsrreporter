import streamlit as st
import pandas as pd
import requests
import io

# Set page config
st.set_page_config(page_title="CSV Uploader · Region Selector", layout="centered")

st.title("CSV Uploader & Region Selector")

# --- Sidebar or header options
st.markdown("Upload a CSV file, select region, preview and send to the webhook.")

# --- File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

regions = ["anz", "korea", "mena", "japan", "china"]
region = st.selectbox("Select region", options=[""] + regions, format_func=lambda x: "— Choose a region —" if x == "" else x)

# --- State management
if "df" not in st.session_state:
    st.session_state.df = None
if "parse_error" not in st.session_state:
    st.session_state.parse_error = ""

# --- Parse CSV
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        # Drop fully empty rows
        df = df.dropna(how="all")
        st.session_state.df = df
        st.session_state.parse_error = ""
    except Exception as e:
        st.session_state.df = None
        st.session_state.parse_error = f"Parse error: {str(e)}"

# --- Status pill
if uploaded_file is not None:
    st.success(f"Selected file: {uploaded_file.name}")
else:
    st.info("No file selected.")

# --- Error message
if st.session_state.parse_error:
    st.error(st.session_state.parse_error)

# --- Show preview
if st.session_state.df is not None and st.session_state.df.shape[0] > 0:
    st.markdown("#### Preview")
    st.write(
        f"Rows: {st.session_state.df.shape[0]:,} · Columns: {st.session_state.df.shape[1]} · Delimiter: \",\""
    )
    st.dataframe(st.session_state.df.head(100))
elif uploaded_file is not None and not st.session_state.parse_error:
    st.warning("No rows found in this CSV.")

# --- Send to webhook
WEBHOOK = "https://corp-dev-aiplatform-n8n.data.ea.com/webhook/b89ebd73-ae38-46ff-9f8d-c66b2bed6ab1"

def send_to_webhook(df, region, filename):
    # Prepare rows
    rows = df.fillna("").to_dict(orient="records")
    # Add region to each row
    for r in rows:
        r["region"] = region
    payload = {
        "rows": rows,
        "meta": {
            "filename": filename or "upload.csv",
            "columns": list(df.columns) + ["region"],
            "delimiter": ","
        }
    }
    try:
        r = requests.post(WEBHOOK, json=payload, timeout=10)
        r.raise_for_status()
        return True, f"Sent {len(rows)} JSON rows to n8n ✅"
    except Exception as e:
        return False, f"Error sending to webhook: {str(e)}"

btn_disabled = st.session_state.df is None or not region
if st.button("Generate Sentiment Summary", disabled=btn_disabled):
    if not region:
        st.error("Select a region.")
    elif st.session_state.df is None or st.session_state.df.shape[0] == 0:
        st.error("No data to send.")
    else:
        with st.spinner("Sending data to webhook..."):
            success, msg = send_to_webhook(st.session_state.df, region.strip().lower(), uploaded_file.name if uploaded_file else None)
        if success:
            st.success(msg)
        else:
            st.error(msg)

st.markdown(
    "<span style='font-size:12px; color:#9fb0c0'>Your data stays in the browser unless you click <em>Generate Sentiment Summary</em>, which will POST parsed JSON rows (with region) to the hard‑coded webhook.</span>",
    unsafe_allow_html=True,
)
