from versioning import chroma_versioning

# Sample document additions
chroma_versioning.add_version("v1", "This is the original scraped document.", {"stage": "scraped"})
chroma_versioning.add_version("v2", "This is the AI rewritten version.", {"stage": "rewritten"})

# Retrieve a specific version
doc = chroma_versioning.get_version("v2")
print("📄 Retrieved Document:", doc)

# List all stored versions
print("📚 All Version IDs:", chroma_versioning.list_versions())

# Semantic search demo
search_result = chroma_versioning.search_versions("AI rewritten")
print("🔍 Search Results:", search_result)
