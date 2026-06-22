# KRINEIA.md — governed-compression
---
krineia_manifest_version: "0.1"
schema: "krineia-manifest@0.1"
repo:
  full_name: "hummbl-dev/governed-compression"
  default_branch: "main"
authority:
  steward: "HUMMBL Research Institute"
  approving_human: "Reuben Bowlby"
governance_profile:
  status: "adopted"
  krineia_required: true
  trust_root_mode: "deployment_asserted"
chains:
  primary:
    chain_id: "governed-compression-primary"
    storage: "_receipts/krineia/primary.jsonl"
    genesis_policy: "repo_bootstrap"
    hash_algorithm: "sha256"
operators:
  allowed: ["append", "project", "cut"]
  forbidden: ["update", "delete", "rewrite"]
last_reviewed: "2026-06-22"
---
