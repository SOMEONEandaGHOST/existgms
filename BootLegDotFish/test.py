import os
from lxml import etree
from bs4 import BeautifulSoup

# Convert HTML to XML (XHTML)
def convert_html_to_xml(input_html, output_xml):
    with open(input_html, "rb") as file:  # Read as bytes (fixes encoding issue)
        html_content = file.read()

    # Parse HTML using lxml
    parser = etree.HTMLParser(recover=True)  # Allows recovering from malformed HTML
    root = etree.fromstring(html_content, parser)  # Parse bytes, not string

    # Convert _Element to ElementTree and write to XML
    tree = etree.ElementTree(root)
    tree.write(output_xml, pretty_print=True, xml_declaration=True, encoding="UTF-8")

    print(f"Converted {input_html} to {output_xml}")

# Wrap JS in XML
def wrap_js_in_xml(input_js, output_xml):
    with open(input_js, "r", encoding="utf-8") as file:
        js_code = file.read()

    xml_content = f"<Script>\n<![CDATA[\n{js_code}\n]]>\n</Script>"

    with open(output_xml, "w", encoding="utf-8") as file:
        file.write(xml_content)
    print(f"Wrapped {input_js} into {output_xml}")

# Convert all files in a folder
def convert_files_in_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if item.endswith(".html"):  # For HTML files
            convert_html_to_xml(item_path, os.path.join(folder_path, f"{os.path.splitext(item)[0]}.xml"))
        elif item.endswith(".js"):  # For JS files
            wrap_js_in_xml(item_path, os.path.join(folder_path, f"{os.path.splitext(item)[0]}.xml"))

# Example usage
convert_files_in_folder(r"C:\Users\stone\Downloads\ExistenceGMS (1)")
