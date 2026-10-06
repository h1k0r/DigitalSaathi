with open('scripts/gen_tools_convert.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace all ${( ... )} with ${{ ( ... ) }}
text = text.replace('${(pdfBlob.size / 1024).toFixed(1)}', '${{ (pdfBlob.size / 1024).toFixed(1) }}')
text = text.replace('${(zipBlob.size / 1024).toFixed(1)}', '${{ (zipBlob.size / 1024).toFixed(1) }}')
text = text.replace('\\s', '\\\\s')

with open('scripts/gen_tools_convert.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed gen_tools_convert.py.")
