import streamlit as st
import pandas as pd
from src.cleaner import (
    remove_duplicates,
    fill_missing,
    drop_missing,
    standardize_text,
    convert_types,
    filter_outliers_iqr,
    rename_columns,
)
from src.utils import CLEANING_METHODS, TEXT_OPERATIONS
from src.exporter import to_csv_bytes


def _fb(msg: str, icon: str = "✅") -> None:
    st.session_state["_fb_msg"] = msg
    st.session_state["_fb_icon"] = icon


def render_clean() -> None:
    df = st.session_state.df
    original = st.session_state.get("df_original", df)
    log = st.session_state.setdefault("cleaning_log", [])

    fb_msg = st.session_state.pop("_fb_msg", None)
    fb_icon = st.session_state.pop("_fb_icon", "✅")
    if fb_msg:
        st.toast(fb_msg, icon=fb_icon)
        st.success(f"{fb_icon} {fb_msg}")

    st.markdown(
        "<div class='section-header'>🧹 Clean Your Data</div>",
        unsafe_allow_html=True,
    )

    # ── Working stats ──
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.metric("Rows", f"{len(df):,}")
    with col_s2:
        st.metric("Columns", len(df.columns))
    with col_s3:
        removed = len(original) - len(df)
        st.metric("Rows Removed", f"{removed:,}" if removed > 0 else "—")

    if removed > 0:
        st.info(f"⚠️ {removed:,} rows have been removed by cleaning operations.")

    # ── Remove Duplicates ──
    with st.container(border=True):
        st.markdown(
            "<div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;'>"
            "<span style='font-size:1.2rem;'>🔁</span>"
            "<span style='font-size:0.95rem; font-weight:700; color:var(--text);'>"
            "Remove Duplicates</span></div>",
            unsafe_allow_html=True,
        )
        dup_cols = st.multiselect(
            "Columns to check (leave empty for all columns)",
            options=df.columns.tolist(),
            key="dup_cols",
        )
        dup_subset = dup_cols if dup_cols else None
        if st.button("Remove Duplicates", type="primary", key="btn_dup"):
            new_df = remove_duplicates(df, subset=dup_subset)
            dup_removed = len(df) - len(new_df)
            if dup_removed > 0:
                st.session_state.df = new_df
                log.append(
                    f"Removed {dup_removed:,} duplicate rows{' on selected columns' if dup_cols else ''}"
                )
                _fb(f"Removed {dup_removed:,} duplicate rows!")
                st.rerun()
            else:
                _fb("No duplicates found.", "ℹ️")
                st.rerun()

    # ── Handle Missing Values ──
    with st.container(border=True):
        st.markdown(
            "<div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;'>"
            "<span style='font-size:1.2rem;'>❓</span>"
            "<span style='font-size:0.95rem; font-weight:700; color:var(--text);'>"
            "Handle Missing Values</span></div>",
            unsafe_allow_html=True,
        )
        strategy = st.selectbox(
            "Strategy",
            options=list(CLEANING_METHODS.keys()),
            format_func=lambda k: CLEANING_METHODS[k],
            key="miss_strategy",
        )
        miss_cols = st.multiselect(
            "Apply to columns (leave empty for all columns)",
            options=df.columns.tolist(),
            key="miss_cols",
        )
        fill_val = None
        if strategy == "value":
            fill_val = st.text_input(
                "Fill with value:",
                key="fill_val",
                placeholder="e.g. N/A, 0, Unknown...",
            )
        miss_subset = miss_cols if miss_cols else None

        if st.button("Apply Missing Value Fix", type="primary", key="btn_miss"):
            if strategy == "drop":
                new_df = drop_missing(df, columns=miss_subset)
                dropped = len(df) - len(new_df)
                st.session_state.df = new_df
                log.append(f"Dropped {dropped:,} rows with missing values")
                _fb(f"Dropped {dropped:,} rows!")
                st.rerun()
            elif strategy == "value":
                if not fill_val:
                    _fb("Enter a value to fill with.", "⚠️")
                    st.rerun()
                new_df = fill_missing(
                    df, strategy="value", columns=miss_subset, fill_value=fill_val
                )
                st.session_state.df = new_df
                log.append(f"Filled missing values with '{fill_val}'")
                _fb(f"Filled with '{fill_val}'!")
                st.rerun()
            else:
                if strategy in ("mean", "median") and miss_subset:
                    non_numeric = [
                        c
                        for c in miss_subset
                        if not pd.api.types.is_numeric_dtype(df[c])
                    ]
                    if non_numeric:
                        _fb(
                            f"Skipped non-numeric: {', '.join(non_numeric)}. Use 'mode' or 'value'.",
                            "⚠️",
                        )
                        filtered_cols = [c for c in miss_subset if c not in non_numeric]
                        if not filtered_cols:
                            st.rerun()
                        miss_subset = filtered_cols
                new_df = fill_missing(df, strategy=strategy, columns=miss_subset)
                st.session_state.df = new_df
                log.append(f"Applied '{strategy}' filling to missing values")
                _fb(f"Filled using {CLEANING_METHODS[strategy]}!")
                st.rerun()

    # ── Standardize Text ──
    with st.container(border=True):
        st.markdown(
            "<div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;'>"
            "<span style='font-size:1.2rem;'>✏️</span>"
            "<span style='font-size:0.95rem; font-weight:700; color:var(--text);'>"
            "Standardize Text</span></div>",
            unsafe_allow_html=True,
        )
        text_cols = st.multiselect(
            "Text columns to standardize",
            options=df.select_dtypes(include="object").columns.tolist(),
            key="text_cols",
        )
        if text_cols:
            t1, t2 = st.columns(2)
            with t1:
                do_strip = st.checkbox("Strip whitespace", value=True, key="t_strip")
                do_lower = st.checkbox("Convert to lowercase", key="t_lower")
                do_upper = st.checkbox("Convert to UPPERCASE", key="t_upper")
            with t2:
                do_title = st.checkbox("Convert to Title Case", key="t_title")
                do_special = st.checkbox("Remove special characters", key="t_special")
            find_text = st.text_input(
                "Find (optional):", key="t_find", placeholder="Text to find..."
            )
            replace_text = st.text_input(
                "Replace with:", key="t_replace", placeholder="Replacement text..."
            )
            fr_pair = (find_text, replace_text) if find_text else None

            if st.button("Apply Text Standardization", type="primary", key="btn_text"):
                new_df = standardize_text(
                    df,
                    columns=text_cols,
                    strip=do_strip,
                    lowercase=do_lower,
                    uppercase=do_upper,
                    title_case=do_title,
                    remove_special=do_special,
                    find_replace=fr_pair,
                )
                st.session_state.df = new_df
                log_details = []
                if do_strip:
                    log_details.append("stripped")
                if do_lower:
                    log_details.append("lowercase")
                if do_upper:
                    log_details.append("UPPERCASE")
                if do_title:
                    log_details.append("Title Case")
                if do_special:
                    log_details.append("no special chars")
                if fr_pair:
                    log_details.append(f"replace '{find_text}'")
                log_text = ", ".join(log_details) if log_details else "standardized"
                log.append(
                    f"Text standardized in {len(text_cols)} columns ({log_text})"
                )
                _fb(f"Text standardized ({len(text_cols)} cols)!")
                st.rerun()

    # ── Convert Data Types ──
    with st.container(border=True):
        st.markdown(
            "<div style='display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;'>"
            "<span style='font-size:1.2rem;'>🔄</span>"
            "<span style='font-size:0.95rem; font-weight:700; color:var(--text);'>"
            "Convert Data Types</span></div>",
            unsafe_allow_html=True,
        )
        type_options = ["int64", "float64", "string", "datetime64[ns]", "category"]
        type_map = {}
        tcols = st.columns(2)
        for i, col in enumerate(df.columns):
            with tcols[i % 2]:
                chosen = st.selectbox(
                    f"{col} ({df[col].dtype})",
                    options=["— keep as is —"] + type_options,
                    key=f"type_{col}",
                )
                if chosen and chosen != "— keep as is —":
                    type_map[col] = chosen
        if type_map and st.button(
            "Apply Type Conversions", type="primary", key="btn_types"
        ):
            new_df = convert_types(df, type_map)
            st.session_state.df = new_df
            log.append(f"Converted types for {len(type_map)} columns")
            _fb(f"Types converted ({len(type_map)} cols)!")
            st.rerun()

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("⬅ Back to Issues", use_container_width=True):
            st.session_state.page = "issues"
            st.rerun()
    with c2:
        if st.button("📥 Export", use_container_width=True, type="primary"):
            st.session_state.page = "export"
            st.rerun()
    with c3:
        if st.button("↩ Reset to Original", use_container_width=True):
            st.session_state.df = original.copy()
            st.session_state.cleaning_log = []
            _fb("Data reset to original!")
            st.rerun()
