SecureNote.link MCP Server - allowing AI agents to securely share sensitive information through end-to-end encrypted notes.

## MCP Info
Attribute|Details|
|-|-|
**Docker Image**|[mcp/securenote-link-mcp-server](https://hub.docker.com/repository/docker/mcp/securenote-link-mcp-server)
**Author**|[jackalterman](https://github.com/jackalterman)
**Repository**|https://github.com/jackalterman/securenote-link-MCP-server

## Available Tools (3)
Tools provided by this Server|Short Description
-|-
`create_note`|Encrypt a message and store it via the securenote.link API.|
`get_instructions`|Returns a guide on how to use this secure note sharing service, intended for both humans and AI agents.|
`get_note`|Retrieve and decrypt a note from the securenote.link API.|

---
## Tools Details

#### Tool: **`create_note`**
Encrypt a message and store it via the securenote.link API.

Returns the note ID, decryption key, shareable one-click URL, expiry,
and password-protection status.

The one-click URL embeds the decryption key in the fragment (#), which is
never sent to the server. For maximum security, share the URL and key
through separate channels.
Parameters|Type|Description
-|-|-
`text`|`string`|The plain-text message to encrypt and store.
`expires_in`|`integer` *optional*|Expiry time in hours — must be one of: 1, 24, 72, 168.
`password`|`string` *optional*|Optional password for additional protection.

---
#### Tool: **`get_instructions`**
Returns a guide on how to use this secure note sharing service,
intended for both humans and AI agents.
#### Tool: **`get_note`**
Retrieve and decrypt a note from the securenote.link API.
Parameters|Type|Description
-|-|-
`decryption_key`|`string`|The base64-encoded decryption key (from the URL fragment or create_note).
`secret_id`|`string`|The ID of the note to retrieve.
`password`|`string` *optional*|Required only if the note is password-protected.

---
