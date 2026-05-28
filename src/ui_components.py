import streamlit as st


def load_css(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)


def render_circle_metric(title, value, color, status):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="circle" style="--value:{value}; --color:{color};">
                <span>{value}%</span>
            </div>
            <div class="metric-status">{status}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_skill_chips(items, chip_type="matched"):
    if not items:
        st.write("None found.")
        return

    chip_class = "skill-chip" if chip_type == "matched" else "missing-chip"
    html = ""

    for item in items:
        html += f'<span class="{chip_class}">{item}</span>'

    st.markdown(html, unsafe_allow_html=True)


def render_recommendations(recommendations):
    for rec in recommendations:
        st.markdown(
            f"""
            <div class="recommendation">
                💡 {rec}
            </div>
            """,
            unsafe_allow_html=True
        )