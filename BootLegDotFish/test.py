import os
from lxml import etree

# Convert HTML to Google Gadget XML
def convert_html_to_gadget_xml(input_html, output_xml):
    with open(input_html, "rb") as file:  # Read as bytes (fixes encoding issue)
        html_content = file.read()

    # Parse HTML using lxml
    parser = etree.HTMLParser(recover=True)  # Allows recovering from malformed HTML
    root = etree.fromstring(html_content, parser)

    # Create a new root <Module> tag for the Google Gadget
    module_element = etree.Element("Module")
    
    # Add <ModulePrefs> as required for Google Gadgets
    module_prefs = etree.SubElement(module_element, "ModulePrefs", title="My Gadget", height="300", width="300", view="home")
    
    # Add the parsed HTML content under <Content> tag
    content_element = etree.SubElement(module_element, "Content")
    content_element.append(root)

    # Convert _Element to ElementTree and write to XML
    tree = etree.ElementTree(module_element)
    tree.write(output_xml, pretty_print=True, xml_declaration=True, encoding="UTF-8")

    print(f"Converted {input_html} to Google Gadget format at {output_xml}")

# Convert all files in a folder
def convert_files_in_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if item.endswith(".html"):  # For HTML files
            convert_html_to_gadget_xml(item_path, os.path.join(folder_path, f"{os.path.splitext(item)[0]}.xml"))

# Example usage
convert_files_in_folder(r"C:\Users\stone\Downloads\BootLegDotFish")
