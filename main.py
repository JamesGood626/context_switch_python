import sys
from helpers import open_contexts


def main():
    args_len = len(sys.argv)
    if args_len > 1:
        # removes main.py from the list
        # so that the rest of the items in the list
        # refer to a key in the context_dict
        del sys.argv[0]
        open_contexts(sys.argv)
    else:
        return


main()

# open_ebooks([erlang_in_anger_path, second_book_path])

# open_new_browser_tab(urls[0])


# def open_ebooks(paths):
#     subprocess.Popen([PREVIEW_EXE_PATH, *paths])


# def open_project_in_vscode(path):
#     os.system("code " + path)


# def open_new_browser_tab(url):
#     webbrowser.open_new_tab(url)
