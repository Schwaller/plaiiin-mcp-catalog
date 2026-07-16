Provide persistent memory capabilities through Neo4j graph database integration.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/neo4j-memory](https://hub.docker.com/repository/docker/mcp/neo4j-memory)
**Author**|[neo4j-contrib](https://github.com/neo4j-contrib)
**Repository**|https://github.com/neo4j-contrib/mcp-neo4j

## Available Tools (9)
Tools provided by this Server|Short Description
-|-
`add_observations`|Add Observations|
`create_entities`|Create Entities|
`create_relations`|Create Relations|
`delete_entities`|Delete Entities|
`delete_observations`|Delete Observations|
`delete_relations`|Delete Relations|
`find_memories_by_name`|Find Memories by Name|
`read_graph`|Read Graph|
`search_memories`|Search Memories|

---
## Tools Details

#### Tool: **`add_observations`**
Add new observations/facts to existing entities in the knowledge graph.

Appends new observations to entities that already exist. The entity must be present
in the graph before adding observations. Each observation should be a distinct fact.

Returns:
    list[dict]: Details about the added observations including entity name and new facts

Example call:
{
    "observations": [
        {
            "entityName": "Alice Johnson",
            "observations": ["Promoted to Senior Engineer", "Completed AWS certification"]
        },
        {
            "entityName": "Microsoft",
            "observations": ["Launched new AI products", "Stock price increased 15%"]
        }
    ]
}
Parameters|Type|Description
-|-|-
`observations`|`array`|List of observations to add to existing entities

*This tool interacts with external entities.*

---
#### Tool: **`create_entities`**
Create multiple new entities in the knowledge graph.

Creates new memory entities with their associated observations. If an entity with the same name
already exists, this operation will merge the observations with existing ones.

Returns:
    list[Entity]: The created entities with their final state

Example call:
{
    "entities": [
        {
            "name": "Alice Johnson",
            "type": "person",
            "observations": ["Software engineer", "Lives in Seattle", "Enjoys hiking"]
        },
        {
            "name": "Microsoft",
            "type": "company", 
            "observations": ["Technology company", "Headquartered in Redmond, WA"]
        }
    ]
}
Parameters|Type|Description
-|-|-
`entities`|`array`|List of entities to create with name, type, and observations

*This tool interacts with external entities.*

---
#### Tool: **`create_relations`**
Create multiple new relationships between existing entities in the knowledge graph.

Creates directed relationships between entities that already exist. Both source and target
entities must already be present in the graph. Use descriptive relationship types.

Returns:
    list[Relation]: The created relationships

Example call:
{
    "relations": [
        {
            "source": "Alice Johnson",
            "target": "Microsoft", 
            "relationType": "WORKS_AT"
        },
        {
            "source": "Alice Johnson",
            "target": "Seattle",
            "relationType": "LIVES_IN"
        }
    ]
}
Parameters|Type|Description
-|-|-
`relations`|`array`|List of relations to create between existing entities

*This tool interacts with external entities.*

---
#### Tool: **`delete_entities`**
Delete entities and all their associated relationships from the knowledge graph.

Permanently removes entities from the graph along with all relationships they participate in.
This is a destructive operation that cannot be undone. Entity names must match exactly.

Returns:
    str: Success confirmation message

Example call:
{
    "entityNames": ["Old Company", "Outdated Person"]
}

Warning: This will delete the entities and ALL relationships they're involved in.
Parameters|Type|Description
-|-|-
`entityNames`|`array`|List of exact entity names to delete permanently

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`delete_observations`**
Delete specific observations from existing entities in the knowledge graph.

Removes specific observation texts from entities. The observation text must match exactly
what is stored. The entity will remain but the specified observations will be deleted.

Returns:
    str: Success confirmation message

Example call:
{
    "deletions": [
        {
            "entityName": "Alice Johnson",
            "observations": ["Old job title", "Outdated phone number"]
        },
        {
            "entityName": "Microsoft", 
            "observations": ["Former CEO information"]
        }
    ]
}

Note: Observation text must match exactly (case-sensitive) to be deleted.
Parameters|Type|Description
-|-|-
`deletions`|`array`|List of specific observations to remove from entities

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`delete_relations`**
Delete specific relationships between entities in the knowledge graph.

Removes relationships while keeping the entities themselves. The source, target, and 
relationship type must match exactly for deletion. This only affects the relationships,
not the entities they connect.

Returns:
    str: Success confirmation message

Example call:
{
    "relations": [
        {
            "source": "Alice Johnson",
            "target": "Old Company",
            "relationType": "WORKS_AT"
        },
        {
            "source": "John Smith", 
            "target": "Former City",
            "relationType": "LIVES_IN"
        }
    ]
}

Note: All fields (source, target, relationType) must match exactly for deletion.
Parameters|Type|Description
-|-|-
`relations`|`array`|List of specific relationships to delete from the graph

*This tool may perform destructive updates.*

*This tool is idempotent. Repeated calls with same args have no additional effect.*

*This tool interacts with external entities.*

---
#### Tool: **`find_memories_by_name`**
Find specific entities by their exact names.

Retrieves entities that exactly match the provided names, along with all their
relationships and connected entities. Use this when you know the exact entity names.

Returns:
    KnowledgeGraph: Subgraph containing the specified entities and their relationships

Example call:
{
    "names": ["Alice Johnson", "Microsoft", "Seattle"]
}

This retrieves the entities with exactly those names plus their connections.
Parameters|Type|Description
-|-|-
`names`|`array`|List of exact entity names to retrieve

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
#### Tool: **`read_graph`**
Read the entire knowledge graph with all entities and relationships.

Returns the complete memory graph including all stored entities and their relationships.
Use this to get a full overview of stored knowledge.

Returns:
    KnowledgeGraph: Complete graph with all entities and relations

Example response:
{
    "entities": [
        {"name": "John Smith", "type": "person", "observations": ["Works at Neo4j"]},
        {"name": "Neo4j Inc", "type": "company", "observations": ["Graph database company"]}
    ],
    "relations": [
        {"source": "John Smith", "target": "Neo4j Inc", "relationType": "WORKS_AT"}
    ]
}
#### Tool: **`search_memories`**
Search for entities in the knowledge graph using fulltext search.

Searches across entity names, types, and observations using Neo4j's fulltext index.
Returns matching entities and their related connections. Supports partial matches
and multiple search terms.

Returns:
    KnowledgeGraph: Subgraph containing matching entities and their relationships

Example call:
{
    "query": "engineer software"
}

This searches for entities containing "engineer" or "software" in their name, type, or observations.
Parameters|Type|Description
-|-|-
`query`|`string`|Fulltext search query to find entities by name, type, or observations

*This tool is read-only. It does not modify its environment.*

*This tool interacts with external entities.*

---
