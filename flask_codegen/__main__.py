import argparse
from .codegenerator import CodeGenerator

actions = ["all", "models", "routes", "forms", "templates"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser("flask_codegen")
    parser.add_argument(
        "action", choices=actions, help="Which files should be generated?"
    )
    parser.add_argument(
        "entity", help="Which entity should the files be generated for?"
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Print what would happen, but don't actually do anything",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    args = parser.parse_args()

    print(args)

    action = args.action
    entity = args.entity
    dry_run = args.dry_run
    verbose = args.verbose

    code_generator = CodeGenerator(entity)
    if action == "all":
        code_generator.all()
    elif action == "models":
        code_generator.models()
    elif action == "routes":
        code_generator.routes()
    elif action == "forms":
        code_generator.forms()
    elif action == "templates":
        code_generator.templates()
