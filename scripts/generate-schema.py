"""
Script to generate JSON schemas and markdown documentation from pydantic models.
Usage: python scripts/generate-schema.py

"""
from json import dumps
import erdantic as erd
from pathlib import Path

from digitalcrust.interchange_schemas import FieldSite

__root__ = Path(__file__).parent.parent

# Get the output directory
output_dir = __root__ / "output"
if not output_dir.exists():
    output_dir.mkdir(parents=True, exist_ok=True)
name = "field-site"

models = [FieldSite]

graph = erd.create(*models)

# Draw the entity-relation diagram
erd_file = output_dir / (name + ".png")
graph.draw(out=erd_file)


schemas = [mod.model_json_schema() for mod in models]

json_file = output_dir / (name + ".json")
with json_file.open("w") as f:
    f.write(dumps(schemas, indent=2))

