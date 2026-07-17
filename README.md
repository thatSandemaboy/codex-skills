# Codex Skills

Public repository for reusable Codex skills.

Each skill lives in `skills/<skill-name>/` and includes a `SKILL.md` file that Codex can load. Human-facing notes live beside the skill or in `docs/`, while `inventory/skills.json` provides a machine-readable directory.

## Skills

| Skill | Purpose | Install |
| --- | --- | --- |
| [readwise-categorization](skills/readwise-categorization/) | Categorize saved Readwise Reader documents with exactly two tags: `Domain + Lens`. | `./scripts/install-skill.sh readwise-categorization` |

## Install A Skill

Clone the repo:

```bash
git clone https://github.com/thatSandemaboy/codex-skills.git
cd codex-skills
```

Install one skill into Codex:

```bash
./scripts/install-skill.sh readwise-categorization
```

Install every skill:

```bash
./scripts/install-all.sh
```

By default, scripts install into `${CODEX_HOME:-$HOME/.codex}/skills`.

## Repository Layout

```text
.
├── README.md
├── docs/
│   └── readwise-categorization.md
├── inventory/
│   └── skills.json
├── scripts/
│   ├── index-skills.mjs
│   ├── install-all.sh
│   └── install-skill.sh
└── skills/
    ├── README.md
    └── readwise-categorization/
        ├── README.md
        └── SKILL.md
```

## Add A New Skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Keep the folder name lowercase with hyphens.
3. Add a short `README.md` in the skill folder for GitHub visitors.
4. Run `node scripts/index-skills.mjs`.
5. Commit the updated skill and inventory.

## Skill Folder Contract

For Codex compatibility, every skill folder needs:

- `SKILL.md` with YAML frontmatter containing `name` and `description`.
- Optional `scripts/`, `references/`, or `assets/` folders when the skill needs reusable resources.

The public README files are for people browsing GitHub; `SKILL.md` remains the source of truth for Codex.
