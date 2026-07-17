#!/usr/bin/env node
import { readdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const skillsRoot = path.join(repoRoot, "skills");
const inventoryPath = path.join(repoRoot, "inventory", "skills.json");

function parseFrontmatter(markdown) {
  const match = markdown.match(/^---\n([\s\S]*?)\n---/);
  if (!match) {
    throw new Error("Missing YAML frontmatter");
  }

  const values = {};
  for (const line of match[1].split("\n")) {
    const pair = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (pair) {
      values[pair[1]] = pair[2].replace(/^["']|["']$/g, "");
    }
  }
  return values;
}

let previousInventory = { skills: [] };
try {
  previousInventory = JSON.parse(await readFile(inventoryPath, "utf8"));
} catch {
  previousInventory = { skills: [] };
}

const previousByName = new Map((previousInventory.skills || []).map((skill) => [skill.name, skill]));
const entries = await readdir(skillsRoot, { withFileTypes: true });
const skills = [];

for (const entry of entries) {
  if (!entry.isDirectory()) continue;

  const skillName = entry.name;
  const skillPath = path.join(skillsRoot, skillName, "SKILL.md");

  let markdown;
  try {
    markdown = await readFile(skillPath, "utf8");
  } catch {
    continue;
  }

  const frontmatter = parseFrontmatter(markdown);
  if (frontmatter.name !== skillName) {
    throw new Error(`Skill folder ${skillName} does not match SKILL.md name ${frontmatter.name}`);
  }

  const previous = previousByName.get(frontmatter.name) || {};

  skills.push({
    name: frontmatter.name,
    path: `skills/${skillName}`,
    skill_file: `skills/${skillName}/SKILL.md`,
    docs: `docs/${skillName}.md`,
    description: frontmatter.description,
    tags: previous.tags || [],
    status: previous.status || "active"
  });
}

skills.sort((a, b) => a.name.localeCompare(b.name));

await writeFile(
  inventoryPath,
  `${JSON.stringify({ schema_version: "1.0.0", repo: "thatSandemaboy/codex-skills", skills }, null, 2)}\n`
);

console.log(`Indexed ${skills.length} skill(s)`);
