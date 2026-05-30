# {{PROJECT_NAME}}

> Project dashboard. Each section is a live Base — requires Obsidian 1.8+ with the Bases core plugin enabled.

---

## All Notes

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "type", "field": "type", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": []
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [{ "field": "status", "operator": "eq", "value": "draft" }]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [{ "field": "status", "operator": "eq", "value": "complete" }]
      }
    }
  ]
}
```

---

## Characters

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "role", "field": "role", "type": "text" },
    { "id": "archetype", "field": "archetype", "type": "text" },
    { "id": "factions", "field": "factions", "type": "multitext" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "character" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "character" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "character" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```

---

## Locations

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "region", "field": "region", "type": "text" },
    { "id": "function", "field": "function", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "location" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "location" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "location" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```

---

## Factions

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "function", "field": "function", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "faction" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "faction" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "faction" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```

---

## Concepts

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "layer", "field": "layer", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "concept" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "concept" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "concept" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```

---

## Story

```base
{
  "schemaVersion": "1",
  "columns": [
    { "id": "file-name", "field": "file.name", "type": "text" },
    { "id": "status", "field": "status", "type": "text" },
    { "id": "scope", "field": "scope", "type": "text" },
    { "id": "last_updated", "field": "last_updated", "type": "date" }
  ],
  "filters": {
    "conjunction": "AND",
    "conditions": [{ "field": "type", "operator": "eq", "value": "story" }]
  },
  "sort": [{ "field": "last_updated", "direction": "desc" }],
  "views": [
    { "id": "all", "name": "All", "type": "table" },
    {
      "id": "draft", "name": "Draft", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "story" },
          { "field": "status", "operator": "eq", "value": "draft" }
        ]
      }
    },
    {
      "id": "complete", "name": "Complete", "type": "table",
      "filters": {
        "conjunction": "AND",
        "conditions": [
          { "field": "type", "operator": "eq", "value": "story" },
          { "field": "status", "operator": "eq", "value": "complete" }
        ]
      }
    }
  ]
}
```
