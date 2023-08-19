import os

from split_settings.tools import include
from decouple import config
from pathlib import Path


def include_files(base_path, module_name, skipped_modules=None):
    skipped_modules = skipped_modules if skipped_modules else list()
    root_path = os.path.join(base_path, module_name)
    modules = [
        f"{module_name}/{file}" for file in os.listdir(root_path)
        if file.endswith('py') and file not in skipped_modules
    ]
    include(*modules)


settings_root_path = Path(__file__).parent
include_files(settings_root_path, 'components')
include(f"environments/{config('DJANGO_ENV', 'dev')}.py")
