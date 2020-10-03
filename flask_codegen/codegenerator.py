import os
from sqlalchemy import inspect
from app import db  # TODO: This needs to be configurable somehow?
from .util import create_dir, log


class CodeGenerator:
    def __init__(self, entity: str):
        self._entity = entity
        self._db = db

        self._initialise_empty_structure()
        self._schema = self._load_schema()

    def _initialise_empty_structure(self):
        if os.path.exists("blueprints"):
            log("blueprints directory already exists")
            return

        log("blueprints directory does not exist, creating")
        create_dir("blueprints")

    def _load_schema(self):
        log("Loading schema")
        schema = {}
        inspector = inspect(self._db.engine)
        for table in inspector.get_table_names():
            log(f"Loading {table}")
            schema[table] = inspector.get_columns(table)
        log("Loaded schema")
        log(schema)

        return schema

    def all(self):
        log(f"Generating all for {self._entity}")

    def models(self):
        log(f"Generating models for {self._entity}")

    def routes(self):
        log(f"Generating routes for {self._entity}")

    def forms(self):
        log(f"Generating forms for {self._entity}")

    def templates(self):
        log(f"Generating templates for {self._entity}")
