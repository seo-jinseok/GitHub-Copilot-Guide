const fs = require('fs');
const path = require('path');

// Usage: node generate-toc.js <file-to-update.md>
const args = process.argv.slice(2);
if (args.length === 0) {
    console.error('Error: Please provide a file path as an argument.');
    console.error('Usage: node generate-toc.js <file.md>');
    process.exit(1);
}

const filePath = path.resolve(args[0]);

if (!fs.existsSync(filePath) || !filePath.endsWith('.md')) {
    console.error(`Error: File does not exist or is not a markdown file: ${filePath}`);
    process.exit(1);
}

const content = fs.readFileSync(filePath, 'utf8');
const headerRegex = /^(##|###)\s(.*)/gm;
const tocMarker = '<!-- TOC -->';
const tocLines = [];
let match;

console.log(`Scanning ${filePath} for headers...`);

while ((match = headerRegex.exec(content)) !== null) {
    const level = match[1].length; // ## -> 2, ### -> 3
    const title = match[2].trim();
    // Simple slug generation (GitHub-compatible)
    const slug = title.toLowerCase()
        .replace(/[^\w\s-]/g, '') // Remove special characters
        .replace(/\s+/g, '-');   // Replace spaces with hyphens

    const indent = level === 3 ? '  ' : '';
    tocLines.push(`${indent}- [${title}](#${slug})`);
}

if (tocLines.length === 0) {
    console.log('No H2 or H3 headers found. Nothing to generate.');
    process.exit(0);
}

const tocMarkdown = '## 목차 (Table of Contents)\n\n' + tocLines.join('\n');

if (content.includes(tocMarker)) {
    const newContent = content.replace(tocMarker, tocMarkdown);
    fs.writeFileSync(filePath, newContent, 'utf8');
    console.log(`TOC successfully generated and inserted into ${filePath}`);
} else {
    console.warn(`Warning: No '<!-- TOC -->' marker found in ${filePath}. Could not insert TOC.`);
    console.log('\nGenerated TOC:\n');
    console.log(tocMarkdown);
}
