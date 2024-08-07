import re
import streamlit as st
import pandas as pd
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal, LTChar, LAParams
import matplotlib.pyplot as plt


# st.set_page_config(page_title="Resume Analyzer", page_icon="☑️")

# Function to extract text and styles from PDF
def extract_text_and_styles(pdf_file):
    elements = []
    for page_layout in extract_pages(pdf_file, laparams=LAParams()):
        for element in page_layout:
            if isinstance(element, LTTextBoxHorizontal):
                for text_line in element:
                    if isinstance(text_line, LTTextLineHorizontal):
                        text = text_line.get_text()
                        text = re.sub(r'^[\s\d\W]+', '', text)  # Remove bullets, numbers, and leading whitespace
                        if not text:
                            continue
                        text = re.sub(r'[^\w\s]', '', text)  # Remove all special characters
                        font = None
                        size = None
                        bold = False
                        for character in text_line:
                            if isinstance(character, LTChar):
                                font = character.fontname
                                size = round(character.size)  # Take integer value of the font size
                                bold = 'Bold' in character.fontname or 'bold' in character.fontname
                                break  # Use the first character's font and size as representative
                        elements.append({
                            "text": text.strip(),
                            "font": font,
                            "size": size,
                            "bold": bold,
                            "x0": text_line.x0,
                            "x1": text_line.x1,
                            "y0": text_line.y0,
                            "y1": text_line.y1,
                        })
    return pd.DataFrame(elements)

# Function to determine the border width of the text
def determine_border_width(elements, page_width, page_height):
    left_border = min(elements['x0'])
    right_border = page_width - max(elements['x1'])
    top_border = page_height - max(elements['y1'])
    bottom_border = min(elements['y0'])

    border_widths = {
        "left_border": (left_border, left_border / 72),
        "right_border": (right_border, right_border / 72),
        "top_border": (top_border, top_border / 72),
        "bottom_border": (bottom_border, bottom_border / 72)
    }
    return border_widths

# Function to check font style and size for normal text
def check_normal_text(elements):
    standard_fonts = ["TimesNewRomanPSMT", "TimesNewRomanPS-BoldMT","SymbolMT"]
    standard_size_range = range(11, 15)  # Font size between 11 and 12 (inclusive)
    total_elements = 0
    matching_elements = 0
    mismatches = []

    for _, element in elements.iterrows():
        if element['size'] in standard_size_range and element['font'] in standard_fonts:
            matching_elements += 1
        else:
            mismatch_detail = f"{element['text']} (font: {element['font']}, size: {element['size']}, bold: {element['bold']})"
            mismatches.append(mismatch_detail)
        total_elements += 1

    match_percentage = (matching_elements / total_elements) * 100 if total_elements > 0 else 0
    return match_percentage, mismatches

# Streamlit UI
st.title("Resume Analyzer")

st.header("Upload Your PDF Resume")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Extract elements from the PDF
    elements = extract_text_and_styles(uploaded_file)

    # Assuming an A4 page size (8.27 x 11.69 inches), convert to points (1 inch = 72 points)
    page_width = 8.27 * 72
    page_height = 11.69 * 72

    # Determine the border width of the text
    border_widths = determine_border_width(elements, page_width, page_height)

    #st.subheader("Text Elements with Font Style and Size")
    #st.write(elements)

    st.subheader("Border Widths")
    border_df = pd.DataFrame.from_dict(border_widths, orient='index', columns=['Width (points)', 'Width (inches)'])
    border_df['Width (inches)'] = border_df['Width (inches)'].apply(lambda x: f"{float(x):.4f}")
    st.write(border_df)

    standard_margin = 0.5  # Standard margin in inches
    for border, (_, width_inches) in border_df.iterrows():
        width_inches = float(width_inches)  # Ensure width_inches is a float
        if width_inches < standard_margin:
            st.write(f"The {border.replace('_', ' ')} is too narrow by {standard_margin - width_inches:.4f} inches.")
        elif width_inches > standard_margin:
            st.write(f"The {border.replace('_', ' ')} is too wide by {width_inches - standard_margin:.4f} inches.")

    # Check font style and size for normal text
    normal_text_match_percentage, normal_text_mismatches = check_normal_text(elements)

    st.subheader("Normal Text Font Style and Size Match")
    st.write(f"Match Percentage: {normal_text_match_percentage:.2f}%")
    if normal_text_mismatches:
        st.write("Normal text that do not match the standard:")
        for mismatch in normal_text_mismatches:
            st.write(f"- {mismatch}")

    # Plotting the pie chart for normal text
    fig, ax = plt.subplots()
    ax.pie(
        [normal_text_match_percentage, 100 - normal_text_match_percentage], 
        labels=["Matching Normal Text", "Non-Matching Normal Text"], 
        autopct='%1.1f%%', 
        colors=['#4CAF50', '#FF5722']
    )
    ax.set_title("Normal Text Font Style and Size Match Percentage")
    st.pyplot(fig)