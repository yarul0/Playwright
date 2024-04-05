import pandas as pd

# Define the checklist items
checklist_items = [
    {"Category": "Basic SEO Analysis",
     "Check": "Verify optimization of title tags and meta descriptions on key pages."},
    {"Category": "Basic SEO Analysis",
     "Check": "Check for logical use of headings (H1, H2, H3) with relevant keywords."},
    {"Category": "Basic SEO Analysis", "Check": "Assess content quality for uniqueness and audience relevance."},
    {"Category": "Basic SEO Analysis", "Check": "Review internal linking structure and quality."},
    {"Category": "Basic SEO Analysis", "Check": "Ensure keywords are naturally integrated in content."},
    {"Category": "Basic SEO Analysis", "Check": "Confirm site is responsive on various devices."},
    {"Category": "Basic SEO Analysis", "Check": "Check for clean, SEO-friendly URLs."},
    {"Category": "Basic SEO Analysis", "Check": "Ensure an updated XML sitemap is in place."},
    {"Category": "Basic SEO Analysis", "Check": "Verify correct configuration of robots.txt."},
    {"Category": "Page Speed and Performance",
     "Check": "Utilize tools like Google PageSpeed Insights to check load time."},
    {"Category": "Page Speed and Performance", "Check": "Confirm images are optimized in size and format."},
    {"Category": "Page Speed and Performance", "Check": "Check caching and compression mechanisms."},
    {"Category": "Page Speed and Performance", "Check": "Ensure CSS and JavaScript are minified."},
    {"Category": "Page Speed and Performance", "Check": "Test and optimize server response time."},
    {"Category": "Page Speed and Performance", "Check": "Analyze and optimize resource usage."},
    {"Category": "User Experience (UX) and Engagement", "Check": "Evaluate navigation for ease and logic."},
    {"Category": "User Experience (UX) and Engagement", "Check": "Check for clear and actionable CTAs."},
    {"Category": "User Experience (UX) and Engagement", "Check": "Assess text formatting and legibility."},
    {"Category": "User Experience (UX) and Engagement", "Check": "Confirm adherence to WCAG accessibility standards."},
    {"Category": "User Experience (UX) and Engagement", "Check": "Analyze and address high bounce rate pages."},
    {"Category": "User Experience (UX) and Engagement", "Check": "Ensure effective social media linking and presence."},
    {"Category": "Technical and Security Review", "Check": "Identify and fix any broken links."},
    {"Category": "Technical and Security Review", "Check": "Verify SSL certificate implementation and validity."},
    {"Category": "Technical and Security Review", "Check": "Conduct a vulnerability scan for security risks."},
    {"Category": "Technical and Security Review", "Check": "Review password policies and access controls."},
    {"Category": "Content and Legal Compliance", "Check": "Check for and resolve any duplicate content issues."},
    {"Category": "Content and Legal Compliance", "Check": "Evaluate content update frequency and relevance."},
    {"Category": "Content and Legal Compliance", "Check": "Verify alt text and accessibility of multimedia elements."},
    {"Category": "Content and Legal Compliance", "Check": "Ensure compliance with data protection laws like GDPR."},
    {"Category": "Content and Legal Compliance",
     "Check": "Confirm the presence and update status of Terms of Service."},
    {"Category": "Analytics and Conversion Tracking",
     "Check": "Ensure comprehensive tracking with tools like Google Analytics."},
    {"Category": "Analytics and Conversion Tracking",
     "Check": "Verify the effectiveness of CTAs and conversion paths."},
    {"Category": "Analytics and Conversion Tracking", "Check": "Check for site verification in Google Search Console."},
    {"Category": "General Advice and Maintenance", "Check": "Ensure all components are up-to-date."},
    {"Category": "General Advice and Maintenance", "Check": "Verify regular and reliable backup processes."},
    {"Category": "General Advice and Maintenance", "Check": "Consider implementing user feedback tools."},
]

# Create a DataFrame
df_checklist = pd.DataFrame(checklist_items)

# Define the file name
file_name = '/mnt/data/Website_Audit_Checklist.xlsx'

# Write the DataFrame to an Excel file
df_checklist.to_excel(file_name, index=False)

file_name
