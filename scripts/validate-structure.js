const fs = require('fs');
const path = require('path');

const DOCS_DIR = path.join(__dirname, '../docs');
let hasErrors = false;

// Regex to find markdown links, excluding http/https links: [text](link)
const markdownLinkRegex = /\[([^\]]+)\]\((?!https?:\/\/)([^)]+)\)/g;

function validateFileName(filePath) {
    const fileName = path.basename(filePath);
    // Simple rule: no spaces allowed.
    if (/\s/.test(fileName)) {
        console.error(`ERROR: File name contains whitespace: ${filePath}`);
        hasErrors = true;
    }
}

function validateFileContent(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const currentDir = path.dirname(filePath);
    let match;

    while ((match = markdownLinkRegex.exec(content)) !== null) {
        const link = match[2].split('#')[0]; // Ignore anchor part of the link
        if (!link) continue; // Skip if link is only an anchor

        const targetPath = path.resolve(currentDir, link);

        if (!fs.existsSync(targetPath)) {
            console.error(`ERROR: Broken link in ${filePath}`);
            console.error(`  -> Link: ${match[2]}`);
            console.error(`  -> Resolved Path: ${targetPath}\n`);
            hasErrors = true;
        }
    }
}

function traverseDir(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });

    for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);

        if (entry.isDirectory()) {
            traverseDir(fullPath);
        } else {
            validateFileName(fullPath);
            if (fullPath.endsWith('.md')) {
                validateFileContent(fullPath);
            }
        }
    }
}

console.log(`Starting validation in ${DOCS_DIR}...`);
traverseDir(DOCS_DIR);

if (hasErrors) {
    console.error('\nValidation failed with errors.');
    process.exit(1);
} else {
    console.log('\nValidation successful. All links and file names are OK.');
}
