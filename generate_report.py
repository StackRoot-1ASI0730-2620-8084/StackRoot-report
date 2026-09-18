import os

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

output_filename = "upc-pre-202620-1asi0730-NRC-StackRoot-report-av1.md"

with open(output_filename, 'w', encoding='utf-8') as outfile:
    for fname in files_to_concat:
        if os.path.exists(fname):
            with open(fname, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n<div style=\"page-break-after: always;\"></div>\n\n")
        else:
            print(f"Warning: {fname} does not exist.")

print(f"Successfully created {output_filename}")
