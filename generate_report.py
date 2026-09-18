import os
import re
import subprocess

files_to_concat = [
    "report/front-matter/01-front-page.md",
    "report/front-matter/02-version-register.md",
    "report/front-matter/03-collaboration-insights.md",
    "report/front-matter/04-content.md",
    "report/front-matter/05-student-outcome.md",
    "report/11-startup-profile.md",
    "report/12-solution-profile.md",
    "report/13-segmentos-objetivo.md",
    "report/21-competidores.md",
    "report/22-entrevistas.md",
    "report/23-needfinding.md",
    "report/24-event-storming.md",
    "report/25-ubiquitous-language.md",
    "report/31-user-stories.md",
    "report/32-impact-mapping.md",
    "report/33-product-backlog.md",
    "report/41-style-guidelines.md",
    "report/42-information-architecture.md",
    "report/43-landing-page-ui-design.md",
    "report/44-web-applications-ux-ui-design.md",
    "report/45-web-applications-prototyping.md",
    "report/46-domain-driven-software-architecture.md",
    "report/47-software-object-oriented-design.md",
    "report/48-database-design.md",
    "report/51-software-configuration-management.md",
    "report/52-landing-page-services-applications-implementation.md",
    "report/61-conclusiones.md",
    "report/62-bibliografia.md",
    "report/63-anexos.md"
]

full_content = []

for fname in files_to_concat:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as infile:
            content = infile.read()
            full_content.append(content)
            full_content.append("\n\n<div style=\"page-break-after: always;\"></div>\n\n")
    else:
        print(f"Warning: {fname} does not exist.")

merged_text = "".join(full_content)

# Normalize all image paths for root execution
# 1. Replace ../../assets/ with assets/
# 2. Replace ../assets/ with assets/
merged_text = re.sub(r'(\.\./)+assets/', 'assets/', merged_text)
# Fix perfil.jpg to Perfil_Emanuel.png
merged_text = merged_text.replace('assets/images/perfil.jpg', 'assets/images/chapter1/Perfil_Emanuel.png')

# Save consolidated markdown files
output_filenames = [
    "upc-pre-202620-1asi0730-8084-StackRoot-report-av1.md",
    "upc-pre-202620-1asi0730-NRC-StackRoot-report-av1.md"
]

for out_name in output_filenames:
    with open(out_name, 'w', encoding='utf-8') as outfile:
        outfile.write(merged_text)
    print(f"Saved: {out_name}")

# Verify image paths
print("\n--- Verifying image paths in consolidated markdown ---")
all_matches = []
for m in re.finditer(r"!\[(.*?)\]\((.*?)\)", merged_text):
    all_matches.append(("md", m.group(1), m.group(2)))
for m in re.finditer(r"<img [^>]*src=[\"\x27](.*?)[\"\x27]", merged_text):
    all_matches.append(("html", "", m.group(1)))

missing_count = 0
for t, alt, path in all_matches:
    if not os.path.exists(path):
        print(f"MISSING IMAGE: {path}")
        missing_count += 1

if missing_count == 0:
    print("ALL images exist and resolved successfully! (0 missing)")
else:
    print(f"Total missing images: {missing_count}")

# Conversion to Word (.docx)
print("\n--- Converting to Word (.docx) ---")
subprocess.run([
    "pandoc",
    "upc-pre-202620-1asi0730-8084-StackRoot-report-av1.md",
    "-o", "upc-pre-202620-1asi0730-8084-StackRoot-report-av1.docx",
    "--resource-path=."
], check=True)
subprocess.run(["cp", "upc-pre-202620-1asi0730-8084-StackRoot-report-av1.docx", "upc-pre-202620-1asi0730-NRC-StackRoot-report-av1.docx"])

subprocess.run([
    "pandoc",
    "upc-pre-202620-1asi0730-8084-StackRoot-performance-av1.md",
    "-o", "upc-pre-202620-1asi0730-8084-StackRoot-performance-av1.docx",
    "--resource-path=."
], check=True)
subprocess.run(["cp", "upc-pre-202620-1asi0730-8084-StackRoot-performance-av1.docx", "upc-pre-202620-1asi0730-NRC-StackRoot-performance-av1.docx"])
print("Word (.docx) files generated successfully!")

# Conversion to PDF (.pdf)
print("\n--- Converting to PDF (.pdf) ---")
css = """
@page { size: A4; margin: 20mm 15mm 20mm 15mm; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; font-size: 11pt; line-height: 1.5; color: #1a1a1a; background: #ffffff; }
h1, h2, h3, h4, h5, h6 { color: #0f172a; font-weight: 700; margin-top: 1.2em; margin-bottom: 0.5em; page-break-after: avoid; }
h1 { font-size: 20pt; border-bottom: 2px solid #e2e8f0; padding-bottom: 6px; }
h2 { font-size: 16pt; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; }
h3 { font-size: 13pt; }
table { width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 9pt; page-break-inside: auto; }
tr { page-break-inside: avoid; page-break-after: auto; }
thead { display: table-header-group; }
th, td { border: 1px solid #cbd5e1; padding: 6px 8px; text-align: left; vertical-align: top; }
th { background-color: #f1f5f9; font-weight: 600; }
img { max-width: 100%; height: auto; display: block; margin: 10px auto; page-break-inside: avoid; }
blockquote { border-left: 4px solid #3b82f6; margin: 1em 0; padding: 0.5em 1em; background: #f8fafc; color: #475569; }
code { background: #f1f5f9; padding: 2px 4px; border-radius: 4px; font-family: monospace; font-size: 0.9em; }
pre { background: #0f172a; color: #f8fafc; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 9pt; }
"""

css_path = "/tmp/pdf_style.css"
with open(css_path, "w") as f:
    f.write(css)

def md_to_pdf(md_file, pdf_file):
    html_file = os.path.abspath(md_file.replace(".md", ".html"))
    pdf_dest = os.path.abspath(pdf_file)
    subprocess.run([
        "pandoc", md_file, "-s", "--embed-resources", "--standalone",
        f"--css={css_path}", "--resource-path=.", "-o", html_file
    ], check=True)
    
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.run([
        chrome_bin, "--headless", "--disable-gpu",
        f"--print-to-pdf={pdf_dest}", "--no-pdf-header-footer",
        f"file://{html_file}"
    ], check=True)
    if os.path.exists(html_file):
        os.remove(html_file)

md_to_pdf("upc-pre-202620-1asi0730-8084-StackRoot-performance-av1.md", "upc-pre-202620-1asi0730-8084-StackRoot-performance-av1.pdf")
subprocess.run(["cp", "upc-pre-202620-1asi0730-8084-StackRoot-performance-av1.pdf", "upc-pre-202620-1asi0730-NRC-StackRoot-performance-av1.pdf"])

md_to_pdf("upc-pre-202620-1asi0730-8084-StackRoot-report-av1.md", "upc-pre-202620-1asi0730-8084-StackRoot-report-av1.pdf")
subprocess.run(["cp", "upc-pre-202620-1asi0730-8084-StackRoot-report-av1.pdf", "upc-pre-202620-1asi0730-NRC-StackRoot-report-av1.pdf"])

if os.path.exists(css_path):
    os.remove(css_path)

print("PDF (.pdf) files generated successfully!")
