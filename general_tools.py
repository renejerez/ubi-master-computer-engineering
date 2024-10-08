def summary_create(sections, parent_index="", level=1):
    toc_html = ""
    if level == 1:
        toc_html += '<h1>Scraping Scores and Number of Reviews<span class="tocSkip"></span></h1>\n<div class="toc">\n  <ul class="toc-item">\n'

    for i, (section_title, subsections) in enumerate(sections, start=1):
        current_index = f"{parent_index}{i}" if parent_index else str(i)
        toc_html += f'    <li><span><a href="#{section_title.replace(" ", "-")}" data-toc-modified-id="{section_title.replace(" ", "-")}-{current_index}"><span class="toc-item-num">{current_index}&nbsp;&nbsp;</span>{section_title}</a></span>\n'
        if subsections:
            toc_html += '      <div class="toc">\n        <ul class="toc-item">\n'
            toc_html += summary_create(subsections, current_index + ".", level + 1)
            toc_html += '        </ul>\n      </div>\n'
        toc_html += '    </li>\n'

    if level == 1:
        toc_html += '  </ul>\n</div>'
    return toc_html