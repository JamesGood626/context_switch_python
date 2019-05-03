from paths import DEV_DIR_PATH
from ebook_paths import PROGRAMMING_PHOENIX, PROPERTY_BASED_TESTING
from project_paths import BUDGET_CLIENT, BUDGET_APP

context_dict = {
    "cardsail_react": {
        "ebooks": [PROGRAMMING_PHOENIX, PROPERTY_BASED_TESTING],
        "urls": ['https://jamesgood.io', 'https://www.google.com'],
        "projects": [BUDGET_CLIENT, BUDGET_APP],
    },
    "svelte": {
        "ebooks": [],
        # want to see how svelte approaches state management
        "urls": ["https://svelte.dev/tutorial/writable-stores"],
        "projects": []
    }
}
